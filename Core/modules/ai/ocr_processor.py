#!/usr/bin/env python3
"""
OCR Processor - Advanced Optical Character Recognition
Extracts text from images with high accuracy and multiple language support
"""

import cv2
import numpy as np
from typing import Dict, List, Any, Optional
from datetime import datetime
import logging
import os

try:
    import pytesseract
    TESSERACT_AVAILABLE = True
except ImportError:
    TESSERACT_AVAILABLE = False

try:
    import easyocr
    EASYOCR_AVAILABLE = True
except ImportError:
    EASYOCR_AVAILABLE = False

logger = logging.getLogger(__name__)

class OCRProcessor:
    """
    Advanced OCR processor with multiple engines and language support
    - Multiple OCR engines (Tesseract, EasyOCR)
    - Language detection and support
    - Image preprocessing for better accuracy
    - Text extraction with confidence scores
    """
    
    def __init__(self):
        self.engines = {}
        self.supported_languages = ['en', 'es', 'fr', 'de', 'it', 'pt', 'ru', 'zh', 'ja', 'ko']
        self.preprocessing_methods = ['grayscale', 'denoise', 'contrast', 'rotation']
        
        # Initialize available OCR engines
        self._initialize_engines()
    
    def _initialize_engines(self):
        """Initialize available OCR engines"""
        if TESSERACT_AVAILABLE:
            self.engines['tesseract'] = {
                'available': True,
                'languages': self.supported_languages,
                'accuracy': 'high'
            }
        
        if EASYOCR_AVAILABLE:
            self.engines['easyocr'] = {
                'available': True,
                'languages': self.supported_languages,
                'accuracy': 'very_high'
            }
    
    def preprocess_image(self, image: np.ndarray, method: str = 'auto') -> np.ndarray:
        """Preprocess image for better OCR accuracy"""
        try:
            if method == 'auto':
                # Apply multiple preprocessing techniques
                processed = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
                processed = cv2.medianBlur(processed, 3)
                processed = cv2.threshold(processed, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]
            elif method == 'grayscale':
                processed = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
            elif method == 'denoise':
                processed = cv2.fastNlMeansDenoising(image)
            elif method == 'contrast':
                processed = cv2.convertScaleAbs(image, alpha=1.5, beta=0)
            
            return processed
        except Exception as e:
            logger.error(f"Image preprocessing failed: {e}")
            return image
    
    def extract_text_tesseract(self, image: np.ndarray, language: str = 'eng') -> Dict[str, Any]:
        """Extract text using Tesseract OCR"""
        try:
            if not TESSERACT_AVAILABLE:
                return {"status": "error", "error": "Tesseract not available"}
            
            # Preprocess image
            processed_image = self.preprocess_image(image)
            
            # Extract text with confidence scores
            data = pytesseract.image_to_data(processed_image, lang=language, output_type=pytesseract.Output.DICT)
            
            # Process results
            text_blocks = []
            for i in range(len(data['text'])):
                if int(data['conf'][i]) > 30:  # Filter low confidence text
                    text_blocks.append({
                        'text': data['text'][i],
                        'confidence': int(data['conf'][i]),
                        'bbox': [data['left'][i], data['top'][i], data['width'][i], data['height'][i]]
                    })
            
            # Combine all text
            full_text = ' '.join([block['text'] for block in text_blocks if block['text'].strip()])
            
            return {
                "status": "success",
                "text": full_text,
                "confidence": sum([block['confidence'] for block in text_blocks]) / len(text_blocks) if text_blocks else 0,
                "text_blocks": text_blocks,
                "engine": "tesseract",
                "language": language,
                "timestamp": datetime.now().isoformat()
            }
            
        except Exception as e:
            logger.error(f"Tesseract OCR failed: {e}")
            return {"status": "error", "error": str(e), "engine": "tesseract"}
    
    def extract_text_easyocr(self, image: np.ndarray, languages: List[str] = ['en']) -> Dict[str, Any]:
        """Extract text using EasyOCR"""
        try:
            if not EASYOCR_AVAILABLE:
                return {"status": "error", "error": "EasyOCR not available"}
            
            # Initialize EasyOCR reader
            reader = easyocr.Reader(languages)
            
            # Extract text
            results = reader.readtext(image)
            
            # Process results
            text_blocks = []
            for (bbox, text, confidence) in results:
                if confidence > 0.3:  # Filter low confidence text
                    text_blocks.append({
                        'text': text,
                        'confidence': confidence,
                        'bbox': bbox
                    })
            
            # Combine all text
            full_text = ' '.join([block['text'] for block in text_blocks])
            
            return {
                "status": "success",
                "text": full_text,
                "confidence": sum([block['confidence'] for block in text_blocks]) / len(text_blocks) if text_blocks else 0,
                "text_blocks": text_blocks,
                "engine": "easyocr",
                "languages": languages,
                "timestamp": datetime.now().isoformat()
            }
            
        except Exception as e:
            logger.error(f"EasyOCR failed: {e}")
            return {"status": "error", "error": str(e), "engine": "easyocr"}
    
    def extract_text(self, image: np.ndarray, engine: str = 'auto', languages: List[str] = ['en']) -> Dict[str, Any]:
        """Extract text from image using specified or best available engine"""
        try:
            if engine == 'auto':
                # Try EasyOCR first (usually better), fallback to Tesseract
                if EASYOCR_AVAILABLE:
                    return self.extract_text_easyocr(image, languages)
                elif TESSERACT_AVAILABLE:
                    return self.extract_text_tesseract(image, languages[0])
                else:
                    return {"status": "error", "error": "No OCR engines available"}
            
            elif engine == 'tesseract':
                return self.extract_text_tesseract(image, languages[0])
            
            elif engine == 'easyocr':
                return self.extract_text_easyocr(image, languages)
            
            else:
                return {"status": "error", "error": f"Unknown OCR engine: {engine}"}
                
        except Exception as e:
            logger.error(f"OCR extraction failed: {e}")
            return {"status": "error", "error": str(e)}
    
    def extract_text_from_file(self, image_path: str, engine: str = 'auto', languages: List[str] = ['en']) -> Dict[str, Any]:
        """Extract text from image file"""
        try:
            if not os.path.exists(image_path):
                return {"status": "error", "error": f"Image file not found: {image_path}"}
            
            # Load image
            image = cv2.imread(image_path)
            if image is None:
                return {"status": "error", "error": f"Could not load image: {image_path}"}
            
            # Extract text
            result = self.extract_text(image, engine, languages)
            result['image_path'] = image_path
            
            return result
            
        except Exception as e:
            logger.error(f"File OCR extraction failed: {e}")
            return {"status": "error", "error": str(e)}
    
    def batch_extract_text(self, image_paths: List[str], engine: str = 'auto', languages: List[str] = ['en']) -> Dict[str, Any]:
        """Extract text from multiple images"""
        try:
            results = []
            
            for image_path in image_paths:
                result = self.extract_text_from_file(image_path, engine, languages)
                results.append(result)
            
            # Calculate overall statistics
            successful_extractions = [r for r in results if r.get('status') == 'success']
            total_text = ' '.join([r.get('text', '') for r in successful_extractions])
            avg_confidence = sum([r.get('confidence', 0) for r in successful_extractions]) / len(successful_extractions) if successful_extractions else 0
            
            return {
                "status": "success",
                "total_images": len(image_paths),
                "successful_extractions": len(successful_extractions),
                "failed_extractions": len(results) - len(successful_extractions),
                "combined_text": total_text,
                "average_confidence": avg_confidence,
                "results": results,
                "timestamp": datetime.now().isoformat()
            }
            
        except Exception as e:
            logger.error(f"Batch OCR extraction failed: {e}")
            return {"status": "error", "error": str(e)}

# Factory function for easy module usage
def create_ocr_processor() -> OCRProcessor:
    """Create an OCR processor instance"""
    return OCRProcessor()

# Example usage
if __name__ == "__main__":
    processor = create_ocr_processor()
    
    # Test with sample image
    result = processor.extract_text_from_file("sample_image.jpg")
    print(json.dumps(result, indent=2))
