#!/usr/bin/env python3
"""
WebSocket Manager - Real-time Communication
Manages WebSocket connections and real-time communication
"""

import asyncio
import json
import logging
from typing import Dict, List, Any, Optional, Callable
from datetime import datetime
import uuid
from fastapi import WebSocket, WebSocketDisconnect
from enum import Enum

logger = logging.getLogger(__name__)

class MessageType(Enum):
    """Message types for WebSocket communication"""
    SYSTEM = "system"
    USER = "user"
    AI_RESPONSE = "ai_response"
    WORKFLOW_UPDATE = "workflow_update"
    FILE_PROCESSING = "file_processing"
    HARDWARE_STATUS = "hardware_status"
    ERROR = "error"
    NOTIFICATION = "notification"

class WebSocketManager:
    """Advanced WebSocket manager for real-time communication"""
    
    def __init__(self):
        self.active_connections: Dict[str, WebSocket] = {}
        self.connection_metadata: Dict[str, Dict[str, Any]] = {}
        self.message_handlers: Dict[MessageType, List[Callable]] = {}
        self.rooms: Dict[str, List[str]] = {}
        self.broadcast_queue = asyncio.Queue()
        self.is_running = False
        
        # Initialize message handlers
        self._initialize_handlers()
    
    def _initialize_handlers(self):
        """Initialize default message handlers"""
        self.message_handlers = {
            MessageType.SYSTEM: [self._handle_system_message],
            MessageType.USER: [self._handle_user_message],
            MessageType.AI_RESPONSE: [self._handle_ai_response],
            MessageType.WORKFLOW_UPDATE: [self._handle_workflow_update],
            MessageType.FILE_PROCESSING: [self._handle_file_processing],
            MessageType.HARDWARE_STATUS: [self._handle_hardware_status],
            MessageType.ERROR: [self._handle_error_message],
            MessageType.NOTIFICATION: [self._handle_notification]
        }
    
    async def connect(self, websocket: WebSocket, client_id: str = None) -> str:
        """Accept a WebSocket connection"""
        await websocket.accept()
        
        if not client_id:
            client_id = str(uuid.uuid4())
        
        self.active_connections[client_id] = websocket
        self.connection_metadata[client_id] = {
            "connected_at": datetime.now().isoformat(),
            "last_activity": datetime.now().isoformat(),
            "room": None,
            "user_id": None,
            "project_id": None
        }
        
        # Send welcome message
        await self.send_message(client_id, {
            "type": MessageType.SYSTEM.value,
            "message": "Connected to OLAI WebSocket server",
            "client_id": client_id,
            "timestamp": datetime.now().isoformat()
        })
        
        logger.info(f"Client {client_id} connected")
        return client_id
    
    async def disconnect(self, client_id: str):
        """Disconnect a WebSocket connection"""
        if client_id in self.active_connections:
            # Remove from room if in one
            metadata = self.connection_metadata.get(client_id, {})
            room = metadata.get("room")
            if room and room in self.rooms:
                self.rooms[room].remove(client_id)
                if not self.rooms[room]:
                    del self.rooms[room]
            
            # Remove connection
            del self.active_connections[client_id]
            if client_id in self.connection_metadata:
                del self.connection_metadata[client_id]
            
            logger.info(f"Client {client_id} disconnected")
    
    async def send_message(self, client_id: str, message: Dict[str, Any]):
        """Send message to specific client"""
        if client_id in self.active_connections:
            try:
                websocket = self.active_connections[client_id]
                await websocket.send_text(json.dumps(message))
                
                # Update last activity
                if client_id in self.connection_metadata:
                    self.connection_metadata[client_id]["last_activity"] = datetime.now().isoformat()
                    
            except Exception as e:
                logger.error(f"Error sending message to {client_id}: {e}")
                await self.disconnect(client_id)
    
    async def broadcast_message(self, message: Dict[str, Any], room: str = None, exclude_client: str = None):
        """Broadcast message to all clients or specific room"""
        targets = []
        
        if room and room in self.rooms:
            targets = self.rooms[room]
        else:
            targets = list(self.active_connections.keys())
        
        if exclude_client and exclude_client in targets:
            targets.remove(exclude_client)
        
        for client_id in targets:
            await self.send_message(client_id, message)
    
    async def join_room(self, client_id: str, room: str):
        """Join a client to a room"""
        if client_id in self.active_connections:
            # Leave current room if in one
            metadata = self.connection_metadata.get(client_id, {})
            current_room = metadata.get("room")
            if current_room and current_room in self.rooms:
                self.rooms[current_room].remove(client_id)
            
            # Join new room
            if room not in self.rooms:
                self.rooms[room] = []
            self.rooms[room].append(client_id)
            
            # Update metadata
            self.connection_metadata[client_id]["room"] = room
            
            # Notify room members
            await self.broadcast_message({
                "type": MessageType.NOTIFICATION.value,
                "message": f"Client {client_id} joined room {room}",
                "room": room,
                "timestamp": datetime.now().isoformat()
            }, room=room, exclude_client=client_id)
            
            # Send confirmation to client
            await self.send_message(client_id, {
                "type": MessageType.SYSTEM.value,
                "message": f"Joined room {room}",
                "room": room,
                "timestamp": datetime.now().isoformat()
            })
    
    async def leave_room(self, client_id: str):
        """Leave current room"""
        if client_id in self.connection_metadata:
            metadata = self.connection_metadata[client_id]
            room = metadata.get("room")
            
            if room and room in self.rooms:
                self.rooms[room].remove(client_id)
                
                # Notify room members
                await self.broadcast_message({
                    "type": MessageType.NOTIFICATION.value,
                    "message": f"Client {client_id} left room {room}",
                    "room": room,
                    "timestamp": datetime.now().isoformat()
                }, room=room)
                
                # Update metadata
                self.connection_metadata[client_id]["room"] = None
    
    async def handle_message(self, client_id: str, message: str):
        """Handle incoming message from client"""
        try:
            data = json.loads(message)
            message_type = data.get("type", MessageType.USER.value)
            
            # Update last activity
            if client_id in self.connection_metadata:
                self.connection_metadata[client_id]["last_activity"] = datetime.now().isoformat()
            
            # Route to appropriate handler
            if message_type in [msg_type.value for msg_type in MessageType]:
                message_type_enum = MessageType(message_type)
                if message_type_enum in self.message_handlers:
                    for handler in self.message_handlers[message_type_enum]:
                        await handler(client_id, data)
                else:
                    await self._handle_unknown_message(client_id, data)
            else:
                await self._handle_unknown_message(client_id, data)
                
        except json.JSONDecodeError:
            await self.send_message(client_id, {
                "type": MessageType.ERROR.value,
                "message": "Invalid JSON format",
                "timestamp": datetime.now().isoformat()
            })
        except Exception as e:
            logger.error(f"Error handling message from {client_id}: {e}")
            await self.send_message(client_id, {
                "type": MessageType.ERROR.value,
                "message": f"Error processing message: {str(e)}",
                "timestamp": datetime.now().isoformat()
            })
    
    async def _handle_system_message(self, client_id: str, data: Dict[str, Any]):
        """Handle system messages"""
        message = data.get("message", "")
        logger.info(f"System message from {client_id}: {message}")
        
        # Echo back with timestamp
        await self.send_message(client_id, {
            "type": MessageType.SYSTEM.value,
            "message": f"System: {message}",
            "timestamp": datetime.now().isoformat()
        })
    
    async def _handle_user_message(self, client_id: str, data: Dict[str, Any]):
        """Handle user messages"""
        message = data.get("message", "")
        logger.info(f"User message from {client_id}: {message}")
        
        # Echo back with timestamp
        await self.send_message(client_id, {
            "type": MessageType.USER.value,
            "message": f"You: {message}",
            "timestamp": datetime.now().isoformat()
        })
    
    async def _handle_ai_response(self, client_id: str, data: Dict[str, Any]):
        """Handle AI response messages"""
        message = data.get("message", "")
        logger.info(f"AI response to {client_id}: {message}")
        
        # Broadcast to room if in one
        metadata = self.connection_metadata.get(client_id, {})
        room = metadata.get("room")
        if room:
            await self.broadcast_message({
                "type": MessageType.AI_RESPONSE.value,
                "message": message,
                "client_id": client_id,
                "timestamp": datetime.now().isoformat()
            }, room=room)
    
    async def _handle_workflow_update(self, client_id: str, data: Dict[str, Any]):
        """Handle workflow update messages"""
        workflow_data = data.get("workflow", {})
        logger.info(f"Workflow update from {client_id}")
        
        # Broadcast workflow update to room
        metadata = self.connection_metadata.get(client_id, {})
        room = metadata.get("room")
        if room:
            await self.broadcast_message({
                "type": MessageType.WORKFLOW_UPDATE.value,
                "workflow": workflow_data,
                "client_id": client_id,
                "timestamp": datetime.now().isoformat()
            }, room=room)
    
    async def _handle_file_processing(self, client_id: str, data: Dict[str, Any]):
        """Handle file processing messages"""
        file_info = data.get("file_info", {})
        status = data.get("status", "processing")
        
        # Broadcast file processing status to room
        metadata = self.connection_metadata.get(client_id, {})
        room = metadata.get("room")
        if room:
            await self.broadcast_message({
                "type": MessageType.FILE_PROCESSING.value,
                "file_info": file_info,
                "status": status,
                "client_id": client_id,
                "timestamp": datetime.now().isoformat()
            }, room=room)
    
    async def _handle_hardware_status(self, client_id: str, data: Dict[str, Any]):
        """Handle hardware status messages"""
        hardware_info = data.get("hardware_info", {})
        status = data.get("status", "unknown")
        
        # Broadcast hardware status to room
        metadata = self.connection_metadata.get(client_id, {})
        room = metadata.get("room")
        if room:
            await self.broadcast_message({
                "type": MessageType.HARDWARE_STATUS.value,
                "hardware_info": hardware_info,
                "status": status,
                "client_id": client_id,
                "timestamp": datetime.now().isoformat()
            }, room=room)
    
    async def _handle_error_message(self, client_id: str, data: Dict[str, Any]):
        """Handle error messages"""
        error_message = data.get("message", "Unknown error")
        logger.error(f"Error from {client_id}: {error_message}")
        
        # Send error acknowledgment
        await self.send_message(client_id, {
            "type": MessageType.ERROR.value,
            "message": "Error received and logged",
            "timestamp": datetime.now().isoformat()
        })
    
    async def _handle_notification(self, client_id: str, data: Dict[str, Any]):
        """Handle notification messages"""
        notification = data.get("message", "")
        logger.info(f"Notification from {client_id}: {notification}")
        
        # Broadcast notification to room
        metadata = self.connection_metadata.get(client_id, {})
        room = metadata.get("room")
        if room:
            await self.broadcast_message({
                "type": MessageType.NOTIFICATION.value,
                "message": notification,
                "client_id": client_id,
                "timestamp": datetime.now().isoformat()
            }, room=room)
    
    async def _handle_unknown_message(self, client_id: str, data: Dict[str, Any]):
        """Handle unknown message types"""
        logger.warning(f"Unknown message type from {client_id}: {data}")
        
        await self.send_message(client_id, {
            "type": MessageType.ERROR.value,
            "message": "Unknown message type",
            "timestamp": datetime.now().isoformat()
        })
    
    def add_message_handler(self, message_type: MessageType, handler: Callable):
        """Add custom message handler"""
        if message_type not in self.message_handlers:
            self.message_handlers[message_type] = []
        self.message_handlers[message_type].append(handler)
    
    def get_connection_stats(self) -> Dict[str, Any]:
        """Get connection statistics"""
        return {
            "active_connections": len(self.active_connections),
            "rooms": len(self.rooms),
            "connections_per_room": {room: len(clients) for room, clients in self.rooms.items()},
            "timestamp": datetime.now().isoformat()
        }
    
    def get_client_info(self, client_id: str) -> Dict[str, Any]:
        """Get client information"""
        if client_id in self.connection_metadata:
            return self.connection_metadata[client_id].copy()
        return {}

# Factory function
def create_websocket_manager() -> WebSocketManager:
    """Create a WebSocket manager instance"""
    return WebSocketManager()

# Example usage
if __name__ == "__main__":
    manager = create_websocket_manager()
    print("WebSocket Manager created successfully")
