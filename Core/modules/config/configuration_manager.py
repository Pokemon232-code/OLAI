#!/usr/bin/env python3
"""
Configuration Manager - Dynamic Configuration System
Manages dynamic configuration for OLAI modules and applications
"""

import os
import json
import yaml
import toml
from typing import Dict, List, Any, Optional, Union
from datetime import datetime
import logging
import threading
import asyncio
from pathlib import Path
import uuid
from dataclasses import dataclass, asdict
from enum import Enum

logger = logging.getLogger(__name__)

class ConfigFormat(Enum):
    """Configuration file formats"""
    JSON = "json"
    YAML = "yaml"
    TOML = "toml"
    ENV = "env"

class ConfigScope(Enum):
    """Configuration scopes"""
    GLOBAL = "global"
    PROJECT = "project"
    USER = "user"
    MODULE = "module"
    SESSION = "session"

@dataclass
class ConfigItem:
    """Configuration item"""
    key: str
    value: Any
    scope: ConfigScope
    description: str = ""
    default_value: Any = None
    data_type: str = "string"
    required: bool = False
    validation_rules: Dict[str, Any] = None
    created_at: str = ""
    updated_at: str = ""

class ConfigurationManager:
    """Advanced configuration management system for OLAI"""
    
    def __init__(self, config_dir: str = "config"):
        self.config_dir = Path(config_dir)
        self.config_dir.mkdir(exist_ok=True)
        
        # Configuration storage
        self.configs: Dict[str, Dict[str, ConfigItem]] = {}
        self.config_files: Dict[str, Path] = {}
        self.config_watchers: Dict[str, Any] = {}
        
        # Thread safety
        self.lock = threading.Lock()
        
        # Configuration templates
        self.templates: Dict[str, Dict[str, Any]] = {}
        
        # Initialize default configurations
        self._initialize_default_configs()
    
    def _initialize_default_configs(self):
        """Initialize default configurations"""
        # Global OLAI configuration
        self._create_default_config("olai_global", {
            "api": {
                "host": "0.0.0.0",
                "port": 8000,
                "cors_origins": ["*"],
                "rate_limit": 1000
            },
            "database": {
                "type": "sqlite",
                "path": "olai.db",
                "pool_size": 10
            },
            "ai": {
                "gemini_api_key": "",
                "openai_api_key": "",
                "huggingface_token": "",
                "default_model": "gemini-2.0-flash-exp"
            },
            "storage": {
                "base_path": "storage",
                "max_file_size": 100 * 1024 * 1024,  # 100MB
                "allowed_types": ["image", "video", "audio", "document"]
            },
            "security": {
                "jwt_secret": "",
                "session_timeout": 3600,
                "password_min_length": 8
            },
            "logging": {
                "level": "INFO",
                "format": "%(asctime)s - %(name)s - %(levelname)s - %(message)s",
                "file": "olai.log"
            }
        })
        
        # Hardware configuration
        self._create_default_config("hardware", {
            "camera": {
                "default_device": 0,
                "resolution": "auto",
                "fps": 30,
                "auto_focus": True
            },
            "microphone": {
                "default_device": 0,
                "sample_rate": 16000,
                "channels": 1,
                "chunk_size": 1024
            },
            "gpu": {
                "enabled": True,
                "memory_limit": 0,  # 0 = no limit
                "auto_optimize": True
            },
            "sensors": {
                "temperature": True,
                "humidity": True,
                "pressure": True,
                "motion": True
            }
        })
        
        # AI services configuration
        self._create_default_config("ai_services", {
            "ocr": {
                "default_engine": "auto",
                "languages": ["en"],
                "confidence_threshold": 0.7
            },
            "speech_to_text": {
                "default_engine": "auto",
                "language": "en",
                "real_time": True
            },
            "text_processing": {
                "default_model": "gemini",
                "max_tokens": 1000,
                "temperature": 0.7
            },
            "vision": {
                "object_detection": True,
                "face_recognition": True,
                "scene_analysis": True
            }
        })
        
        # Workflow configuration
        self._create_default_config("workflow", {
            "execution": {
                "max_concurrent": 10,
                "timeout": 300,  # 5 minutes
                "retry_attempts": 3
            },
            "nodes": {
                "default_timeout": 30,
                "memory_limit": 512 * 1024 * 1024,  # 512MB
                "cpu_limit": 1.0
            },
            "storage": {
                "temp_path": "temp",
                "max_temp_size": 1024 * 1024 * 1024,  # 1GB
                "cleanup_interval": 3600  # 1 hour
            }
        })
    
    def _create_default_config(self, config_name: str, config_data: Dict[str, Any]):
        """Create default configuration"""
        self.configs[config_name] = {}
        
        for key, value in config_data.items():
            if isinstance(value, dict):
                # Nested configuration
                for sub_key, sub_value in value.items():
                    full_key = f"{key}.{sub_key}"
                    config_item = ConfigItem(
                        key=full_key,
                        value=sub_value,
                        scope=ConfigScope.GLOBAL,
                        description=f"Default {config_name} configuration for {full_key}",
                        default_value=sub_value,
                        created_at=datetime.now().isoformat(),
                        updated_at=datetime.now().isoformat()
                    )
                    self.configs[config_name][full_key] = config_item
            else:
                # Simple configuration
                config_item = ConfigItem(
                    key=key,
                    value=value,
                    scope=ConfigScope.GLOBAL,
                    description=f"Default {config_name} configuration for {key}",
                    default_value=value,
                    created_at=datetime.now().isoformat(),
                    updated_at=datetime.now().isoformat()
                )
                self.configs[config_name][key] = config_item
    
    def get_config(self, config_name: str, key: str = None, scope: ConfigScope = ConfigScope.GLOBAL) -> Any:
        """Get configuration value"""
        try:
            with self.lock:
                if config_name not in self.configs:
                    return None
                
                if key is None:
                    # Return all configurations for the scope
                    return {
                        k: v.value for k, v in self.configs[config_name].items()
                        if v.scope == scope
                    }
                
                if key in self.configs[config_name]:
                    config_item = self.configs[config_name][key]
                    return config_item.value
                
                return None
        except Exception as e:
            logger.error(f"Error getting config {config_name}.{key}: {e}")
            return None
    
    def set_config(self, config_name: str, key: str, value: Any, 
                   scope: ConfigScope = ConfigScope.GLOBAL, description: str = "") -> bool:
        """Set configuration value"""
        try:
            with self.lock:
                if config_name not in self.configs:
                    self.configs[config_name] = {}
                
                if key in self.configs[config_name]:
                    # Update existing configuration
                    config_item = self.configs[config_name][key]
                    config_item.value = value
                    config_item.scope = scope
                    config_item.updated_at = datetime.now().isoformat()
                    if description:
                        config_item.description = description
                else:
                    # Create new configuration
                    config_item = ConfigItem(
                        key=key,
                        value=value,
                        scope=scope,
                        description=description,
                        default_value=value,
                        created_at=datetime.now().isoformat(),
                        updated_at=datetime.now().isoformat()
                    )
                    self.configs[config_name][key] = config_item
                
                return True
        except Exception as e:
            logger.error(f"Error setting config {config_name}.{key}: {e}")
            return False
    
    def delete_config(self, config_name: str, key: str) -> bool:
        """Delete configuration"""
        try:
            with self.lock:
                if config_name in self.configs and key in self.configs[config_name]:
                    del self.configs[config_name][key]
                    return True
                return False
        except Exception as e:
            logger.error(f"Error deleting config {config_name}.{key}: {e}")
            return False
    
    def load_config_from_file(self, config_name: str, file_path: str, 
                             format: ConfigFormat = ConfigFormat.JSON) -> bool:
        """Load configuration from file"""
        try:
            file_path = Path(file_path)
            if not file_path.exists():
                return False
            
            with open(file_path, 'r', encoding='utf-8') as f:
                if format == ConfigFormat.JSON:
                    data = json.load(f)
                elif format == ConfigFormat.YAML:
                    data = yaml.safe_load(f)
                elif format == ConfigFormat.TOML:
                    data = toml.load(f)
                else:
                    return False
            
            # Store file path
            self.config_files[config_name] = file_path
            
            # Load configuration data
            self._load_config_data(config_name, data)
            
            return True
        except Exception as e:
            logger.error(f"Error loading config from file {file_path}: {e}")
            return False
    
    def save_config_to_file(self, config_name: str, file_path: str = None, 
                           format: ConfigFormat = ConfigFormat.JSON) -> bool:
        """Save configuration to file"""
        try:
            if config_name not in self.configs:
                return False
            
            if file_path is None:
                file_path = self.config_dir / f"{config_name}.{format.value}"
            else:
                file_path = Path(file_path)
            
            # Convert configuration to dictionary
            config_data = {}
            for key, config_item in self.configs[config_name].items():
                self._set_nested_value(config_data, key, config_item.value)
            
            # Save to file
            with open(file_path, 'w', encoding='utf-8') as f:
                if format == ConfigFormat.JSON:
                    json.dump(config_data, f, indent=2)
                elif format == ConfigFormat.YAML:
                    yaml.dump(config_data, f, default_flow_style=False)
                elif format == ConfigFormat.TOML:
                    toml.dump(config_data, f)
            
            # Store file path
            self.config_files[config_name] = file_path
            
            return True
        except Exception as e:
            logger.error(f"Error saving config to file {file_path}: {e}")
            return False
    
    def _load_config_data(self, config_name: str, data: Dict[str, Any], prefix: str = ""):
        """Load configuration data recursively"""
        if config_name not in self.configs:
            self.configs[config_name] = {}
        
        for key, value in data.items():
            full_key = f"{prefix}.{key}" if prefix else key
            
            if isinstance(value, dict):
                self._load_config_data(config_name, value, full_key)
            else:
                config_item = ConfigItem(
                    key=full_key,
                    value=value,
                    scope=ConfigScope.GLOBAL,
                    description=f"Loaded from file",
                    default_value=value,
                    created_at=datetime.now().isoformat(),
                    updated_at=datetime.now().isoformat()
                )
                self.configs[config_name][full_key] = config_item
    
    def _set_nested_value(self, data: Dict[str, Any], key: str, value: Any):
        """Set nested value in dictionary"""
        keys = key.split('.')
        current = data
        
        for k in keys[:-1]:
            if k not in current:
                current[k] = {}
            current = current[k]
        
        current[keys[-1]] = value
    
    def create_project_config(self, project_id: str, project_config: Dict[str, Any]) -> bool:
        """Create project-specific configuration"""
        try:
            config_name = f"project_{project_id}"
            self.configs[config_name] = {}
            
            for key, value in project_config.items():
                config_item = ConfigItem(
                    key=key,
                    value=value,
                    scope=ConfigScope.PROJECT,
                    description=f"Project {project_id} configuration",
                    default_value=value,
                    created_at=datetime.now().isoformat(),
                    updated_at=datetime.now().isoformat()
                )
                self.configs[config_name][key] = config_item
            
            return True
        except Exception as e:
            logger.error(f"Error creating project config: {e}")
            return False
    
    def create_user_config(self, user_id: str, user_config: Dict[str, Any]) -> bool:
        """Create user-specific configuration"""
        try:
            config_name = f"user_{user_id}"
            self.configs[config_name] = {}
            
            for key, value in user_config.items():
                config_item = ConfigItem(
                    key=key,
                    value=value,
                    scope=ConfigScope.USER,
                    description=f"User {user_id} configuration",
                    default_value=value,
                    created_at=datetime.now().isoformat(),
                    updated_at=datetime.now().isoformat()
                )
                self.configs[config_name][key] = config_item
            
            return True
        except Exception as e:
            logger.error(f"Error creating user config: {e}")
            return False
    
    def merge_configs(self, config_name: str, override_config: Dict[str, Any]) -> bool:
        """Merge configuration with override values"""
        try:
            if config_name not in self.configs:
                return False
            
            for key, value in override_config.items():
                if key in self.configs[config_name]:
                    self.configs[config_name][key].value = value
                    self.configs[config_name][key].updated_at = datetime.now().isoformat()
                else:
                    config_item = ConfigItem(
                        key=key,
                        value=value,
                        scope=ConfigScope.GLOBAL,
                        description="Merged configuration",
                        default_value=value,
                        created_at=datetime.now().isoformat(),
                        updated_at=datetime.now().isoformat()
                    )
                    self.configs[config_name][key] = config_item
            
            return True
        except Exception as e:
            logger.error(f"Error merging configs: {e}")
            return False
    
    def validate_config(self, config_name: str) -> Dict[str, Any]:
        """Validate configuration"""
        try:
            if config_name not in self.configs:
                return {"status": "error", "error": "Configuration not found"}
            
            validation_result = {
                "status": "success",
                "valid": True,
                "errors": [],
                "warnings": []
            }
            
            for key, config_item in self.configs[config_name].items():
                # Check required fields
                if config_item.required and config_item.value is None:
                    validation_result["errors"].append(f"Required field {key} is missing")
                    validation_result["valid"] = False
                
                # Check data type
                if config_item.data_type and not self._validate_data_type(config_item.value, config_item.data_type):
                    validation_result["errors"].append(f"Field {key} has invalid data type")
                    validation_result["valid"] = False
                
                # Check validation rules
                if config_item.validation_rules:
                    for rule, rule_value in config_item.validation_rules.items():
                        if not self._validate_rule(config_item.value, rule, rule_value):
                            validation_result["errors"].append(f"Field {key} failed validation rule {rule}")
                            validation_result["valid"] = False
            
            return validation_result
        except Exception as e:
            logger.error(f"Error validating config: {e}")
            return {"status": "error", "error": str(e)}
    
    def _validate_data_type(self, value: Any, data_type: str) -> bool:
        """Validate data type"""
        try:
            if data_type == "string":
                return isinstance(value, str)
            elif data_type == "integer":
                return isinstance(value, int)
            elif data_type == "float":
                return isinstance(value, float)
            elif data_type == "boolean":
                return isinstance(value, bool)
            elif data_type == "list":
                return isinstance(value, list)
            elif data_type == "dict":
                return isinstance(value, dict)
            return True
        except:
            return False
    
    def _validate_rule(self, value: Any, rule: str, rule_value: Any) -> bool:
        """Validate rule"""
        try:
            if rule == "min_length" and isinstance(value, str):
                return len(value) >= rule_value
            elif rule == "max_length" and isinstance(value, str):
                return len(value) <= rule_value
            elif rule == "min_value" and isinstance(value, (int, float)):
                return value >= rule_value
            elif rule == "max_value" and isinstance(value, (int, float)):
                return value <= rule_value
            elif rule == "pattern" and isinstance(value, str):
                import re
                return re.match(rule_value, value) is not None
            return True
        except:
            return False
    
    def get_config_summary(self) -> Dict[str, Any]:
        """Get configuration summary"""
        try:
            summary = {
                "total_configs": len(self.configs),
                "config_names": list(self.configs.keys()),
                "total_items": sum(len(config) for config in self.configs.values()),
                "scopes": {
                    scope.value: sum(
                        1 for config in self.configs.values()
                        for item in config.values()
                        if item.scope == scope
                    )
                    for scope in ConfigScope
                },
                "timestamp": datetime.now().isoformat()
            }
            return summary
        except Exception as e:
            logger.error(f"Error getting config summary: {e}")
            return {"status": "error", "error": str(e)}

# Factory function
def create_configuration_manager(config_dir: str = "config") -> ConfigurationManager:
    """Create a configuration manager instance"""
    return ConfigurationManager(config_dir)

# Example usage
if __name__ == "__main__":
    manager = create_configuration_manager()
    print("Configuration Manager created successfully")
