#!/usr/bin/env python3
"""
Text Processor Node - Advanced Text Processing
Processes text data with various AI models and techniques
"""

import re
import json
from typing import Dict, List, Any, Optional
from datetime import datetime
import logging

try:
    import google.generativeai as genai
    GEMINI_AVAILABLE = True
except ImportError:
    GEMINI_AVAILABLE = False

try:
    from transformers import pipeline
    TRANSFORMERS_AVAILABLE = True
except ImportError:
    TRANSFORMERS_AVAILABLE = False

logger = logging.getLogger(__name__)

class TextProcessorNode:
    """Advanced text processing node for OLAI workflows"""
    
    def __init__(self, config: Dict[str, Any]):
        self.config = config
        self.processor_type = config.get("processor_type", "gemini")
        self.language = config.get("language", "en")
        self.max_length = config.get("max_length", 1000)
        self.temperature = config.get("temperature", 0.7)
        
        # Initialize processors
        self._initialize_processors()
    
    def _initialize_processors(self):
        """Initialize text processing engines"""
        self.processors = {}
        
        if GEMINI_AVAILABLE and self.processor_type == "gemini":
            try:
                genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
                self.processors['gemini'] = genai.GenerativeModel('gemini-2.0-flash-exp')
            except Exception as e:
                logger.error(f"Gemini initialization failed: {e}")
        
        if TRANSFORMERS_AVAILABLE:
            try:
                self.processors['summarizer'] = pipeline("summarization")
                self.processors['sentiment'] = pipeline("sentiment-analysis")
                self.processors['classifier'] = pipeline("text-classification")
            except Exception as e:
                logger.error(f"Transformers initialization failed: {e}")
    
    def process_text(self, input_data: Dict[str, Any]) -> Dict[str, Any]:
        """Process text based on configuration"""
        try:
            text = input_data.get("text", "")
            if not text:
                return {"status": "error", "error": "No text provided"}
            
            processor_type = self.config.get("processor_type", "gemini")
            
            if processor_type == "gemini":
                return self._process_with_gemini(text, input_data)
            elif processor_type == "summarize":
                return self._process_with_summarizer(text)
            elif processor_type == "sentiment":
                return self._process_with_sentiment(text)
            elif processor_type == "classify":
                return self._process_with_classifier(text)
            elif processor_type == "extract_entities":
                return self._extract_entities(text)
            elif processor_type == "translate":
                return self._translate_text(text)
            else:
                return {"status": "error", "error": f"Unknown processor type: {processor_type}"}
                
        except Exception as e:
            logger.error(f"Text processing failed: {e}")
            return {"status": "error", "error": str(e)}
    
    def _process_with_gemini(self, text: str, input_data: Dict[str, Any]) -> Dict[str, Any]:
        """Process text using Gemini"""
        try:
            if 'gemini' not in self.processors:
                return {"status": "error", "error": "Gemini not available"}
            
            prompt = self.config.get("prompt", "Process the following text:")
            task = self.config.get("task", "analyze")
            
            full_prompt = f"{prompt}\n\nText: {text}\n\nTask: {task}"
            
            response = self.processors['gemini'].generate_content(
                full_prompt,
                generation_config=genai.types.GenerationConfig(
                    temperature=self.temperature,
                    max_output_tokens=self.max_length
                )
            )
            
            return {
                "status": "success",
                "processed_text": response.text,
                "original_text": text,
                "processor": "gemini",
                "task": task,
                "timestamp": datetime.now().isoformat()
            }
            
        except Exception as e:
            logger.error(f"Gemini processing failed: {e}")
            return {"status": "error", "error": str(e)}
    
    def _process_with_summarizer(self, text: str) -> Dict[str, Any]:
        """Process text using summarization"""
        try:
            if 'summarizer' not in self.processors:
                return {"status": "error", "error": "Summarizer not available"}
            
            # Truncate text if too long
            if len(text) > 1000:
                text = text[:1000]
            
            result = self.processors['summarizer'](text, max_length=150, min_length=30)
            summary = result[0]['summary_text']
            
            return {
                "status": "success",
                "processed_text": summary,
                "original_text": text,
                "processor": "summarizer",
                "task": "summarize",
                "timestamp": datetime.now().isoformat()
            }
            
        except Exception as e:
            logger.error(f"Summarization failed: {e}")
            return {"status": "error", "error": str(e)}
    
    def _process_with_sentiment(self, text: str) -> Dict[str, Any]:
        """Process text using sentiment analysis"""
        try:
            if 'sentiment' not in self.processors:
                return {"status": "error", "error": "Sentiment analyzer not available"}
            
            result = self.processors['sentiment'](text)
            sentiment = result[0]
            
            return {
                "status": "success",
                "processed_text": f"Sentiment: {sentiment['label']} (Score: {sentiment['score']:.2f})",
                "original_text": text,
                "processor": "sentiment",
                "task": "sentiment_analysis",
                "sentiment_label": sentiment['label'],
                "sentiment_score": sentiment['score'],
                "timestamp": datetime.now().isoformat()
            }
            
        except Exception as e:
            logger.error(f"Sentiment analysis failed: {e}")
            return {"status": "error", "error": str(e)}
    
    def _process_with_classifier(self, text: str) -> Dict[str, Any]:
        """Process text using classification"""
        try:
            if 'classifier' not in self.processors:
                return {"status": "error", "error": "Classifier not available"}
            
            result = self.processors['classifier'](text)
            classification = result[0]
            
            return {
                "status": "success",
                "processed_text": f"Classification: {classification['label']} (Score: {classification['score']:.2f})",
                "original_text": text,
                "processor": "classifier",
                "task": "classification",
                "classification_label": classification['label'],
                "classification_score": classification['score'],
                "timestamp": datetime.now().isoformat()
            }
            
        except Exception as e:
            logger.error(f"Classification failed: {e}")
            return {"status": "error", "error": str(e)}
    
    def _extract_entities(self, text: str) -> Dict[str, Any]:
        """Extract entities from text using regex patterns"""
        try:
            # Simple entity extraction patterns
            email_pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
            phone_pattern = r'\b\d{3}-\d{3}-\d{4}\b'
            url_pattern = r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\\(\\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+'
            date_pattern = r'\b\d{1,2}/\d{1,2}/\d{4}\b'
            
            entities = {
                'emails': re.findall(email_pattern, text),
                'phones': re.findall(phone_pattern, text),
                'urls': re.findall(url_pattern, text),
                'dates': re.findall(date_pattern, text)
            }
            
            # Count total entities
            total_entities = sum(len(entity_list) for entity_list in entities.values())
            
            return {
                "status": "success",
                "processed_text": f"Extracted {total_entities} entities from text",
                "original_text": text,
                "processor": "entity_extractor",
                "task": "extract_entities",
                "entities": entities,
                "total_entities": total_entities,
                "timestamp": datetime.now().isoformat()
            }
            
        except Exception as e:
            logger.error(f"Entity extraction failed: {e}")
            return {"status": "error", "error": str(e)}
    
    def _translate_text(self, text: str) -> Dict[str, Any]:
        """Translate text using Gemini"""
        try:
            if 'gemini' not in self.processors:
                return {"status": "error", "error": "Gemini not available for translation"}
            
            target_language = self.config.get("target_language", "Spanish")
            prompt = f"Translate the following text to {target_language}:\n\n{text}"
            
            response = self.processors['gemini'].generate_content(prompt)
            
            return {
                "status": "success",
                "processed_text": response.text,
                "original_text": text,
                "processor": "gemini_translator",
                "task": "translate",
                "target_language": target_language,
                "timestamp": datetime.now().isoformat()
            }
            
        except Exception as e:
            logger.error(f"Translation failed: {e}")
            return {"status": "error", "error": str(e)}

# Factory function for easy module usage
def create_text_processor_node(config: Dict[str, Any]) -> TextProcessorNode:
    """Create a text processor node instance"""
    return TextProcessorNode(config)

# Example usage
if __name__ == "__main__":
    config = {
        "processor_type": "gemini",
        "task": "analyze",
        "prompt": "Analyze the sentiment and key points of this text:"
    }
    
    node = create_text_processor_node(config)
    
    # Test with sample text
    input_data = {"text": "This is a sample text for processing."}
    result = node.process_text(input_data)
    print(json.dumps(result, indent=2))
