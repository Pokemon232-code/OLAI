#!/usr/bin/env python3
"""
REST API Manager - Comprehensive API Endpoints
Manages all RESTful API endpoints for OLAI modules
"""

from fastapi import FastAPI, HTTPException, Depends, UploadFile, File, Form, WebSocket, WebSocketDisconnect
from fastapi.middleware.cors import CORSMiddleware
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from fastapi.responses import JSONResponse, FileResponse
import uvicorn
import json
import os
import asyncio
from typing import Dict, List, Any, Optional
from datetime import datetime
import logging
import hashlib
import jwt
from pydantic import BaseModel

# Import OLAI modules
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

try:
    from database.database_manager import DatabaseManager
    from ai.ocr_processor import OCRProcessor
    from ai.speech_to_text import SpeechToTextProcessor
    from ai.text_processor import TextProcessorNode
    from hardware.camera_controller import CameraController
    from hardware.microphone_controller import MicrophoneController
    from microservices.auth_service import AuthService
    from microservices.model_discovery import ModelDiscovery
    from microservices.model_orchestrator import ModelOrchestrator
except ImportError as e:
    print(f"Warning: Some modules not available: {e}")

logger = logging.getLogger(__name__)

# Pydantic models for API requests/responses
class UserCreate(BaseModel):
    username: str
    email: str
    password: str

class UserLogin(BaseModel):
    username: str
    password: str

class ProjectCreate(BaseModel):
    name: str
    description: str
    project_type: str
    config: Dict[str, Any] = {}

class WorkflowCreate(BaseModel):
    project_id: int
    name: str
    config: Dict[str, Any]

class TextProcessRequest(BaseModel):
    text: str
    processor_type: str = "gemini"
    task: str = "analyze"
    language: str = "en"

class OCRRequest(BaseModel):
    image_path: str
    engine: str = "auto"
    languages: List[str] = ["en"]

class STTRequest(BaseModel):
    audio_path: str
    engine: str = "auto"
    language: str = "en"

class CameraConfig(BaseModel):
    device_id: int = 0
    resolution: str = "auto"
    fps: int = 30

class MicrophoneConfig(BaseModel):
    device_id: int = 0
    sample_rate: int = 16000
    channels: int = 1

class RESTAPIManager:
    """Comprehensive REST API manager for OLAI modules"""
    
    def __init__(self):
        self.app = FastAPI(
            title="OLAI REST API",
            description="Comprehensive API for OLAI modules",
            version="1.0.0"
        )
        
        # Initialize modules
        self.db_manager = DatabaseManager()
        self.ocr_processor = OCRProcessor()
        self.stt_processor = SpeechToTextProcessor()
        self.camera_controller = CameraController()
        self.microphone_controller = MicrophoneController()
        self.auth_service = AuthService()
        self.model_discovery = ModelDiscovery()
        self.model_orchestrator = ModelOrchestrator()
        
        # WebSocket connections
        self.active_connections: List[WebSocket] = []
        
        # Security
        self.security = HTTPBearer()
        
        # Setup middleware and routes
        self._setup_middleware()
        self._setup_routes()
    
    def _setup_middleware(self):
        """Setup CORS and other middleware"""
        self.app.add_middleware(
            CORSMiddleware,
            allow_origins=["*"],
            allow_credentials=True,
            allow_methods=["*"],
            allow_headers=["*"],
        )
    
    def _setup_routes(self):
        """Setup all API routes"""
        
        # Health and status endpoints
        @self.app.get("/health")
        async def health_check():
            return {"status": "healthy", "timestamp": datetime.now().isoformat()}
        
        @self.app.get("/status")
        async def get_status():
            return {
                "status": "running",
                "modules": {
                    "database": "available",
                    "ocr": "available",
                    "stt": "available",
                    "camera": "available",
                    "microphone": "available",
                    "auth": "available"
                },
                "timestamp": datetime.now().isoformat()
            }
        
        # Authentication endpoints
        @self.app.post("/auth/register")
        async def register_user(user_data: UserCreate):
            try:
                result = self.auth_service.register_user(
                    user_data.username,
                    user_data.email,
                    user_data.password
                )
                if result["status"] == "success":
                    return JSONResponse(content=result, status_code=201)
                else:
                    raise HTTPException(status_code=400, detail=result["error"])
            except Exception as e:
                raise HTTPException(status_code=500, detail=str(e))
        
        @self.app.post("/auth/login")
        async def login_user(user_data: UserLogin):
            try:
                result = self.auth_service.authenticate(user_data.username, user_data.password)
                if result["status"] == "success":
                    return JSONResponse(content=result)
                else:
                    raise HTTPException(status_code=401, detail=result["error"])
            except Exception as e:
                raise HTTPException(status_code=500, detail=str(e))
        
        # User management endpoints
        @self.app.get("/users/{user_id}")
        async def get_user(user_id: int, credentials: HTTPAuthorizationCredentials = Depends(self.security)):
            try:
                result = self.db_manager.get_user(user_id=user_id)
                if result["status"] == "success":
                    return JSONResponse(content=result)
                else:
                    raise HTTPException(status_code=404, detail=result["error"])
            except Exception as e:
                raise HTTPException(status_code=500, detail=str(e))
        
        # Project management endpoints
        @self.app.post("/projects")
        async def create_project(project_data: ProjectCreate, credentials: HTTPAuthorizationCredentials = Depends(self.security)):
            try:
                result = self.db_manager.create_project(
                    project_data.name,
                    project_data.description,
                    project_data.project_type,
                    project_data.config
                )
                if result["status"] == "success":
                    return JSONResponse(content=result, status_code=201)
                else:
                    raise HTTPException(status_code=400, detail=result["error"])
            except Exception as e:
                raise HTTPException(status_code=500, detail=str(e))
        
        @self.app.get("/projects")
        async def get_projects(credentials: HTTPAuthorizationCredentials = Depends(self.security)):
            try:
                result = self.db_manager.get_projects()
                if result["status"] == "success":
                    return JSONResponse(content=result)
                else:
                    raise HTTPException(status_code=500, detail=result["error"])
            except Exception as e:
                raise HTTPException(status_code=500, detail=str(e))
        
        @self.app.get("/projects/{project_id}")
        async def get_project(project_id: int, credentials: HTTPAuthorizationCredentials = Depends(self.security)):
            try:
                # This would need to be implemented in database_manager
                return {"message": f"Project {project_id} details", "status": "success"}
            except Exception as e:
                raise HTTPException(status_code=500, detail=str(e))
        
        # Workflow management endpoints
        @self.app.post("/workflows")
        async def create_workflow(workflow_data: WorkflowCreate, credentials: HTTPAuthorizationCredentials = Depends(self.security)):
            try:
                result = self.db_manager.create_workflow(
                    workflow_data.project_id,
                    workflow_data.name,
                    workflow_data.config
                )
                if result["status"] == "success":
                    return JSONResponse(content=result, status_code=201)
                else:
                    raise HTTPException(status_code=400, detail=result["error"])
            except Exception as e:
                raise HTTPException(status_code=500, detail=str(e))
        
        # AI processing endpoints
        @self.app.post("/ai/text/process")
        async def process_text(request: TextProcessRequest, credentials: HTTPAuthorizationCredentials = Depends(self.security)):
            try:
                config = {
                    "processor_type": request.processor_type,
                    "task": request.task,
                    "language": request.language
                }
                text_processor = TextProcessorNode(config)
                result = text_processor.process_text({"text": request.text})
                return JSONResponse(content=result)
            except Exception as e:
                raise HTTPException(status_code=500, detail=str(e))
        
        @self.app.post("/ai/ocr/extract")
        async def extract_text_ocr(request: OCRRequest, credentials: HTTPAuthorizationCredentials = Depends(self.security)):
            try:
                result = self.ocr_processor.extract_text_from_file(
                    request.image_path,
                    request.engine,
                    request.languages
                )
                return JSONResponse(content=result)
            except Exception as e:
                raise HTTPException(status_code=500, detail=str(e))
        
        @self.app.post("/ai/stt/transcribe")
        async def transcribe_audio(request: STTRequest, credentials: HTTPAuthorizationCredentials = Depends(self.security)):
            try:
                result = self.stt_processor.transcribe_from_file(
                    request.audio_path,
                    request.engine,
                    request.language
                )
                return JSONResponse(content=result)
            except Exception as e:
                raise HTTPException(status_code=500, detail=str(e))
        
        # File upload endpoints
        @self.app.post("/files/upload")
        async def upload_file(file: UploadFile = File(...), credentials: HTTPAuthorizationCredentials = Depends(self.security)):
            try:
                # Create uploads directory if it doesn't exist
                upload_dir = "uploads"
                os.makedirs(upload_dir, exist_ok=True)
                
                # Generate unique filename
                file_hash = hashlib.md5(file.filename.encode()).hexdigest()
                file_extension = os.path.splitext(file.filename)[1]
                unique_filename = f"{file_hash}_{datetime.now().strftime('%Y%m%d_%H%M%S')}{file_extension}"
                file_path = os.path.join(upload_dir, unique_filename)
                
                # Save file
                with open(file_path, "wb") as buffer:
                    content = await file.read()
                    buffer.write(content)
                
                return JSONResponse(content={
                    "status": "success",
                    "filename": unique_filename,
                    "original_filename": file.filename,
                    "file_path": file_path,
                    "file_size": len(content),
                    "upload_time": datetime.now().isoformat()
                })
            except Exception as e:
                raise HTTPException(status_code=500, detail=str(e))
        
        @self.app.get("/files/{filename}")
        async def download_file(filename: str, credentials: HTTPAuthorizationCredentials = Depends(self.security)):
            try:
                file_path = os.path.join("uploads", filename)
                if os.path.exists(file_path):
                    return FileResponse(file_path)
                else:
                    raise HTTPException(status_code=404, detail="File not found")
            except Exception as e:
                raise HTTPException(status_code=500, detail=str(e))
        
        # Hardware control endpoints
        @self.app.post("/hardware/camera/start")
        async def start_camera(config: CameraConfig, credentials: HTTPAuthorizationCredentials = Depends(self.security)):
            try:
                camera_config = {
                    "device_id": config.device_id,
                    "resolution": config.resolution,
                    "fps": config.fps
                }
                result = self.camera_controller.initialize(camera_config)
                if result:
                    return JSONResponse(content={"status": "success", "message": "Camera started"})
                else:
                    raise HTTPException(status_code=500, detail="Failed to start camera")
            except Exception as e:
                raise HTTPException(status_code=500, detail=str(e))
        
        @self.app.post("/hardware/camera/capture")
        async def capture_image(credentials: HTTPAuthorizationCredentials = Depends(self.security)):
            try:
                result = self.camera_controller.capture_frame()
                if result["status"] == "success":
                    return JSONResponse(content=result)
                else:
                    raise HTTPException(status_code=500, detail=result["error"])
            except Exception as e:
                raise HTTPException(status_code=500, detail=str(e))
        
        @self.app.post("/hardware/microphone/start")
        async def start_microphone(config: MicrophoneConfig, credentials: HTTPAuthorizationCredentials = Depends(self.security)):
            try:
                mic_config = {
                    "device_id": config.device_id,
                    "sample_rate": config.sample_rate,
                    "channels": config.channels
                }
                result = self.microphone_controller.initialize(mic_config)
                if result:
                    return JSONResponse(content={"status": "success", "message": "Microphone started"})
                else:
                    raise HTTPException(status_code=500, detail="Failed to start microphone")
            except Exception as e:
                raise HTTPException(status_code=500, detail=str(e))
        
        # Model management endpoints
        @self.app.get("/models/discover")
        async def discover_models(prompt: str, credentials: HTTPAuthorizationCredentials = Depends(self.security)):
            try:
                result = self.model_discovery.discover_models_for_prompt(prompt)
                if result["status"] == "success":
                    return JSONResponse(content=result)
                else:
                    raise HTTPException(status_code=500, detail=result["error"])
            except Exception as e:
                raise HTTPException(status_code=500, detail=str(e))
        
        @self.app.post("/models/orchestrate")
        async def orchestrate_models(models: List[str], credentials: HTTPAuthorizationCredentials = Depends(self.security)):
            try:
                result = self.model_orchestrator.create_model_chain(models)
                if result["status"] == "success":
                    return JSONResponse(content=result)
                else:
                    raise HTTPException(status_code=500, detail=result["error"])
            except Exception as e:
                raise HTTPException(status_code=500, detail=str(e))
        
        # WebSocket endpoint for real-time communication
        @self.app.websocket("/ws")
        async def websocket_endpoint(websocket: WebSocket):
            await websocket.accept()
            self.active_connections.append(websocket)
            try:
                while True:
                    data = await websocket.receive_text()
                    # Echo back the message
                    await websocket.send_text(f"Echo: {data}")
            except WebSocketDisconnect:
                self.active_connections.remove(websocket)
        
        # Batch processing endpoints
        @self.app.post("/ai/batch/ocr")
        async def batch_ocr(image_paths: List[str], credentials: HTTPAuthorizationCredentials = Depends(self.security)):
            try:
                result = self.ocr_processor.batch_extract_text(image_paths)
                return JSONResponse(content=result)
            except Exception as e:
                raise HTTPException(status_code=500, detail=str(e))
        
        @self.app.post("/ai/batch/stt")
        async def batch_stt(audio_paths: List[str], credentials: HTTPAuthorizationCredentials = Depends(self.security)):
            try:
                result = self.stt_processor.batch_transcribe(audio_paths)
                return JSONResponse(content=result)
            except Exception as e:
                raise HTTPException(status_code=500, detail=str(e))
    
    async def broadcast_message(self, message: str):
        """Broadcast message to all WebSocket connections"""
        for connection in self.active_connections:
            try:
                await connection.send_text(message)
            except:
                pass
    
    def start_server(self, host: str = "0.0.0.0", port: int = 8000):
        """Start the API server"""
        uvicorn.run(self.app, host=host, port=port)

# Factory function
def create_rest_api_manager() -> RESTAPIManager:
    """Create a REST API manager instance"""
    return RESTAPIManager()

# Example usage
if __name__ == "__main__":
    api_manager = create_rest_api_manager()
    api_manager.start_server()
