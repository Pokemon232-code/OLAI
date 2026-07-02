#!/usr/bin/env python3
"""
File Manager - Advanced File Management System
Handles file upload, processing, storage, and management
"""

import os
import shutil
import hashlib
import mimetypes
import zipfile
import tarfile
from typing import Dict, List, Any, Optional, Union
from datetime import datetime
import logging
import json
import uuid
from pathlib import Path
import asyncio
import aiofiles

try:
    from PIL import Image
    PIL_AVAILABLE = True
except ImportError:
    PIL_AVAILABLE = False

try:
    import magic
    MAGIC_AVAILABLE = True
except ImportError:
    MAGIC_AVAILABLE = False

logger = logging.getLogger(__name__)

class FileType(Enum):
    """File type enumeration"""
    IMAGE = "image"
    VIDEO = "video"
    AUDIO = "audio"
    DOCUMENT = "document"
    ARCHIVE = "archive"
    CODE = "code"
    DATA = "data"
    UNKNOWN = "unknown"

class FileManager:
    """Advanced file management system for OLAI"""
    
    def __init__(self, base_storage_path: str = "storage"):
        self.base_storage_path = Path(base_storage_path)
        self.upload_path = self.base_storage_path / "uploads"
        self.processed_path = self.base_storage_path / "processed"
        self.temp_path = self.base_storage_path / "temp"
        self.backup_path = self.base_storage_path / "backup"
        
        # File type configurations
        self.file_type_configs = {
            FileType.IMAGE: {
                "extensions": [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".tiff", ".webp"],
                "max_size": 50 * 1024 * 1024,  # 50MB
                "processors": ["resize", "compress", "convert"]
            },
            FileType.VIDEO: {
                "extensions": [".mp4", ".avi", ".mov", ".wmv", ".flv", ".webm", ".mkv"],
                "max_size": 500 * 1024 * 1024,  # 500MB
                "processors": ["compress", "extract_audio", "thumbnail"]
            },
            FileType.AUDIO: {
                "extensions": [".mp3", ".wav", ".flac", ".aac", ".ogg", ".m4a"],
                "max_size": 100 * 1024 * 1024,  # 100MB
                "processors": ["convert", "extract_metadata"]
            },
            FileType.DOCUMENT: {
                "extensions": [".pdf", ".doc", ".docx", ".txt", ".rtf", ".odt"],
                "max_size": 25 * 1024 * 1024,  # 25MB
                "processors": ["extract_text", "convert"]
            },
            FileType.ARCHIVE: {
                "extensions": [".zip", ".rar", ".7z", ".tar", ".gz", ".bz2"],
                "max_size": 200 * 1024 * 1024,  # 200MB
                "processors": ["extract", "compress"]
            },
            FileType.CODE: {
                "extensions": [".py", ".js", ".html", ".css", ".json", ".xml", ".yaml"],
                "max_size": 10 * 1024 * 1024,  # 10MB
                "processors": ["syntax_check", "format"]
            }
        }
        
        # Initialize storage directories
        self._initialize_storage()
        
        # File metadata database
        self.metadata_db = {}
    
    def _initialize_storage(self):
        """Initialize storage directories"""
        for path in [self.upload_path, self.processed_path, self.temp_path, self.backup_path]:
            path.mkdir(parents=True, exist_ok=True)
        
        logger.info(f"Storage initialized at {self.base_storage_path}")
    
    def _detect_file_type(self, file_path: Union[str, Path]) -> FileType:
        """Detect file type based on extension and content"""
        file_path = Path(file_path)
        extension = file_path.suffix.lower()
        
        # Check by extension first
        for file_type, config in self.file_type_configs.items():
            if extension in config["extensions"]:
                return file_type
        
        # Check by MIME type if available
        if MAGIC_AVAILABLE:
            try:
                mime_type = magic.from_file(str(file_path), mime=True)
                if mime_type.startswith("image/"):
                    return FileType.IMAGE
                elif mime_type.startswith("video/"):
                    return FileType.VIDEO
                elif mime_type.startswith("audio/"):
                    return FileType.AUDIO
                elif mime_type in ["application/pdf", "application/msword", "text/plain"]:
                    return FileType.DOCUMENT
            except Exception as e:
                logger.warning(f"Could not detect MIME type: {e}")
        
        return FileType.UNKNOWN
    
    def _generate_file_hash(self, file_path: Union[str, Path]) -> str:
        """Generate SHA-256 hash of file"""
        hash_sha256 = hashlib.sha256()
        with open(file_path, "rb") as f:
            for chunk in iter(lambda: f.read(4096), b""):
                hash_sha256.update(chunk)
        return hash_sha256.hexdigest()
    
    def _generate_unique_filename(self, original_filename: str, file_hash: str) -> str:
        """Generate unique filename with hash"""
        file_path = Path(original_filename)
        extension = file_path.suffix
        name = file_path.stem
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        return f"{name}_{file_hash[:8]}_{timestamp}{extension}"
    
    async def upload_file(self, file_content: bytes, original_filename: str, 
                         metadata: Dict[str, Any] = None) -> Dict[str, Any]:
        """Upload and process a file"""
        try:
            # Generate file hash
            file_hash = hashlib.sha256(file_content).hexdigest()
            
            # Check if file already exists
            existing_file = self._find_file_by_hash(file_hash)
            if existing_file:
                return {
                    "status": "success",
                    "message": "File already exists",
                    "file_id": existing_file["file_id"],
                    "file_path": existing_file["file_path"],
                    "duplicate": True
                }
            
            # Generate unique filename
            unique_filename = self._generate_unique_filename(original_filename, file_hash)
            file_path = self.upload_path / unique_filename
            
            # Save file
            async with aiofiles.open(file_path, 'wb') as f:
                await f.write(file_content)
            
            # Detect file type
            file_type = self._detect_file_type(file_path)
            
            # Get file size
            file_size = len(file_content)
            
            # Check file size limits
            if file_type in self.file_type_configs:
                max_size = self.file_type_configs[file_type]["max_size"]
                if file_size > max_size:
                    os.remove(file_path)
                    return {
                        "status": "error",
                        "error": f"File size {file_size} exceeds maximum {max_size} for {file_type.value}"
                    }
            
            # Generate file ID
            file_id = str(uuid.uuid4())
            
            # Create file metadata
            file_metadata = {
                "file_id": file_id,
                "original_filename": original_filename,
                "unique_filename": unique_filename,
                "file_path": str(file_path),
                "file_type": file_type.value,
                "file_size": file_size,
                "file_hash": file_hash,
                "upload_time": datetime.now().isoformat(),
                "metadata": metadata or {},
                "processed": False
            }
            
            # Store metadata
            self.metadata_db[file_id] = file_metadata
            
            # Save metadata to file
            await self._save_metadata(file_id, file_metadata)
            
            # Process file based on type
            processing_result = await self._process_file(file_id, file_type)
            
            return {
                "status": "success",
                "file_id": file_id,
                "file_path": str(file_path),
                "file_type": file_type.value,
                "file_size": file_size,
                "processing_result": processing_result,
                "metadata": file_metadata
            }
            
        except Exception as e:
            logger.error(f"File upload failed: {e}")
            return {"status": "error", "error": str(e)}
    
    async def _process_file(self, file_id: str, file_type: FileType) -> Dict[str, Any]:
        """Process file based on type"""
        try:
            file_metadata = self.metadata_db.get(file_id)
            if not file_metadata:
                return {"status": "error", "error": "File metadata not found"}
            
            file_path = Path(file_metadata["file_path"])
            processing_result = {"status": "success", "operations": []}
            
            if file_type == FileType.IMAGE:
                result = await self._process_image(file_path)
                processing_result["operations"].append(result)
            elif file_type == FileType.VIDEO:
                result = await self._process_video(file_path)
                processing_result["operations"].append(result)
            elif file_type == FileType.AUDIO:
                result = await self._process_audio(file_path)
                processing_result["operations"].append(result)
            elif file_type == FileType.DOCUMENT:
                result = await self._process_document(file_path)
                processing_result["operations"].append(result)
            elif file_type == FileType.ARCHIVE:
                result = await self._process_archive(file_path)
                processing_result["operations"].append(result)
            
            # Update metadata
            file_metadata["processed"] = True
            file_metadata["processing_result"] = processing_result
            self.metadata_db[file_id] = file_metadata
            await self._save_metadata(file_id, file_metadata)
            
            return processing_result
            
        except Exception as e:
            logger.error(f"File processing failed: {e}")
            return {"status": "error", "error": str(e)}
    
    async def _process_image(self, file_path: Path) -> Dict[str, Any]:
        """Process image file"""
        try:
            if not PIL_AVAILABLE:
                return {"status": "error", "error": "PIL not available"}
            
            with Image.open(file_path) as img:
                # Get image info
                info = {
                    "format": img.format,
                    "mode": img.mode,
                    "size": img.size,
                    "width": img.width,
                    "height": img.height
                }
                
                # Create thumbnail
                thumbnail_path = self.processed_path / f"thumb_{file_path.name}"
                img.thumbnail((300, 300))
                img.save(thumbnail_path)
                
                return {
                    "status": "success",
                    "operation": "image_processing",
                    "info": info,
                    "thumbnail_path": str(thumbnail_path)
                }
                
        except Exception as e:
            return {"status": "error", "error": str(e)}
    
    async def _process_video(self, file_path: Path) -> Dict[str, Any]:
        """Process video file"""
        try:
            # For now, just return basic info
            # In a real implementation, you'd use ffmpeg or similar
            return {
                "status": "success",
                "operation": "video_processing",
                "message": "Video processing not implemented yet"
            }
        except Exception as e:
            return {"status": "error", "error": str(e)}
    
    async def _process_audio(self, file_path: Path) -> Dict[str, Any]:
        """Process audio file"""
        try:
            # For now, just return basic info
            # In a real implementation, you'd use librosa or similar
            return {
                "status": "success",
                "operation": "audio_processing",
                "message": "Audio processing not implemented yet"
            }
        except Exception as e:
            return {"status": "error", "error": str(e)}
    
    async def _process_document(self, file_path: Path) -> Dict[str, Any]:
        """Process document file"""
        try:
            # For now, just return basic info
            # In a real implementation, you'd use PyPDF2, python-docx, etc.
            return {
                "status": "success",
                "operation": "document_processing",
                "message": "Document processing not implemented yet"
            }
        except Exception as e:
            return {"status": "error", "error": str(e)}
    
    async def _process_archive(self, file_path: Path) -> Dict[str, Any]:
        """Process archive file"""
        try:
            # For now, just return basic info
            # In a real implementation, you'd extract and analyze contents
            return {
                "status": "success",
                "operation": "archive_processing",
                "message": "Archive processing not implemented yet"
            }
        except Exception as e:
            return {"status": "error", "error": str(e)}
    
    async def _save_metadata(self, file_id: str, metadata: Dict[str, Any]):
        """Save metadata to file"""
        try:
            metadata_path = self.upload_path / f"{file_id}.meta"
            async with aiofiles.open(metadata_path, 'w') as f:
                await f.write(json.dumps(metadata, indent=2))
        except Exception as e:
            logger.error(f"Failed to save metadata: {e}")
    
    def _find_file_by_hash(self, file_hash: str) -> Optional[Dict[str, Any]]:
        """Find file by hash"""
        for file_id, metadata in self.metadata_db.items():
            if metadata.get("file_hash") == file_hash:
                return metadata
        return None
    
    async def get_file(self, file_id: str) -> Dict[str, Any]:
        """Get file information"""
        try:
            if file_id in self.metadata_db:
                return {
                    "status": "success",
                    "file_info": self.metadata_db[file_id]
                }
            else:
                return {"status": "error", "error": "File not found"}
        except Exception as e:
            return {"status": "error", "error": str(e)}
    
    async def delete_file(self, file_id: str) -> Dict[str, Any]:
        """Delete file and metadata"""
        try:
            if file_id in self.metadata_db:
                metadata = self.metadata_db[file_id]
                file_path = Path(metadata["file_path"])
                
                # Delete file
                if file_path.exists():
                    os.remove(file_path)
                
                # Delete metadata file
                metadata_path = self.upload_path / f"{file_id}.meta"
                if metadata_path.exists():
                    os.remove(metadata_path)
                
                # Remove from database
                del self.metadata_db[file_id]
                
                return {"status": "success", "message": "File deleted successfully"}
            else:
                return {"status": "error", "error": "File not found"}
        except Exception as e:
            return {"status": "error", "error": str(e)}
    
    async def list_files(self, file_type: str = None, limit: int = 100) -> Dict[str, Any]:
        """List files with optional filtering"""
        try:
            files = list(self.metadata_db.values())
            
            if file_type:
                files = [f for f in files if f.get("file_type") == file_type]
            
            # Sort by upload time (newest first)
            files.sort(key=lambda x: x.get("upload_time", ""), reverse=True)
            
            # Apply limit
            files = files[:limit]
            
            return {
                "status": "success",
                "files": files,
                "count": len(files),
                "total": len(self.metadata_db)
            }
        except Exception as e:
            return {"status": "error", "error": str(e)}
    
    async def search_files(self, query: str) -> Dict[str, Any]:
        """Search files by filename or metadata"""
        try:
            results = []
            query_lower = query.lower()
            
            for file_id, metadata in self.metadata_db.items():
                # Search in filename
                if query_lower in metadata.get("original_filename", "").lower():
                    results.append(metadata)
                # Search in metadata
                elif query_lower in str(metadata.get("metadata", {})).lower():
                    results.append(metadata)
            
            return {
                "status": "success",
                "results": results,
                "count": len(results),
                "query": query
            }
        except Exception as e:
            return {"status": "error", "error": str(e)}
    
    def get_storage_stats(self) -> Dict[str, Any]:
        """Get storage statistics"""
        try:
            total_files = len(self.metadata_db)
            total_size = sum(metadata.get("file_size", 0) for metadata in self.metadata_db.values())
            
            file_types = {}
            for metadata in self.metadata_db.values():
                file_type = metadata.get("file_type", "unknown")
                file_types[file_type] = file_types.get(file_type, 0) + 1
            
            return {
                "total_files": total_files,
                "total_size": total_size,
                "total_size_mb": total_size / (1024 * 1024),
                "file_types": file_types,
                "storage_path": str(self.base_storage_path),
                "timestamp": datetime.now().isoformat()
            }
        except Exception as e:
            return {"status": "error", "error": str(e)}

# Factory function
def create_file_manager(base_storage_path: str = "storage") -> FileManager:
    """Create a file manager instance"""
    return FileManager(base_storage_path)

# Example usage
if __name__ == "__main__":
    manager = create_file_manager()
    print("File Manager created successfully")
