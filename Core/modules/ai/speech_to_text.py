#!/usr/bin/env python3
"""
Speech-to-Text Processor - Advanced Voice Recognition
Converts speech to text with multiple engines and language support
"""

import os
import numpy as np
from typing import Dict, List, Any, Optional
from datetime import datetime
import logging
import tempfile

try:
    import whisper
    WHISPER_AVAILABLE = True
except ImportError:
    WHISPER_AVAILABLE = False

try:
    import speech_recognition as sr
    SPEECH_RECOGNITION_AVAILABLE = True
except ImportError:
    SPEECH_RECOGNITION_AVAILABLE = False

try:
    import librosa
    LIBROSA_AVAILABLE = True
except ImportError:
    LIBROSA_AVAILABLE = False

logger = logging.getLogger(__name__)

class SpeechToTextProcessor:
    """
    Advanced speech-to-text processor with multiple engines
    - Multiple STT engines (Whisper, Google Speech, Azure, etc.)
    - Real-time and batch processing
    - Multiple language support
    - Audio preprocessing for better accuracy
    """
    
    def __init__(self):
        self.engines = {}
        self.supported_languages = ['en', 'es', 'fr', 'de', 'it', 'pt', 'ru', 'zh', 'ja', 'ko', 'hi', 'ar']
        self.audio_formats = ['wav', 'mp3', 'flac', 'ogg', 'm4a']
        
        # Initialize available STT engines
        self._initialize_engines()
    
    def _initialize_engines(self):
        """Initialize available STT engines"""
        if WHISPER_AVAILABLE:
            self.engines['whisper'] = {
                'available': True,
                'languages': self.supported_languages,
                'accuracy': 'very_high',
                'real_time': False
            }
        
        if SPEECH_RECOGNITION_AVAILABLE:
            self.engines['google'] = {
                'available': True,
                'languages': self.supported_languages,
                'accuracy': 'high',
                'real_time': True
            }
            
            self.engines['azure'] = {
                'available': True,
                'languages': self.supported_languages,
                'accuracy': 'high',
                'real_time': True
            }
    
    def preprocess_audio(self, audio_data: np.ndarray, sample_rate: int = 16000) -> np.ndarray:
        """Preprocess audio for better STT accuracy"""
        try:
            if LIBROSA_AVAILABLE:
                # Normalize audio
                audio_normalized = librosa.util.normalize(audio_data)
                
                # Remove noise (simple high-pass filter)
                audio_filtered = librosa.effects.preemphasis(audio_normalized)
                
                # Trim silence
                audio_trimmed, _ = librosa.effects.trim(audio_filtered, top_db=20)
                
                return audio_trimmed
            else:
                # Basic normalization without librosa
                return audio_data / np.max(np.abs(audio_data))
                
        except Exception as e:
            logger.error(f"Audio preprocessing failed: {e}")
            return audio_data
    
    def transcribe_whisper(self, audio_data: np.ndarray, language: str = 'en', model_size: str = 'base') -> Dict[str, Any]:
        """Transcribe audio using Whisper"""
        try:
            if not WHISPER_AVAILABLE:
                return {"status": "error", "error": "Whisper not available"}
            
            # Load Whisper model
            model = whisper.load_model(model_size)
            
            # Preprocess audio
            audio_processed = self.preprocess_audio(audio_data)
            
            # Transcribe
            result = model.transcribe(audio_processed, language=language)
            
            return {
                "status": "success",
                "text": result["text"],
                "language": result.get("language", language),
                "segments": result.get("segments", []),
                "engine": "whisper",
                "model_size": model_size,
                "confidence": 0.9,  # Whisper doesn't provide confidence scores
                "timestamp": datetime.now().isoformat()
            }
            
        except Exception as e:
            logger.error(f"Whisper transcription failed: {e}")
            return {"status": "error", "error": str(e), "engine": "whisper"}
    
    def transcribe_google(self, audio_data: np.ndarray, language: str = 'en-US') -> Dict[str, Any]:
        """Transcribe audio using Google Speech Recognition"""
        try:
            if not SPEECH_RECOGNITION_AVAILABLE:
                return {"status": "error", "error": "Google Speech Recognition not available"}
            
            # Initialize recognizer
            recognizer = sr.Recognizer()
            
            # Create AudioData object
            audio_source = sr.AudioData(audio_data.tobytes(), 16000, 2)
            
            # Transcribe
            text = recognizer.recognize_google(audio_source, language=language)
            
            return {
                "status": "success",
                "text": text,
                "language": language,
                "engine": "google",
                "confidence": 0.8,  # Google doesn't provide confidence scores
                "timestamp": datetime.now().isoformat()
            }
            
        except sr.UnknownValueError:
            return {"status": "error", "error": "Could not understand audio", "engine": "google"}
        except sr.RequestError as e:
            return {"status": "error", "error": f"Google Speech API error: {e}", "engine": "google"}
        except Exception as e:
            logger.error(f"Google transcription failed: {e}")
            return {"status": "error", "error": str(e), "engine": "google"}
    
    def transcribe_azure(self, audio_data: np.ndarray, language: str = 'en-US') -> Dict[str, Any]:
        """Transcribe audio using Azure Speech Services"""
        try:
            if not SPEECH_RECOGNITION_AVAILABLE:
                return {"status": "error", "error": "Azure Speech Recognition not available"}
            
            # Initialize recognizer
            recognizer = sr.Recognizer()
            
            # Create AudioData object
            audio_source = sr.AudioData(audio_data.tobytes(), 16000, 2)
            
            # Transcribe using Azure
            text = recognizer.recognize_azure(audio_source, language=language)
            
            return {
                "status": "success",
                "text": text,
                "language": language,
                "engine": "azure",
                "confidence": 0.85,
                "timestamp": datetime.now().isoformat()
            }
            
        except sr.UnknownValueError:
            return {"status": "error", "error": "Could not understand audio", "engine": "azure"}
        except sr.RequestError as e:
            return {"status": "error", "error": f"Azure Speech API error: {e}", "engine": "azure"}
        except Exception as e:
            logger.error(f"Azure transcription failed: {e}")
            return {"status": "error", "str(e)", "engine": "azure"}
    
    def transcribe(self, audio_data: np.ndarray, engine: str = 'auto', language: str = 'en') -> Dict[str, Any]:
        """Transcribe audio using specified or best available engine"""
        try:
            if engine == 'auto':
                # Try Whisper first (usually best accuracy), fallback to Google
                if WHISPER_AVAILABLE:
                    return self.transcribe_whisper(audio_data, language)
                elif SPEECH_RECOGNITION_AVAILABLE:
                    return self.transcribe_google(audio_data, language)
                else:
                    return {"status": "error", "error": "No STT engines available"}
            
            elif engine == 'whisper':
                return self.transcribe_whisper(audio_data, language)
            
            elif engine == 'google':
                return self.transcribe_google(audio_data, language)
            
            elif engine == 'azure':
                return self.transcribe_azure(audio_data, language)
            
            else:
                return {"status": "error", "error": f"Unknown STT engine: {engine}"}
                
        except Exception as e:
            logger.error(f"STT transcription failed: {e}")
            return {"status": "error", "error": str(e)}
    
    def transcribe_from_file(self, audio_path: str, engine: str = 'auto', language: str = 'en') -> Dict[str, Any]:
        """Transcribe audio from file"""
        try:
            if not os.path.exists(audio_path):
                return {"status": "error", "error": f"Audio file not found: {audio_path}"}
            
            # Load audio file
            if LIBROSA_AVAILABLE:
                audio_data, sample_rate = librosa.load(audio_path, sr=16000)
            else:
                # Fallback to basic loading
                import wave
                with wave.open(audio_path, 'rb') as wav_file:
                    audio_data = np.frombuffer(wav_file.readframes(-1), dtype=np.int16)
                    sample_rate = wav_file.getframerate()
            
            # Transcribe
            result = self.transcribe(audio_data, engine, language)
            result['audio_path'] = audio_path
            result['sample_rate'] = sample_rate
            
            return result
            
        except Exception as e:
            logger.error(f"File STT transcription failed: {e}")
            return {"status": "error", "error": str(e)}
    
    def real_time_transcribe(self, audio_stream, engine: str = 'google', language: str = 'en') -> Dict[str, Any]:
        """Real-time transcription from audio stream"""
        try:
            if engine == 'google' and SPEECH_RECOGNITION_AVAILABLE:
                recognizer = sr.Recognizer()
                microphone = sr.Microphone()
                
                with microphone as source:
                    recognizer.adjust_for_ambient_noise(source)
                    audio = recognizer.listen(source)
                
                text = recognizer.recognize_google(audio, language=language)
                
                return {
                    "status": "success",
                    "text": text,
                    "language": language,
                    "engine": "google",
                    "real_time": True,
                    "timestamp": datetime.now().isoformat()
                }
            
            else:
                return {"status": "error", "error": f"Real-time transcription not supported for engine: {engine}"}
                
        except Exception as e:
            logger.error(f"Real-time STT failed: {e}")
            return {"status": "error", "error": str(e)}
    
    def batch_transcribe(self, audio_paths: List[str], engine: str = 'auto', language: str = 'en') -> Dict[str, Any]:
        """Transcribe multiple audio files"""
        try:
            results = []
            
            for audio_path in audio_paths:
                result = self.transcribe_from_file(audio_path, engine, language)
                results.append(result)
            
            # Calculate overall statistics
            successful_transcriptions = [r for r in results if r.get('status') == 'success']
            total_text = ' '.join([r.get('text', '') for r in successful_transcriptions])
            avg_confidence = sum([r.get('confidence', 0) for r in successful_transcriptions]) / len(successful_transcriptions) if successful_transcriptions else 0
            
            return {
                "status": "success",
                "total_files": len(audio_paths),
                "successful_transcriptions": len(successful_transcriptions),
                "failed_transcriptions": len(results) - len(successful_transcriptions),
                "combined_text": total_text,
                "average_confidence": avg_confidence,
                "results": results,
                "timestamp": datetime.now().isoformat()
            }
            
        except Exception as e:
            logger.error(f"Batch STT transcription failed: {e}")
            return {"status": "error", "error": str(e)}

# Factory function for easy module usage
def create_speech_to_text_processor() -> SpeechToTextProcessor:
    """Create a speech-to-text processor instance"""
    return SpeechToTextProcessor()

# Example usage
if __name__ == "__main__":
    processor = create_speech_to_text_processor()
    
    # Test with sample audio file
    result = processor.transcribe_from_file("sample_audio.wav")
    print(json.dumps(result, indent=2))
