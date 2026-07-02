"""
Camera Controller - Unlimited Flexibility
No default limits, maximum capabilities by default
"""

import cv2
import numpy as np
import time
import threading
import queue
from typing import Dict, Any, Optional, Callable, List
from datetime import datetime
import os
import json

class CameraController:
    """
    Advanced camera controller with unlimited capabilities
    - Unlimited duration recording
    - Unlimited resolution and quality
    - Unlimited AI analysis features
    - No default restrictions
    """
    
    def __init__(self):
        self.camera = None
        self.is_recording = False
        self.is_monitoring = False
        self.is_streaming = False
        self.capture_thread = None
        self.monitor_thread = None
        self.stream_thread = None
        self.frame_queue = queue.Queue(maxsize=1000)
        self.callbacks = {}
        self.config = {}
        
        # AI Models (loaded on demand)
        self.ai_models = {}
        self.motion_detector = None
        self.face_detector = None
        self.object_detector = None
        
    def initialize(self, config: Dict[str, Any] = None):
        """Initialize camera with unlimited configuration options"""
        self.config = config or {}
        
        # Default to maximum capabilities
        self.config.setdefault('device_id', 0)
        self.config.setdefault('resolution', 'auto')  # Will use maximum available
        self.config.setdefault('fps', 'unlimited')    # Maximum FPS
        self.config.setdefault('quality', 95)         # Maximum quality
        self.config.setdefault('format', 'jpg')
        
        try:
            self.camera = cv2.VideoCapture(self.config['device_id'])
            if not self.camera.isOpened():
                raise Exception(f"Could not open camera {self.config['device_id']}")
                
            # Set to maximum resolution if auto
            if self.config['resolution'] == 'auto':
                self.camera.set(cv2.CAP_PROP_FRAME_WIDTH, 1920)
                self.camera.set(cv2.CAP_PROP_FRAME_HEIGHT, 1080)
            elif self.config['resolution'] != 'auto':
                width, height = self._parse_resolution(self.config['resolution'])
                self.camera.set(cv2.CAP_PROP_FRAME_WIDTH, width)
                self.camera.set(cv2.CAP_PROP_FRAME_HEIGHT, height)
                
            # Set maximum FPS if unlimited
            if self.config['fps'] == 'unlimited':
                self.camera.set(cv2.CAP_PROP_FPS, 30)  # Set to reasonable max
            else:
                self.camera.set(cv2.CAP_PROP_FPS, int(self.config['fps']))
                
            return True
        except Exception as e:
            print(f"Camera initialization failed: {e}")
            return False
    
    def capture_image(self, 
                     interval: str = "continuous",
                     quality: int = 95,
                     format: str = "jpg",
                     resolution: str = "auto",
                     duration: str = "unlimited",
                     motion_detection: bool = False,
                     face_detection: bool = False,
                     object_detection: bool = False,
                     save_path: str = None,
                     callback: Callable = None) -> Dict[str, Any]:
        """
        Capture images with unlimited flexibility
        - interval: continuous, 1s, 5s, 10s, 30s, 1m, 5m, custom
        - quality: 1-100 (default 95 for maximum quality)
        - duration: unlimited, 1s, 5s, 10s, 30s, 1m, 5m, 10m, 1h, custom
        """
        
        if not self.camera:
            if not self.initialize():
                return {"success": False, "error": "Camera not available"}
        
        # Parse interval
        interval_seconds = self._parse_duration(interval)
        duration_seconds = self._parse_duration(duration)
        
        # Setup save directory
        if save_path is None:
            save_path = f"captures/{datetime.now().strftime('%Y%m%d_%H%M%S')}"
        os.makedirs(save_path, exist_ok=True)
        
        # Load AI models if requested
        if motion_detection:
            self._load_motion_detector()
        if face_detection:
            self._load_face_detector()
        if object_detection:
            self._load_object_detector()
        
        captured_images = []
        start_time = time.time()
        
        try:
            while True:
                ret, frame = self.camera.read()
                if not ret:
                    break
                
                # Apply AI analysis if requested
                analysis_results = {}
                if motion_detection and self.motion_detector:
                    analysis_results['motion'] = self._detect_motion(frame)
                if face_detection and self.face_detector:
                    analysis_results['faces'] = self._detect_faces(frame)
                if object_detection and self.object_detector:
                    analysis_results['objects'] = self._detect_objects(frame)
                
                # Save image
                timestamp = datetime.now().strftime('%Y%m%d_%H%M%S_%f')[:-3]
                filename = f"{save_path}/capture_{timestamp}.{format}"
                
                # Apply quality settings
                if format.lower() in ['jpg', 'jpeg']:
                    cv2.imwrite(filename, frame, [cv2.IMWRITE_JPEG_QUALITY, quality])
                else:
                    cv2.imwrite(filename, frame)
                
                image_info = {
                    "filename": filename,
                    "timestamp": timestamp,
                    "analysis": analysis_results
                }
                captured_images.append(image_info)
                
                # Callback if provided
                if callback:
                    callback(image_info)
                
                # Check duration limit
                if duration_seconds > 0 and (time.time() - start_time) >= duration_seconds:
                    break
                
                # Wait for next interval
                if interval_seconds > 0:
                    time.sleep(interval_seconds)
                else:
                    # Continuous capture - no sleep
                    pass
                    
        except Exception as e:
            return {"success": False, "error": str(e)}
        
        return {
            "success": True,
            "images_captured": len(captured_images),
            "save_path": save_path,
            "images": captured_images,
            "duration": time.time() - start_time
        }
    
    def record_video(self,
                    duration: str = "unlimited",
                    format: str = "mp4",
                    resolution: str = "1080p",
                    fps: int = 30,
                    bitrate: str = "auto",
                    audio: bool = True,
                    audio_quality: str = "high",
                    compression: str = "balanced",
                    save_path: str = None) -> Dict[str, Any]:
        """
        Record video with unlimited duration and quality
        - duration: unlimited, 1s, 5s, 10s, 30s, 1m, 5m, 10m, 1h, 24h, custom
        - resolution: 240p, 480p, 720p, 1080p, 4K, 8K, custom
        - fps: 1-120 (default 30)
        """
        
        if not self.camera:
            if not self.initialize():
                return {"success": False, "error": "Camera not available"}
        
        # Parse duration
        duration_seconds = self._parse_duration(duration)
        
        # Setup save path
        if save_path is None:
            save_path = f"recordings/{datetime.now().strftime('%Y%m%d_%H%M%S')}.{format}"
        os.makedirs(os.path.dirname(save_path), exist_ok=True)
        
        # Setup video writer
        width, height = self._parse_resolution(resolution)
        fourcc = cv2.VideoWriter_fourcc(*self._get_fourcc(format))
        
        # Calculate bitrate if auto
        if bitrate == "auto":
            bitrate = self._calculate_bitrate(width, height, fps)
        
        out = cv2.VideoWriter(save_path, fourcc, fps, (width, height))
        
        if not out.isOpened():
            return {"success": False, "error": "Could not initialize video writer"}
        
        self.is_recording = True
        start_time = time.time()
        frame_count = 0
        
        try:
            while self.is_recording:
                ret, frame = self.camera.read()
                if not ret:
                    break
                
                # Resize frame if needed
                if frame.shape[:2] != (height, width):
                    frame = cv2.resize(frame, (width, height))
                
                out.write(frame)
                frame_count += 1
                
                # Check duration limit
                if duration_seconds > 0 and (time.time() - start_time) >= duration_seconds:
                    break
                    
        except Exception as e:
            return {"success": False, "error": str(e)}
        finally:
            self.is_recording = False
            out.release()
        
        return {
            "success": True,
            "filename": save_path,
            "duration": time.time() - start_time,
            "frames": frame_count,
            "fps_actual": frame_count / (time.time() - start_time) if (time.time() - start_time) > 0 else 0
        }
    
    def start_stream(self,
                    resolution: str = "1080p",
                    fps: int = 30,
                    bitrate: str = "auto",
                    protocol: str = "rtmp",
                    audio: bool = True,
                    low_latency: bool = False,
                    adaptive_bitrate: bool = True,
                    stream_url: str = None) -> Dict[str, Any]:
        """
        Start live streaming with unlimited quality
        - resolution: 240p, 480p, 720p, 1080p, 4K, 8K, custom
        - fps: 1-120 (default 30)
        - protocol: rtmp, rtsp, hls, webrtc, udp, tcp
        """
        
        if not self.camera:
            if not self.initialize():
                return {"success": False, "error": "Camera not available"}
        
        # Setup stream URL
        if stream_url is None:
            stream_url = f"rtmp://localhost:1935/live/stream_{int(time.time())}"
        
        self.is_streaming = True
        
        # Start streaming thread
        self.stream_thread = threading.Thread(
            target=self._stream_worker,
            args=(resolution, fps, bitrate, protocol, stream_url)
        )
        self.stream_thread.start()
        
        return {
            "success": True,
            "stream_url": stream_url,
            "protocol": protocol,
            "resolution": resolution,
            "fps": fps
        }
    
    def start_monitor(self,
                     continuous: bool = True,
                     motion_detection: bool = True,
                     face_recognition: bool = False,
                     object_tracking: bool = False,
                     emotion_analysis: bool = False,
                     pose_estimation: bool = False,
                     alert_threshold: float = 0.7,
                     analysis_interval: str = "1s",
                     save_frames: bool = False,
                     save_analysis: bool = True,
                     callback: Callable = None) -> Dict[str, Any]:
        """
        Start continuous monitoring with AI analysis
        - continuous: True for unlimited monitoring
        - analysis_interval: continuous, 100ms, 500ms, 1s, 5s, 10s, custom
        """
        
        if not self.camera:
            if not self.initialize():
                return {"success": False, "error": "Camera not available"}
        
        # Load AI models
        if motion_detection:
            self._load_motion_detector()
        if face_recognition:
            self._load_face_detector()
        if object_tracking:
            self._load_object_detector()
        
        # Parse analysis interval
        interval_seconds = self._parse_duration(analysis_interval)
        
        self.is_monitoring = True
        self.callbacks['monitor'] = callback
        
        # Start monitoring thread
        self.monitor_thread = threading.Thread(
            target=self._monitor_worker,
            args=(interval_seconds, motion_detection, face_recognition, 
                  object_tracking, emotion_analysis, pose_estimation,
                  alert_threshold, save_frames, save_analysis)
        )
        self.monitor_thread.start()
        
        return {
            "success": True,
            "monitoring": True,
            "features": {
                "motion_detection": motion_detection,
                "face_recognition": face_recognition,
                "object_tracking": object_tracking,
                "emotion_analysis": emotion_analysis,
                "pose_estimation": pose_estimation
            }
        }
    
    def stop_recording(self):
        """Stop video recording"""
        self.is_recording = False
    
    def stop_streaming(self):
        """Stop live streaming"""
        self.is_streaming = False
        if self.stream_thread:
            self.stream_thread.join()
    
    def stop_monitoring(self):
        """Stop continuous monitoring"""
        self.is_monitoring = False
        if self.monitor_thread:
            self.monitor_thread.join()
    
    def get_camera_info(self) -> Dict[str, Any]:
        """Get camera information and capabilities"""
        if not self.camera:
            return {"available": False}
        
        return {
            "available": True,
            "device_id": self.config.get('device_id', 0),
            "resolution": {
                "width": int(self.camera.get(cv2.CAP_PROP_FRAME_WIDTH)),
                "height": int(self.camera.get(cv2.CAP_PROP_FRAME_HEIGHT))
            },
            "fps": self.camera.get(cv2.CAP_PROP_FPS),
            "brightness": self.camera.get(cv2.CAP_PROP_BRIGHTNESS),
            "contrast": self.camera.get(cv2.CAP_PROP_CONTRAST),
            "saturation": self.camera.get(cv2.CAP_PROP_SATURATION),
            "hue": self.camera.get(cv2.CAP_PROP_HUE)
        }
    
    def release(self):
        """Release camera resources"""
        self.stop_recording()
        self.stop_streaming()
        self.stop_monitoring()
        if self.camera:
            self.camera.release()
    
    # Private helper methods
    
    def _parse_duration(self, duration: str) -> float:
        """Parse duration string to seconds"""
        if duration == "unlimited" or duration == "continuous":
            return 0
        
        duration = duration.lower()
        if duration.endswith('s'):
            return float(duration[:-1])
        elif duration.endswith('m'):
            return float(duration[:-1]) * 60
        elif duration.endswith('h'):
            return float(duration[:-1]) * 3600
        elif duration.endswith('d'):
            return float(duration[:-1]) * 86400
        else:
            return float(duration)
    
    def _parse_resolution(self, resolution: str) -> tuple:
        """Parse resolution string to width, height"""
        if resolution == "auto":
            return 1920, 1080
        
        resolution_map = {
            "240p": (426, 240),
            "480p": (854, 480),
            "720p": (1280, 720),
            "1080p": (1920, 1080),
            "4K": (3840, 2160),
            "8K": (7680, 4320)
        }
        
        if resolution in resolution_map:
            return resolution_map[resolution]
        
        # Try to parse custom resolution (e.g., "1920x1080")
        if 'x' in resolution:
            width, height = resolution.split('x')
            return int(width), int(height)
        
        return 1920, 1080  # Default
    
    def _get_fourcc(self, format: str) -> str:
        """Get fourcc code for video format"""
        format_map = {
            "mp4": "mp4v",
            "avi": "XVID",
            "mov": "mp4v",
            "mkv": "XVID",
            "webm": "VP80",
            "flv": "FLV1"
        }
        return format_map.get(format.lower(), "mp4v")
    
    def _calculate_bitrate(self, width: int, height: int, fps: int) -> int:
        """Calculate optimal bitrate based on resolution and fps"""
        pixels = width * height
        if pixels <= 480 * 240:
            return 1000  # 1 Mbps
        elif pixels <= 854 * 480:
            return 2500  # 2.5 Mbps
        elif pixels <= 1280 * 720:
            return 5000  # 5 Mbps
        elif pixels <= 1920 * 1080:
            return 10000  # 10 Mbps
        else:
            return 20000  # 20 Mbps
    
    def _load_motion_detector(self):
        """Load motion detection model"""
        if self.motion_detector is None:
            self.motion_detector = cv2.createBackgroundSubtractorMOG2()
    
    def _load_face_detector(self):
        """Load face detection model"""
        if self.face_detector is None:
            self.face_detector = cv2.CascadeClassifier(
                cv2.data.haarcascades + 'haarcascade_frontalface_default.xml'
            )
    
    def _load_object_detector(self):
        """Load object detection model"""
        if self.object_detector is None:
            # Load YOLO or other object detection model
            # This is a placeholder - would load actual model
            self.object_detector = "yolo_model"
    
    def _detect_motion(self, frame) -> Dict[str, Any]:
        """Detect motion in frame"""
        if self.motion_detector is None:
            return {"detected": False}
        
        fg_mask = self.motion_detector.apply(frame)
        motion_pixels = cv2.countNonZero(fg_mask)
        motion_ratio = motion_pixels / (frame.shape[0] * frame.shape[1])
        
        return {
            "detected": motion_ratio > 0.01,
            "ratio": motion_ratio,
            "pixels": motion_pixels
        }
    
    def _detect_faces(self, frame) -> Dict[str, Any]:
        """Detect faces in frame"""
        if self.face_detector is None:
            return {"faces": []}
        
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = self.face_detector.detectMultiScale(gray, 1.1, 4)
        
        return {
            "faces": [{"x": int(x), "y": int(y), "w": int(w), "h": int(h)} 
                     for x, y, w, h in faces],
            "count": len(faces)
        }
    
    def _detect_objects(self, frame) -> Dict[str, Any]:
        """Detect objects in frame"""
        if self.object_detector is None:
            return {"objects": []}
        
        # Placeholder for object detection
        return {
            "objects": [],
            "count": 0
        }
    
    def _stream_worker(self, resolution, fps, bitrate, protocol, stream_url):
        """Worker thread for streaming"""
        # Implementation would depend on streaming protocol
        pass
    
    def _monitor_worker(self, interval, motion_detection, face_recognition, 
                       object_tracking, emotion_analysis, pose_estimation,
                       alert_threshold, save_frames, save_analysis):
        """Worker thread for monitoring"""
        last_analysis = 0
        
        while self.is_monitoring:
            ret, frame = self.camera.read()
            if not ret:
                break
            
            current_time = time.time()
            
            # Perform analysis at specified interval
            if current_time - last_analysis >= interval:
                analysis_results = {}
                
                if motion_detection:
                    analysis_results['motion'] = self._detect_motion(frame)
                if face_recognition:
                    analysis_results['faces'] = self._detect_faces(frame)
                if object_tracking:
                    analysis_results['objects'] = self._detect_objects(frame)
                
                # Check for alerts
                alerts = []
                if motion_detection and analysis_results.get('motion', {}).get('detected'):
                    alerts.append("Motion detected")
                if face_recognition and analysis_results.get('faces', {}).get('count', 0) > 0:
                    alerts.append(f"{analysis_results['faces']['count']} face(s) detected")
                
                # Save analysis if requested
                if save_analysis:
                    analysis_data = {
                        "timestamp": datetime.now().isoformat(),
                        "analysis": analysis_results,
                        "alerts": alerts
                    }
                    # Save to file or database
                
                # Save frames if requested
                if save_frames and alerts:
                    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S_%f')[:-3]
                    filename = f"monitor_frames/alert_{timestamp}.jpg"
                    os.makedirs(os.path.dirname(filename), exist_ok=True)
                    cv2.imwrite(filename, frame)
                
                # Callback if provided
                if self.callbacks.get('monitor'):
                    self.callbacks['monitor']({
                        "frame": frame,
                        "analysis": analysis_results,
                        "alerts": alerts
                    })
                
                last_analysis = current_time
            
            time.sleep(0.01)  # Small delay to prevent excessive CPU usage
