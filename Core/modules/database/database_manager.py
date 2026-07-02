#!/usr/bin/env python3
"""
Database Manager - Advanced Database Operations
Manages multiple database types with advanced features
"""

import os
import json
import sqlite3
from typing import Dict, List, Any, Optional, Union
from datetime import datetime
import logging
import threading

try:
    import psycopg2
    import psycopg2.extras
    POSTGRES_AVAILABLE = True
except ImportError:
    POSTGRES_AVAILABLE = False

try:
    import pymongo
    MONGODB_AVAILABLE = True
except ImportError:
    MONGODB_AVAILABLE = False

try:
    import redis
    REDIS_AVAILABLE = True
except ImportError:
    REDIS_AVAILABLE = False

logger = logging.getLogger(__name__)

class DatabaseManager:
    """
    Advanced database manager with support for multiple database types
    - SQLite (local development)
    - PostgreSQL (production)
    - MongoDB (document storage)
    - Redis (caching and sessions)
    - Connection pooling and management
    - Migration support
    - Backup and restore
    """
    
    def __init__(self):
        self.connections = {}
        self.connection_pools = {}
        self.db_configs = {}
        self.lock = threading.Lock()
        self.migration_history = []
        
        # Database type support
        self.supported_databases = {
            'sqlite': True,
            'postgresql': POSTGRES_AVAILABLE,
            'mongodb': MONGODB_AVAILABLE,
            'redis': REDIS_AVAILABLE
        }
    
    def initialize(self, config: Dict[str, Any]):
        """Initialize database connections based on configuration"""
        try:
            self.db_configs = config
            
            # Initialize SQLite (always available)
            if config.get('sqlite', {}).get('enabled', True):
                self._initialize_sqlite(config.get('sqlite', {}))
            
            # Initialize PostgreSQL
            if config.get('postgresql', {}).get('enabled', False) and POSTGRES_AVAILABLE:
                self._initialize_postgresql(config.get('postgresql', {}))
            
            # Initialize MongoDB
            if config.get('mongodb', {}).get('enabled', False) and MONGODB_AVAILABLE:
                self._initialize_mongodb(config.get('mongodb', {}))
            
            # Initialize Redis
            if config.get('redis', {}).get('enabled', False) and REDIS_AVAILABLE:
                self._initialize_redis(config.get('redis', {}))
            
            logger.info("Database manager initialized successfully")
            return True
            
        except Exception as e:
            logger.error(f"Database initialization failed: {e}")
            return False
    
    def _initialize_sqlite(self, config: Dict[str, Any]):
        """Initialize SQLite connection"""
        db_path = config.get('path', 'olai_database.db')
        
        # Ensure directory exists
        os.makedirs(os.path.dirname(db_path), exist_ok=True)
        
        # Create connection
        conn = sqlite3.connect(db_path, check_same_thread=False)
        conn.row_factory = sqlite3.Row  # Enable column access by name
        
        self.connections['sqlite'] = conn
        
        # Create basic tables
        self._create_sqlite_tables()
    
    def _initialize_postgresql(self, config: Dict[str, Any]):
        """Initialize PostgreSQL connection"""
        try:
            conn_params = {
                'host': config.get('host', 'localhost'),
                'port': config.get('port', 5432),
                'database': config.get('database', 'olai_db'),
                'user': config.get('user', 'postgres'),
                'password': config.get('password', '')
            }
            
            conn = psycopg2.connect(**conn_params)
            self.connections['postgresql'] = conn
            
            # Create basic tables
            self._create_postgresql_tables()
            
        except Exception as e:
            logger.error(f"PostgreSQL initialization failed: {e}")
    
    def _initialize_mongodb(self, config: Dict[str, Any]):
        """Initialize MongoDB connection"""
        try:
            connection_string = config.get('connection_string', 'mongodb://localhost:27017/')
            database_name = config.get('database', 'olai_db')
            
            client = pymongo.MongoClient(connection_string)
            db = client[database_name]
            
            self.connections['mongodb'] = db
            
        except Exception as e:
            logger.error(f"MongoDB initialization failed: {e}")
    
    def _initialize_redis(self, config: Dict[str, Any]):
        """Initialize Redis connection"""
        try:
            host = config.get('host', 'localhost')
            port = config.get('port', 6379)
            db = config.get('db', 0)
            
            r = redis.Redis(host=host, port=port, db=db, decode_responses=True)
            
            # Test connection
            r.ping()
            
            self.connections['redis'] = r
            
        except Exception as e:
            logger.error(f"Redis initialization failed: {e}")
    
    def _create_sqlite_tables(self):
        """Create basic SQLite tables"""
        cursor = self.connections['sqlite'].cursor()
        
        # Users table
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                username TEXT UNIQUE NOT NULL,
                email TEXT UNIQUE NOT NULL,
                password_hash TEXT NOT NULL,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        ''')
        
        # Projects table
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS projects (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                description TEXT,
                project_type TEXT,
                config TEXT,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        ''')
        
        # Workflows table
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS workflows (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                project_id INTEGER,
                name TEXT NOT NULL,
                config TEXT,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                FOREIGN KEY (project_id) REFERENCES projects (id)
            )
        ''')
        
        # Executions table
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS executions (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                workflow_id INTEGER,
                status TEXT,
                input_data TEXT,
                output_data TEXT,
                started_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                finished_at TIMESTAMP,
                FOREIGN KEY (workflow_id) REFERENCES workflows (id)
            )
        ''')
        
        self.connections['sqlite'].commit()
    
    def _create_postgresql_tables(self):
        """Create basic PostgreSQL tables"""
        cursor = self.connections['postgresql'].cursor()
        
        # Users table
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS users (
                id SERIAL PRIMARY KEY,
                username VARCHAR(255) UNIQUE NOT NULL,
                email VARCHAR(255) UNIQUE NOT NULL,
                password_hash TEXT NOT NULL,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        ''')
        
        # Projects table
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS projects (
                id SERIAL PRIMARY KEY,
                name VARCHAR(255) NOT NULL,
                description TEXT,
                project_type VARCHAR(100),
                config JSONB,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        ''')
        
        # Workflows table
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS workflows (
                id SERIAL PRIMARY KEY,
                project_id INTEGER,
                name VARCHAR(255) NOT NULL,
                config JSONB,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                FOREIGN KEY (project_id) REFERENCES projects (id)
            )
        ''')
        
        # Executions table
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS executions (
                id SERIAL PRIMARY KEY,
                workflow_id INTEGER,
                status VARCHAR(50),
                input_data JSONB,
                output_data JSONB,
                started_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                finished_at TIMESTAMP,
                FOREIGN KEY (workflow_id) REFERENCES workflows (id)
            )
        ''')
        
        self.connections['postgresql'].commit()
    
    def create_user(self, username: str, email: str, password_hash: str) -> Dict[str, Any]:
        """Create a new user"""
        try:
            with self.lock:
                if 'sqlite' in self.connections:
                    cursor = self.connections['sqlite'].cursor()
                    cursor.execute('''
                        INSERT INTO users (username, email, password_hash)
                        VALUES (?, ?, ?)
                    ''', (username, email, password_hash))
                    user_id = cursor.lastrowid
                    self.connections['sqlite'].commit()
                
                elif 'postgresql' in self.connections:
                    cursor = self.connections['postgresql'].cursor()
                    cursor.execute('''
                        INSERT INTO users (username, email, password_hash)
                        VALUES (%s, %s, %s) RETURNING id
                    ''', (username, email, password_hash))
                    user_id = cursor.fetchone()[0]
                    self.connections['postgresql'].commit()
                
                else:
                    return {"status": "error", "error": "No database connection available"}
                
                return {
                    "status": "success",
                    "user_id": user_id,
                    "username": username,
                    "email": email,
                    "created_at": datetime.now().isoformat()
                }
                
        except Exception as e:
            logger.error(f"User creation failed: {e}")
            return {"status": "error", "error": str(e)}
    
    def create_project(self, name: str, description: str = "", project_type: str = "web_app", config: Dict[str, Any] = None) -> Dict[str, Any]:
        """Create a new project"""
        try:
            with self.lock:
                config_json = json.dumps(config or {})
                
                if 'sqlite' in self.connections:
                    cursor = self.connections['sqlite'].cursor()
                    cursor.execute('''
                        INSERT INTO projects (name, description, project_type, config)
                        VALUES (?, ?, ?, ?)
                    ''', (name, description, project_type, config_json))
                    project_id = cursor.lastrowid
                    self.connections['sqlite'].commit()
                
                elif 'postgresql' in self.connections:
                    cursor = self.connections['postgresql'].cursor()
                    cursor.execute('''
                        INSERT INTO projects (name, description, project_type, config)
                        VALUES (%s, %s, %s, %s) RETURNING id
                    ''', (name, description, project_type, config_json))
                    project_id = cursor.fetchone()[0]
                    self.connections['postgresql'].commit()
                
                else:
                    return {"status": "error", "error": "No database connection available"}
                
                return {
                    "status": "success",
                    "project_id": project_id,
                    "name": name,
                    "description": description,
                    "project_type": project_type,
                    "created_at": datetime.now().isoformat()
                }
                
        except Exception as e:
            logger.error(f"Project creation failed: {e}")
            return {"status": "error", "error": str(e)}
    
    def create_workflow(self, project_id: int, name: str, config: Dict[str, Any]) -> Dict[str, Any]:
        """Create a new workflow"""
        try:
            with self.lock:
                config_json = json.dumps(config)
                
                if 'sqlite' in self.connections:
                    cursor = self.connections['sqlite'].cursor()
                    cursor.execute('''
                        INSERT INTO workflows (project_id, name, config)
                        VALUES (?, ?, ?)
                    ''', (project_id, name, config_json))
                    workflow_id = cursor.lastrowid
                    self.connections['sqlite'].commit()
                
                elif 'postgresql' in self.connections:
                    cursor = self.connections['postgresql'].cursor()
                    cursor.execute('''
                        INSERT INTO workflows (project_id, name, config)
                        VALUES (%s, %s, %s) RETURNING id
                    ''', (project_id, name, config_json))
                    workflow_id = cursor.fetchone()[0]
                    self.connections['postgresql'].commit()
                
                else:
                    return {"status": "error", "error": "No database connection available"}
                
                return {
                    "status": "success",
                    "workflow_id": workflow_id,
                    "project_id": project_id,
                    "name": name,
                    "created_at": datetime.now().isoformat()
                }
                
        except Exception as e:
            logger.error(f"Workflow creation failed: {e}")
            return {"status": "error", "error": str(e)}
    
    def get_user(self, user_id: int = None, username: str = None, email: str = None) -> Dict[str, Any]:
        """Get user by ID, username, or email"""
        try:
            with self.lock:
                if 'sqlite' in self.connections:
                    cursor = self.connections['sqlite'].cursor()
                    
                    if user_id:
                        cursor.execute('SELECT * FROM users WHERE id = ?', (user_id,))
                    elif username:
                        cursor.execute('SELECT * FROM users WHERE username = ?', (username,))
                    elif email:
                        cursor.execute('SELECT * FROM users WHERE email = ?', (email,))
                    else:
                        return {"status": "error", "error": "No identifier provided"}
                    
                    user = cursor.fetchone()
                
                elif 'postgresql' in self.connections:
                    cursor = self.connections['postgresql'].cursor(cursor_factory=psycopg2.extras.RealDictCursor)
                    
                    if user_id:
                        cursor.execute('SELECT * FROM users WHERE id = %s', (user_id,))
                    elif username:
                        cursor.execute('SELECT * FROM users WHERE username = %s', (username,))
                    elif email:
                        cursor.execute('SELECT * FROM users WHERE email = %s', (email,))
                    else:
                        return {"status": "error", "error": "No identifier provided"}
                    
                    user = cursor.fetchone()
                
                else:
                    return {"status": "error", "error": "No database connection available"}
                
                if user:
                    return {
                        "status": "success",
                        "user": dict(user),
                        "timestamp": datetime.now().isoformat()
                    }
                else:
                    return {"status": "error", "error": "User not found"}
                
        except Exception as e:
            logger.error(f"User retrieval failed: {e}")
            return {"status": "error", "error": str(e)}
    
    def get_projects(self, user_id: int = None) -> Dict[str, Any]:
        """Get all projects or projects for a specific user"""
        try:
            with self.lock:
                if 'sqlite' in self.connections:
                    cursor = self.connections['sqlite'].cursor()
                    if user_id:
                        cursor.execute('SELECT * FROM projects WHERE user_id = ? ORDER BY created_at DESC', (user_id,))
                    else:
                        cursor.execute('SELECT * FROM projects ORDER BY created_at DESC')
                    projects = cursor.fetchall()
                
                elif 'postgresql' in self.connections:
                    cursor = self.connections['postgresql'].cursor(cursor_factory=psycopg2.extras.RealDictCursor)
                    if user_id:
                        cursor.execute('SELECT * FROM projects WHERE user_id = %s ORDER BY created_at DESC', (user_id,))
                    else:
                        cursor.execute('SELECT * FROM projects ORDER BY created_at DESC')
                    projects = cursor.fetchall()
                
                else:
                    return {"status": "error", "error": "No database connection available"}
                
                projects_list = [dict(project) for project in projects]
                
                return {
                    "status": "success",
                    "projects": projects_list,
                    "count": len(projects_list),
                    "timestamp": datetime.now().isoformat()
                }
                
        except Exception as e:
            logger.error(f"Projects retrieval failed: {e}")
            return {"status": "error", "error": str(e)}
    
    def cache_set(self, key: str, value: Any, expire: int = 3600) -> Dict[str, Any]:
        """Set cache value using Redis"""
        try:
            if 'redis' not in self.connections:
                return {"status": "error", "error": "Redis not available"}
            
            redis_client = self.connections['redis']
            redis_client.setex(key, expire, json.dumps(value))
            
            return {
                "status": "success",
                "key": key,
                "expire": expire,
                "timestamp": datetime.now().isoformat()
            }
            
        except Exception as e:
            logger.error(f"Cache set failed: {e}")
            return {"status": "error", "error": str(e)}
    
    def cache_get(self, key: str) -> Dict[str, Any]:
        """Get cache value using Redis"""
        try:
            if 'redis' not in self.connections:
                return {"status": "error", "error": "Redis not available"}
            
            redis_client = self.connections['redis']
            value = redis_client.get(key)
            
            if value:
                return {
                    "status": "success",
                    "key": key,
                    "value": json.loads(value),
                    "timestamp": datetime.now().isoformat()
                }
            else:
                return {"status": "error", "error": "Key not found"}
                
        except Exception as e:
            logger.error(f"Cache get failed: {e}")
            return {"status": "error", "error": str(e)}
    
    def close_connections(self):
        """Close all database connections"""
        try:
            for db_type, conn in self.connections.items():
                if hasattr(conn, 'close'):
                    conn.close()
                logger.info(f"Closed {db_type} connection")
            
            self.connections.clear()
            
        except Exception as e:
            logger.error(f"Error closing connections: {e}")

# Factory function for easy module usage
def create_database_manager() -> DatabaseManager:
    """Create a database manager instance"""
    return DatabaseManager()

# Example usage
if __name__ == "__main__":
    manager = create_database_manager()
    
    # Initialize with SQLite
    config = {
        'sqlite': {'enabled': True, 'path': 'test.db'},
        'redis': {'enabled': True}
    }
    
    manager.initialize(config)
    
    # Create a test project
    result = manager.create_project("Test Project", "A test project", "web_app")
    print(json.dumps(result, indent=2))
