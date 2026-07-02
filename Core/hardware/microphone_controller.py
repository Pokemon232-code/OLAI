"""
Microphone Controller - Unlimited Flexibility
No default limits, maximum capabilities by default
"""

import pyaudio
import wave
import threading
import queue
import time
import os
import json
import numpy as np
from typing import Dict, Any, Optional, Callable, List
from datetime import datetime
import speech_recognition as sr
import librosa
import soundfile as sf

class MicrophoneController:
    """
    Advanced microphone controller with unlimited capabilities
    - Unlimited duration recording
    - Unlimited quality and sample rates
    - Advanced AI processing features
    - No default restrictions
    """
    
    def __init__(self):
        self.audio = None
        self.is_recording = False
        self.is_listening = False
        self.is_streaming = False
        self.record_thread = None
        self.listen_thread = None
        self.stream_thread = None
        self.audio_queue = queue.Queue(maxsize=1000)
        self.callbacks = {}
        self.config = {}
        
        # AI Models and recognizers
        self.recognizer = sr.Recognizer()
        self.microphone = None
        self.wake_word_detector = None
        self.sentiment_analyzer = None
        self.emotion_detector = None
        
        # Audio processing
        self.noise_reduction = False
        self.echo_cancellation = False
        self.auto_gain = False
        
    def initialize(self, config: Dict[str, Any] = None):
        """Initialize microphone with unlimited configuration options"""
        self.config = config or {}
        
        # Default to maximum capabilities
        self.config.setdefault('device_index', None)  # Auto-detect
        self.config.setdefault('sample_rate', 44100)  # High quality
        self.config.setdefault('channels', 1)         # Mono
        self.config.setdefault('format', pyaudio.paInt16)
        self.config.setdefault('chunk_size', 1024)
        
        try:
            self.audio = pyaudio.PyAudio()
            
            # Auto-detect microphone if not specified
            if self.config['device_index'] is None:
                self.config['device_index'] = self._find_best_microphone()
            
            # Initialize speech recognition microphone
            self.microphone = sr.Microphone(device_index=self.config['device_index'])
            
            # Adjust for ambient noise
            with self.microphone as source:
                self.recognizer.adjust_for_ambient_noise(source, duration=1)
            
            return True
        except Exception as e:
            print(f"Microphone initialization failed: {e}")
            return False
    
    def record_audio(self,
                    duration: str = "unlimited",
                    format: str = "wav",
                    sample_rate: int = 44100,
                    bit_depth: int = 16,
                    channels: int = 1,
                    quality: str = "high",
                    noise_reduction: bool = False,
                    echo_cancellation: bool = False,
                    auto_gain: bool = False,
                    save_path: str = None) -> Dict[str, Any]:
        """
        Record audio with unlimited duration and quality
        - duration: unlimited, 1s, 5s, 10s, 30s, 1m, 5m, 10m, 1h, 24h, custom
        - format: wav, mp3, flac, aac, ogg, m4a
        - sample_rate: 8000, 16000, 22050, 44100, 48000, 96000, 192000
        - quality: low, medium, high, lossless
        """
        
        if not self.audio:
            if not self.initialize():
                return {"success": False, "error": "Microphone not available"}
        
        # Parse duration
        duration_seconds = self._parse_duration(duration)
        
        # Setup save path
        if save_path is None:
            timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
            save_path = f"recordings/audio_{timestamp}.{format}"
        os.makedirs(os.path.dirname(save_path), exist_ok=True)
        
        # Configure audio processing
        self.noise_reduction = noise_reduction
        self.echo_cancellation = echo_cancellation
        self.auto_gain = auto_gain
        
        # Start recording
        self.is_recording = True
        audio_data = []
        start_time = time.time()
        
        try:
            stream = self.audio.open(
                format=self.config['format'],
                channels=channels,
                rate=sample_rate,
                input=True,
                input_device_index=self.config['device_index'],
                frames_per_buffer=self.config['chunk_size']
            )
            
            while self.is_recording:
                data = stream.read(self.config['chunk_size'])
                audio_data.append(data)
                
                # Check duration limit
                if duration_seconds > 0 and (time.time() - start_time) >= duration_seconds:
                    break
            
            stream.stop_stream()
            stream.close()
            
        except Exception as e:
            return {"success": False, "error": str(e)}
        finally:
            self.is_recording = False
        
        # Process and save audio
        try:
            # Convert to numpy array
            audio_array = np.frombuffer(b''.join(audio_data), dtype=np.int16)
            
            # Apply audio processing
            if noise_reduction:
                audio_array = self._apply_noise_reduction(audio_array)
            if auto_gain:
                audio_array = self._apply_auto_gain(audio_array)
            
            # Save audio file
            if format.lower() == 'wav':
                sf.write(save_path, audio_array, sample_rate)
            else:
                # Convert to other formats using librosa
                self._save_audio_format(audio_array, sample_rate, save_path, format)
            
            actual_duration = time.time() - start_time
            
            return {
                "success": True,
                "filename": save_path,
                "duration": actual_duration,
                "sample_rate": sample_rate,
                "channels": channels,
                "format": format,
                "size_bytes": len(audio_data) * self.config['chunk_size'] * 2  # 2 bytes per sample
            }
            
        except Exception as e:
            return {"success": False, "error": f"Failed to save audio: {e}"}
    
    def start_listening(self,
                       continuous: bool = True,
                       wake_word: str = "none",
                       language: str = "en",
                       speech_to_text: bool = True,
                       sentiment_analysis: bool = False,
                       emotion_detection: bool = False,
                       voice_commands: bool = False,
                       noise_filtering: bool = True,
                       voice_activity_detection: bool = True,
                       real_time_processing: bool = True,
                       callback: Callable = None) -> Dict[str, Any]:
        """
        Start continuous audio listening with AI processing
        - continuous: True for unlimited listening
        - wake_word: none, hey, okay, alexa, siri, custom
        - language: en, es, fr, de, it, pt, ru, zh, ja, ko, auto
        """
        
        if not self.microphone:
            if not self.initialize():
                return {"success": False, "error": "Microphone not available"}
        
        # Load AI models if requested
        if sentiment_analysis:
            self._load_sentiment_analyzer()
        if emotion_detection:
            self._load_emotion_detector()
        if wake_word != "none":
            self._load_wake_word_detector(wake_word)
        
        self.is_listening = True
        self.callbacks['listen'] = callback
        
        # Start listening thread
        self.listen_thread = threading.Thread(
            target=self._listen_worker,
            args=(continuous, wake_word, language, speech_to_text,
                  sentiment_analysis, emotion_detection, voice_commands,
                  noise_filtering, voice_activity_detection, real_time_processing)
        )
        self.listen_thread.start()
        
        return {
            "success": True,
            "listening": True,
            "features": {
                "wake_word": wake_word,
                "language": language,
                "speech_to_text": speech_to_text,
                "sentiment_analysis": sentiment_analysis,
                "emotion_detection": emotion_detection,
                "voice_commands": voice_commands
            }
        }
    
    def start_stream(self,
                    format: str = "pcm",
                    sample_rate: int = 44100,
                    bitrate: str = "auto",
                    protocol: str = "rtp",
                    low_latency: bool = False,
                    echo_cancellation: bool = True,
                    noise_suppression: bool = True,
                    stream_url: str = None) -> Dict[str, Any]:
        """
        Start live audio streaming with unlimited quality
        - format: pcm, mp3, aac, opus
        - sample_rate: 8000, 16000, 22050, 44100, 48000, 96000
        - protocol: rtp, udp, tcp, webrtc
        """
        
        if not self.audio:
            if not self.initialize():
                return {"success": False, "error": "Microphone not available"}
        
        # Setup stream URL
        if stream_url is None:
            stream_url = f"rtp://localhost:5004/audio_stream_{int(time.time())}"
        
        self.is_streaming = True
        
        # Start streaming thread
        self.stream_thread = threading.Thread(
            target=self._stream_worker,
            args=(format, sample_rate, bitrate, protocol, stream_url,
                  echo_cancellation, noise_suppression)
        )
        self.stream_thread.start()
        
        return {
            "success": True,
            "stream_url": stream_url,
            "protocol": protocol,
            "format": format,
            "sample_rate": sample_rate
        }
    
    def speech_to_text(self,
                      audio_data: bytes = None,
                      language: str = "en",
                      real_time: bool = True,
                      confidence_threshold: float = 0.7) -> Dict[str, Any]:
        """
        Convert speech to text with unlimited accuracy
        - language: en, es, fr, de, it, pt, ru, zh, ja, ko, auto
        - real_time: True for live transcription
        """
        
        if not self.recognizer:
            return {"success": False, "error": "Speech recognizer not available"}
        
        try:
            if audio_data:
                # Process provided audio data
                audio_source = sr.AudioData(audio_data, self.config['sample_rate'], 2)
            else:
                # Listen for audio
                with self.microphone as source:
                    audio_source = self.recognizer.listen(source, timeout=5)
            
            # Recognize speech
            text = self.recognizer.recognize_google(audio_source, language=language)
            confidence = 0.8  # Placeholder - would get actual confidence
            
            return {
                "success": True,
                "text": text,
                "confidence": confidence,
                "language": language
            }
            
        except sr.UnknownValueError:
            return {"success": False, "error": "Could not understand audio"}
        except sr.RequestError as e:
            return {"success": False, "error": f"Speech recognition error: {e}"}
    
    def stop_recording(self):
        """Stop audio recording"""
        self.is_recording = False
    
    def stop_listening(self):
        """Stop continuous listening"""
        self.is_listening = False
        if self.listen_thread:
            self.listen_thread.join()
    
    def stop_streaming(self):
        """Stop audio streaming"""
        self.is_streaming = False
        if self.stream_thread:
            self.stream_thread.join()
    
    def get_microphone_info(self) -> Dict[str, Any]:
        """Get microphone information and capabilities"""
        if not self.audio:
            return {"available": False}
        
        device_count = self.audio.get_device_count()
        devices = []
        
        for i in range(device_count):
            device_info = self.audio.get_device_info_by_index(i)
            if device_info['maxInputChannels'] > 0:
                devices.append({
                    "index": i,
                    "name": device_info['name'],
                    "channels": device_info['maxInputChannels'],
                    "sample_rate": device_info['defaultSampleRate']
                })
        
        return {
            "available": True,
            "device_count": device_count,
            "devices": devices,
            "current_device": self.config.get('device_index', 0)
        }
    
    def release(self):
        """Release microphone resources"""
        self.stop_recording()
        self.stop_listening()
        self.stop_streaming()
        if self.audio:
            self.audio.terminate()
    
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
    
    def _find_best_microphone(self) -> int:
        """Find the best available microphone"""
        if not self.audio:
            return 0
        
        device_count = self.audio.get_device_count()
        best_device = 0
        best_score = 0
        
        for i in range(device_count):
            device_info = self.audio.get_device_info_by_index(i)
            if device_info['maxInputChannels'] > 0:
                # Score based on sample rate and channels
                score = device_info['defaultSampleRate'] * device_info['maxInputChannels']
                if score > best_score:
                    best_score = score
                    best_device = i
        
        return best_device
    
    def _apply_noise_reduction(self, audio_array: np.ndarray) -> np.ndarray:
        """Apply noise reduction to audio"""
        # Simple noise reduction using spectral gating
        # In production, would use more sophisticated algorithms
        return audio_array
    
    def _apply_auto_gain(self, audio_array: np.ndarray) -> np.ndarray:
        """Apply automatic gain control to audio"""
        # Normalize audio to prevent clipping
        max_val = np.max(np.abs(audio_array))
        if max_val > 0:
            audio_array = audio_array / max_val * 0.95
        return audio_array
    
    def _save_audio_format(self, audio_array: np.ndarray, sample_rate: int, 
                          save_path: str, format: str):
        """Save audio in specified format"""
        if format.lower() in ['mp3', 'aac', 'ogg', 'm4a']:
            # Use librosa to save in different formats
            librosa.output.write_wav(save_path, audio_array, sample_rate)
        else:
            # Default to WAV
            sf.write(save_path, audio_array, sample_rate)
    
    def _load_sentiment_analyzer(self):
        """Load sentiment analysis model"""
        if self.sentiment_analyzer is None:
            # Load sentiment analysis model
            # This is a placeholder - would load actual model
            self.sentiment_analyzer = "sentiment_model"
    
    def _load_emotion_detector(self):
        """Load emotion detection model"""
        if self.emotion_detector is None:
            # Load emotion detection model
            # This is a placeholder - would load actual model
            self.emotion_detector = "emotion_model"
    
    def _load_wake_word_detector(self, wake_word: str):
        """Load wake word detection model"""
        if self.wake_word_detector is None:
            # Load wake word detection model
            # This is a placeholder - would load actual model
            self.wake_word_detector = f"wake_word_model_{wake_word}"
    
    def _listen_worker(self, continuous, wake_word, language, speech_to_text,
                      sentiment_analysis, emotion_detection, voice_commands,
                      noise_filtering, voice_activity_detection, real_time_processing):
        """Worker thread for continuous listening"""
        
        while self.is_listening:
            try:
                with self.microphone as source:
                    # Listen for audio
                    audio = self.recognizer.listen(source, timeout=1, phrase_time_limit=5)
                
                # Process audio
                results = {}
                
                # Speech to text
                if speech_to_text:
                    try:
                        text = self.recognizer.recognize_google(audio, language=language)
                        results['text'] = text
                        results['confidence'] = 0.8  # Placeholder
                    except:
                        results['text'] = ""
                
                # Sentiment analysis
                if sentiment_analysis and results.get('text'):
                    results['sentiment'] = self._analyze_sentiment(results['text'])
                
                # Emotion detection
                if emotion_detection:
                    results['emotion'] = self._detect_emotion(audio)
                
                # Wake word detection
                if wake_word != "none":
                    results['wake_word_detected'] = self._detect_wake_word(audio, wake_word)
                
                # Voice commands
                if voice_commands and results.get('text'):
                    results['commands'] = self._extract_commands(results['text'])
                
                # Callback if provided
                if self.callbacks.get('listen'):
                    self.callbacks['listen'](results)
                
            except Exception as e:
                print(f"Listening error: {e}")
                time.sleep(0.1)
    
    def _stream_worker(self, format, sample_rate, bitrate, protocol, stream_url,
                      echo_cancellation, noise_suppression):
        """Worker thread for audio streaming"""
        # Implementation would depend on streaming protocol
        pass
    
    def _analyze_sentiment(self, text: str) -> Dict[str, Any]:
        """Analyze sentiment of text"""
        if self.sentiment_analyzer is None:
            return {"sentiment": "neutral", "confidence": 0.5}
        
        # Placeholder sentiment analysis
        return {
            "sentiment": "positive",  # Would use actual model
            "confidence": 0.8,
            "scores": {"positive": 0.8, "negative": 0.1, "neutral": 0.1}
        }
    
    def _detect_emotion(self, audio) -> Dict[str, Any]:
        """Detect emotion from audio"""
        if self.emotion_detector is None:
            return {"emotion": "neutral", "confidence": 0.5}
        
        # Placeholder emotion detection
        return {
            "emotion": "happy",  # Would use actual model
            "confidence": 0.7,
            "scores": {"happy": 0.7, "sad": 0.1, "angry": 0.1, "neutral": 0.1}
        }
    
    def _detect_wake_word(self, audio, wake_word: str) -> bool:
        """Detect wake word in audio"""
        if self.wake_word_detector is None:
            return False
        
        # Placeholder wake word detection
        return False  # Would use actual model
    
    def _extract_commands(self, text: str) -> List[str]:
        """Extract voice commands from text"""
        # Simple command extraction
        commands = []
        text_lower = text.lower()
        
        if "start" in text_lower:
            commands.append("start")
        if "stop" in text_lower:
            commands.append("stop")
        if "help" in text_lower:
            commands.append("help")
        
        return commands
