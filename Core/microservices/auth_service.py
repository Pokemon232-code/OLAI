"""
Authentication Service - Unlimited Flexibility
No default limits, maximum capabilities by default
"""

import jwt
import bcrypt
import sqlite3
import json
import time
import threading
from typing import Dict, Any, Optional, List
from datetime import datetime, timedelta
import os
import hashlib
import secrets

class AuthService:
    """
    Advanced authentication service with unlimited capabilities
    - Unlimited users and sessions
    - Flexible password policies
    - OAuth integration
    - No default restrictions
    """
    
    def __init__(self):
        self.db_path = "auth.db"
        self.secret_key = os.getenv("JWT_SECRET", secrets.token_hex(32))
        self.algorithm = "HS256"
        self.session_timeout = None  # Unlimited by default
        self.password_policy = "flexible"  # No restrictions by default
        self.multi_factor_enabled = False
        self.oauth_providers = {}
        self.active_sessions = {}
        self.session_lock = threading.Lock()
        
        # Initialize database
        self._init_database()
    
    def initialize(self, config: Dict[str, Any] = None):
        """Initialize authentication service with unlimited configuration options"""
        if config:
            self.secret_key = config.get('secret_key', self.secret_key)
            self.algorithm = config.get('algorithm', self.algorithm)
            self.session_timeout = config.get('session_timeout', self.session_timeout)
            self.password_policy = config.get('password_policy', self.password_policy)
            self.multi_factor_enabled = config.get('multi_factor', self.multi_factor_enabled)
            self.oauth_providers = config.get('oauth_providers', {})
        
        return True
    
    def register_user(self,
                     username: str,
                     email: str,
                     password: str,
                     role: str = "user",
                     additional_data: Dict[str, Any] = None) -> Dict[str, Any]:
        """
        Register new user with unlimited flexibility
        - role: user, admin, moderator, custom
        - additional_data: Any custom user data
        """
        
        try:
            # Check if user already exists
            if self._user_exists(username, email):
                return {"success": False, "error": "User already exists"}
            
            # Validate password policy
            password_validation = self._validate_password(password)
            if not password_validation["valid"]:
                return {"success": False, "error": password_validation["error"]}
            
            # Hash password
            password_hash = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
            
            # Prepare user data
            user_data = {
                "username": username,
                "email": email,
                "password_hash": password_hash.decode('utf-8'),
                "role": role,
                "created_at": datetime.now().isoformat(),
                "last_login": None,
                "is_active": True,
                "additional_data": json.dumps(additional_data or {})
            }
            
            # Save user to database
            user_id = self._save_user(user_data)
            
            return {
                "success": True,
                "user_id": user_id,
                "username": username,
                "email": email,
                "role": role,
                "created_at": user_data["created_at"]
            }
            
        except Exception as e:
            return {"success": False, "error": str(e)}
    
    def authenticate_user(self,
                         username: str = None,
                         email: str = None,
                         password: str = None,
                         remember_me: bool = False) -> Dict[str, Any]:
        """
        Authenticate user with unlimited session duration
        - remember_me: True for unlimited session duration
        """
        
        try:
            # Find user
            user = self._find_user(username, email)
            if not user:
                return {"success": False, "error": "User not found"}
            
            # Check if user is active
            if not user["is_active"]:
                return {"success": False, "error": "User account is disabled"}
            
            # Verify password
            if password:
                if not bcrypt.checkpw(password.encode('utf-8'), user["password_hash"].encode('utf-8')):
                    return {"success": False, "error": "Invalid password"}
            
            # Generate JWT token
            token_data = {
                "user_id": user["id"],
                "username": user["username"],
                "email": user["email"],
                "role": user["role"],
                "iat": datetime.utcnow(),
                "exp": datetime.utcnow() + timedelta(days=365) if remember_me else None
            }
            
            # Remove exp if unlimited session
            if self.session_timeout is None or remember_me:
                token_data.pop("exp", None)
            
            token = jwt.encode(token_data, self.secret_key, algorithm=self.algorithm)
            
            # Create session
            session_id = secrets.token_hex(32)
            session_data = {
                "session_id": session_id,
                "user_id": user["id"],
                "token": token,
                "created_at": datetime.now().isoformat(),
                "last_activity": datetime.now().isoformat(),
                "expires_at": None if remember_me else (datetime.now() + timedelta(hours=24)).isoformat(),
                "ip_address": None,  # Would be set by request handler
                "user_agent": None   # Would be set by request handler
            }
            
            # Save session
            self._save_session(session_data)
            
            # Update last login
            self._update_last_login(user["id"])
            
            return {
                "success": True,
                "token": token,
                "session_id": session_id,
                "user": {
                    "id": user["id"],
                    "username": user["username"],
                    "email": user["email"],
                    "role": user["role"],
                    "last_login": datetime.now().isoformat()
                },
                "expires_at": session_data["expires_at"]
            }
            
        except Exception as e:
            return {"success": False, "error": str(e)}
    
    def validate_token(self, token: str) -> Dict[str, Any]:
        """Validate JWT token"""
        try:
            payload = jwt.decode(token, self.secret_key, algorithms=[self.algorithm])
            
            # Check if session exists and is valid
            session = self._get_session_by_token(token)
            if not session:
                return {"success": False, "error": "Invalid session"}
            
            # Update last activity
            self._update_session_activity(session["session_id"])
            
            return {
                "success": True,
                "user_id": payload["user_id"],
                "username": payload["username"],
                "email": payload["email"],
                "role": payload["role"],
                "session_id": session["session_id"]
            }
            
        except jwt.ExpiredSignatureError:
            return {"success": False, "error": "Token expired"}
        except jwt.InvalidTokenError:
            return {"success": False, "error": "Invalid token"}
        except Exception as e:
            return {"success": False, "error": str(e)}
    
    def logout_user(self, token: str = None, session_id: str = None) -> Dict[str, Any]:
        """Logout user and invalidate session"""
        try:
            if token:
                session = self._get_session_by_token(token)
                if session:
                    self._delete_session(session["session_id"])
            elif session_id:
                self._delete_session(session_id)
            else:
                return {"success": False, "error": "Token or session_id required"}
            
            return {"success": True, "message": "Logged out successfully"}
            
        except Exception as e:
            return {"success": False, "error": str(e)}
    
    def get_user_info(self, user_id: int = None, username: str = None, email: str = None) -> Dict[str, Any]:
        """Get user information"""
        try:
            user = self._find_user(username, email, user_id)
            if not user:
                return {"success": False, "error": "User not found"}
            
            # Remove sensitive data
            user_info = {
                "id": user["id"],
                "username": user["username"],
                "email": user["email"],
                "role": user["role"],
                "created_at": user["created_at"],
                "last_login": user["last_login"],
                "is_active": user["is_active"],
                "additional_data": json.loads(user["additional_data"]) if user["additional_data"] else {}
            }
            
            return {"success": True, "user": user_info}
            
        except Exception as e:
            return {"success": False, "error": str(e)}
    
    def update_user(self,
                   user_id: int,
                   username: str = None,
                   email: str = None,
                   role: str = None,
                   additional_data: Dict[str, Any] = None,
                   is_active: bool = None) -> Dict[str, Any]:
        """Update user information"""
        try:
            user = self._find_user(user_id=user_id)
            if not user:
                return {"success": False, "error": "User not found"}
            
            # Prepare update data
            update_data = {}
            if username is not None:
                update_data["username"] = username
            if email is not None:
                update_data["email"] = email
            if role is not None:
                update_data["role"] = role
            if additional_data is not None:
                update_data["additional_data"] = json.dumps(additional_data)
            if is_active is not None:
                update_data["is_active"] = is_active
            
            update_data["updated_at"] = datetime.now().isoformat()
            
            # Update user
            self._update_user(user_id, update_data)
            
            return {"success": True, "message": "User updated successfully"}
            
        except Exception as e:
            return {"success": False, "error": str(e)}
    
    def change_password(self,
                       user_id: int,
                       old_password: str,
                       new_password: str) -> Dict[str, Any]:
        """Change user password"""
        try:
            user = self._find_user(user_id=user_id)
            if not user:
                return {"success": False, "error": "User not found"}
            
            # Verify old password
            if not bcrypt.checkpw(old_password.encode('utf-8'), user["password_hash"].encode('utf-8')):
                return {"success": False, "error": "Invalid old password"}
            
            # Validate new password
            password_validation = self._validate_password(new_password)
            if not password_validation["valid"]:
                return {"success": False, "error": password_validation["error"]}
            
            # Hash new password
            new_password_hash = bcrypt.hashpw(new_password.encode('utf-8'), bcrypt.gensalt())
            
            # Update password
            self._update_user(user_id, {
                "password_hash": new_password_hash.decode('utf-8'),
                "updated_at": datetime.now().isoformat()
            })
            
            return {"success": True, "message": "Password changed successfully"}
            
        except Exception as e:
            return {"success": False, "error": str(e)}
    
    def get_active_sessions(self, user_id: int = None) -> Dict[str, Any]:
        """Get active sessions"""
        try:
            sessions = self._get_sessions(user_id)
            
            # Filter active sessions
            active_sessions = []
            for session in sessions:
                if session["expires_at"] is None or datetime.fromisoformat(session["expires_at"]) > datetime.now():
                    active_sessions.append({
                        "session_id": session["session_id"],
                        "created_at": session["created_at"],
                        "last_activity": session["last_activity"],
                        "expires_at": session["expires_at"],
                        "ip_address": session["ip_address"],
                        "user_agent": session["user_agent"]
                    })
            
            return {
                "success": True,
                "sessions": active_sessions,
                "count": len(active_sessions)
            }
            
        except Exception as e:
            return {"success": False, "error": str(e)}
    
    def revoke_session(self, session_id: str) -> Dict[str, Any]:
        """Revoke specific session"""
        try:
            self._delete_session(session_id)
            return {"success": True, "message": "Session revoked successfully"}
            
        except Exception as e:
            return {"success": False, "error": str(e)}
    
    def revoke_all_sessions(self, user_id: int) -> Dict[str, Any]:
        """Revoke all sessions for user"""
        try:
            sessions = self._get_sessions(user_id)
            for session in sessions:
                self._delete_session(session["session_id"])
            
            return {"success": True, "message": f"Revoked {len(sessions)} sessions"}
            
        except Exception as e:
            return {"success": False, "error": str(e)}
    
    def get_user_stats(self) -> Dict[str, Any]:
        """Get user statistics"""
        try:
            conn = sqlite3.connect(self.db_path)
            cursor = conn.cursor()
            
            # Get total users
            cursor.execute("SELECT COUNT(*) FROM users")
            total_users = cursor.fetchone()[0]
            
            # Get active users (logged in last 30 days)
            cursor.execute("""
                SELECT COUNT(*) FROM users 
                WHERE last_login > datetime('now', '-30 days')
            """)
            active_users = cursor.fetchone()[0]
            
            # Get users by role
            cursor.execute("SELECT role, COUNT(*) FROM users GROUP BY role")
            users_by_role = dict(cursor.fetchall())
            
            # Get total sessions
            cursor.execute("SELECT COUNT(*) FROM sessions")
            total_sessions = cursor.fetchone()[0]
            
            # Get active sessions
            cursor.execute("""
                SELECT COUNT(*) FROM sessions 
                WHERE expires_at IS NULL OR expires_at > datetime('now')
            """)
            active_sessions = cursor.fetchone()[0]
            
            conn.close()
            
            return {
                "success": True,
                "stats": {
                    "total_users": total_users,
                    "active_users": active_users,
                    "users_by_role": users_by_role,
                    "total_sessions": total_sessions,
                    "active_sessions": active_sessions
                }
            }
            
        except Exception as e:
            return {"success": False, "error": str(e)}
    
    def cleanup_expired_sessions(self) -> Dict[str, Any]:
        """Clean up expired sessions"""
        try:
            conn = sqlite3.connect(self.db_path)
            cursor = conn.cursor()
            
            # Delete expired sessions
            cursor.execute("""
                DELETE FROM sessions 
                WHERE expires_at IS NOT NULL AND expires_at < datetime('now')
            """)
            
            deleted_count = cursor.rowcount
            conn.commit()
            conn.close()
            
            return {
                "success": True,
                "deleted_sessions": deleted_count,
                "message": f"Cleaned up {deleted_count} expired sessions"
            }
            
        except Exception as e:
            return {"success": False, "error": str(e)}
    
    # Private helper methods
    
    def _init_database(self):
        """Initialize database tables"""
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        
        # Create users table
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                username TEXT UNIQUE NOT NULL,
                email TEXT UNIQUE NOT NULL,
                password_hash TEXT NOT NULL,
                role TEXT DEFAULT 'user',
                created_at TEXT NOT NULL,
                updated_at TEXT,
                last_login TEXT,
                is_active BOOLEAN DEFAULT 1,
                additional_data TEXT
            )
        """)
        
        # Create sessions table
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS sessions (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                session_id TEXT UNIQUE NOT NULL,
                user_id INTEGER NOT NULL,
                token TEXT NOT NULL,
                created_at TEXT NOT NULL,
                last_activity TEXT NOT NULL,
                expires_at TEXT,
                ip_address TEXT,
                user_agent TEXT,
                FOREIGN KEY (user_id) REFERENCES users (id)
            )
        """)
        
        conn.commit()
        conn.close()
    
    def _user_exists(self, username: str = None, email: str = None) -> bool:
        """Check if user exists"""
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        
        if username and email:
            cursor.execute("SELECT COUNT(*) FROM users WHERE username = ? OR email = ?", (username, email))
        elif username:
            cursor.execute("SELECT COUNT(*) FROM users WHERE username = ?", (username,))
        elif email:
            cursor.execute("SELECT COUNT(*) FROM users WHERE email = ?", (email,))
        else:
            return False
        
        count = cursor.fetchone()[0]
        conn.close()
        
        return count > 0
    
    def _find_user(self, username: str = None, email: str = None, user_id: int = None):
        """Find user by username, email, or ID"""
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        
        if user_id:
            cursor.execute("SELECT * FROM users WHERE id = ?", (user_id,))
        elif username:
            cursor.execute("SELECT * FROM users WHERE username = ?", (username,))
        elif email:
            cursor.execute("SELECT * FROM users WHERE email = ?", (email,))
        else:
            return None
        
        row = cursor.fetchone()
        conn.close()
        
        if row:
            columns = [description[0] for description in cursor.description]
            return dict(zip(columns, row))
        
        return None
    
    def _save_user(self, user_data: Dict[str, Any]) -> int:
        """Save user to database"""
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        
        cursor.execute("""
            INSERT INTO users (username, email, password_hash, role, created_at, additional_data)
            VALUES (?, ?, ?, ?, ?, ?)
        """, (
            user_data["username"],
            user_data["email"],
            user_data["password_hash"],
            user_data["role"],
            user_data["created_at"],
            user_data["additional_data"]
        ))
        
        user_id = cursor.lastrowid
        conn.commit()
        conn.close()
        
        return user_id
    
    def _update_user(self, user_id: int, update_data: Dict[str, Any]):
        """Update user in database"""
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        
        set_clause = ", ".join([f"{key} = ?" for key in update_data.keys()])
        values = list(update_data.values()) + [user_id]
        
        cursor.execute(f"UPDATE users SET {set_clause} WHERE id = ?", values)
        conn.commit()
        conn.close()
    
    def _update_last_login(self, user_id: int):
        """Update user's last login time"""
        self._update_user(user_id, {"last_login": datetime.now().isoformat()})
    
    def _save_session(self, session_data: Dict[str, Any]):
        """Save session to database"""
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        
        cursor.execute("""
            INSERT INTO sessions (session_id, user_id, token, created_at, last_activity, expires_at, ip_address, user_agent)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        """, (
            session_data["session_id"],
            session_data["user_id"],
            session_data["token"],
            session_data["created_at"],
            session_data["last_activity"],
            session_data["expires_at"],
            session_data["ip_address"],
            session_data["user_agent"]
        ))
        
        conn.commit()
        conn.close()
    
    def _get_session_by_token(self, token: str):
        """Get session by token"""
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        
        cursor.execute("SELECT * FROM sessions WHERE token = ?", (token,))
        row = cursor.fetchone()
        conn.close()
        
        if row:
            columns = [description[0] for description in cursor.description]
            return dict(zip(columns, row))
        
        return None
    
    def _get_sessions(self, user_id: int = None):
        """Get sessions for user or all sessions"""
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        
        if user_id:
            cursor.execute("SELECT * FROM sessions WHERE user_id = ?", (user_id,))
        else:
            cursor.execute("SELECT * FROM sessions")
        
        rows = cursor.fetchall()
        conn.close()
        
        if rows:
            columns = [description[0] for description in cursor.description]
            return [dict(zip(columns, row)) for row in rows]
        
        return []
    
    def _update_session_activity(self, session_id: str):
        """Update session last activity"""
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        
        cursor.execute("""
            UPDATE sessions SET last_activity = ? WHERE session_id = ?
        """, (datetime.now().isoformat(), session_id))
        
        conn.commit()
        conn.close()
    
    def _delete_session(self, session_id: str):
        """Delete session"""
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        
        cursor.execute("DELETE FROM sessions WHERE session_id = ?", (session_id,))
        conn.commit()
        conn.close()
    
    def _validate_password(self, password: str) -> Dict[str, Any]:
        """Validate password against policy"""
        if self.password_policy == "none":
            return {"valid": True}
        
        if self.password_policy == "basic":
            if len(password) < 6:
                return {"valid": False, "error": "Password must be at least 6 characters"}
        
        elif self.password_policy == "strong":
            if len(password) < 8:
                return {"valid": False, "error": "Password must be at least 8 characters"}
            if not any(c.isupper() for c in password):
                return {"valid": False, "error": "Password must contain uppercase letter"}
            if not any(c.islower() for c in password):
                return {"valid": False, "error": "Password must contain lowercase letter"}
            if not any(c.isdigit() for c in password):
                return {"valid": False, "error": "Password must contain digit"}
            if not any(c in "!@#$%^&*()_+-=[]{}|;:,.<>?" for c in password):
                return {"valid": False, "error": "Password must contain special character"}
        
        # Flexible policy - no restrictions
        return {"valid": True}
