"""
Model Orchestrator - Advanced Model Chaining and Integration
Handles model chaining, linking, and seamless integration between components
"""

import json
import os
import asyncio
import threading
import queue
import time
from typing import Dict, Any, List, Optional, Callable, Union
from datetime import datetime
import uuid
from dataclasses import dataclass, asdict
from enum import Enum
import logging

class ModelStatus(Enum):
    IDLE = "idle"
    LOADING = "loading"
    READY = "ready"
    PROCESSING = "processing"
    ERROR = "error"
    CHAINING = "chaining"

class DataType(Enum):
    TEXT = "text"
    IMAGE = "image"
    AUDIO = "audio"
    VIDEO = "video"
    JSON = "json"
    TENSOR = "tensor"
    BINARY = "binary"

@dataclass
class ModelNode:
    """Represents a model in the orchestration chain"""
    id: str
    name: str
    model_id: str
    platform: str
    input_types: List[DataType]
    output_types: List[DataType]
    status: ModelStatus
    config: Dict[str, Any]
    dependencies: List[str]
    position: Dict[str, int]
    created_at: str

@dataclass
class ModelConnection:
    """Represents a connection between models"""
    id: str
    source_node: str
    target_node: str
    data_type: DataType
    transformation: Optional[Dict[str, Any]]
    created_at: str

@dataclass
class ProcessingResult:
    """Result from model processing"""
    node_id: str
    success: bool
    data: Any
    data_type: DataType
    metadata: Dict[str, Any]
    processing_time: float
    timestamp: str

class ModelOrchestrator:
    """
    Advanced model orchestration system with chaining capabilities
    - Model chaining and pipeline management
    - Automatic data transformation between models
    - Real-time processing and monitoring
    - Seamless backend/frontend integration
    """
    
    def __init__(self):
        self.models = {}  # ModelNode instances
        self.connections = {}  # ModelConnection instances
        self.processing_queue = queue.Queue()
        self.results_cache = {}
        self.active_chains = {}
        self.model_instances = {}
        self.data_transformers = {}
        self.status_callbacks = {}
        self.logger = self._setup_logger()
        
        # Processing threads
        self.processing_thread = None
        self.monitoring_thread = None
        self.running = False
        
        # Performance metrics
        self.metrics = {
            "total_requests": 0,
            "successful_requests": 0,
            "failed_requests": 0,
            "average_processing_time": 0.0,
            "models_loaded": 0,
            "active_chains": 0
        }
    
    def initialize(self, config: Dict[str, Any] = None):
        """Initialize model orchestrator"""
        try:
            # Start processing threads
            self.running = True
            self.processing_thread = threading.Thread(target=self._processing_worker)
            self.monitoring_thread = threading.Thread(target=self._monitoring_worker)
            
            self.processing_thread.start()
            self.monitoring_thread.start()
            
            self.logger.info("Model orchestrator initialized successfully")
            return True
            
        except Exception as e:
            self.logger.error(f"Failed to initialize orchestrator: {e}")
            return False
    
    def create_model_chain(self,
                          chain_name: str,
                          models: List[Dict[str, Any]],
                          connections: List[Dict[str, Any]] = None,
                          config: Dict[str, Any] = None) -> Dict[str, Any]:
        """
        Create a model chain with automatic linking
        - chain_name: Name of the model chain
        - models: List of model configurations
        - connections: List of connections between models
        - config: Chain configuration
        """
        
        try:
            chain_id = str(uuid.uuid4())
            
            # Create model nodes
            model_nodes = []
            for i, model_config in enumerate(models):
                node = ModelNode(
                    id=str(uuid.uuid4()),
                    name=model_config.get("name", f"model_{i}"),
                    model_id=model_config.get("model_id", ""),
                    platform=model_config.get("platform", "huggingface"),
                    input_types=[DataType(t) for t in model_config.get("input_types", ["text"])],
                    output_types=[DataType(t) for t in model_config.get("output_types", ["text"])],
                    status=ModelStatus.IDLE,
                    config=model_config.get("config", {}),
                    dependencies=model_config.get("dependencies", []),
                    position=model_config.get("position", {"x": i * 200, "y": 100}),
                    created_at=datetime.now().isoformat()
                )
                
                self.models[node.id] = node
                model_nodes.append(node)
            
            # Create connections (auto-generate if not provided)
            if not connections:
                connections = self._auto_generate_connections(model_nodes)
            
            connection_objects = []
            for conn_config in connections:
                connection = ModelConnection(
                    id=str(uuid.uuid4()),
                    source_node=conn_config["source_node"],
                    target_node=conn_config["target_node"],
                    data_type=DataType(conn_config.get("data_type", "text")),
                    transformation=conn_config.get("transformation"),
                    created_at=datetime.now().isoformat()
                )
                
                self.connections[connection.id] = connection
                connection_objects.append(connection)
            
            # Create chain configuration
            chain_config = {
                "id": chain_id,
                "name": chain_name,
                "models": [node.id for node in model_nodes],
                "connections": [conn.id for conn in connection_objects],
                "config": config or {},
                "created_at": datetime.now().isoformat(),
                "status": "created"
            }
            
            self.active_chains[chain_id] = chain_config
            
            self.logger.info(f"Created model chain '{chain_name}' with {len(model_nodes)} models")
            
            return {
                "success": True,
                "chain_id": chain_id,
                "chain_name": chain_name,
                "models": [asdict(node) for node in model_nodes],
                "connections": [asdict(conn) for conn in connection_objects],
                "config": chain_config
            }
            
        except Exception as e:
            self.logger.error(f"Failed to create model chain: {e}")
            return {"success": False, "error": str(e)}
    
    def load_chain_models(self, chain_id: str) -> Dict[str, Any]:
        """Load all models in a chain"""
        try:
            if chain_id not in self.active_chains:
                return {"success": False, "error": "Chain not found"}
            
            chain = self.active_chains[chain_id]
            loaded_models = []
            failed_models = []
            
            for model_id in chain["models"]:
                if model_id in self.models:
                    model_node = self.models[model_id]
                    
                    # Load model
                    load_result = self._load_model_instance(model_node)
                    if load_result["success"]:
                        model_node.status = ModelStatus.READY
                        loaded_models.append(model_node.name)
                        self.metrics["models_loaded"] += 1
                    else:
                        model_node.status = ModelStatus.ERROR
                        failed_models.append({
                            "name": model_node.name,
                            "error": load_result["error"]
                        })
            
            # Update chain status
            if failed_models:
                chain["status"] = "partial"
            else:
                chain["status"] = "ready"
            
            return {
                "success": True,
                "chain_id": chain_id,
                "loaded_models": loaded_models,
                "failed_models": failed_models,
                "chain_status": chain["status"]
            }
            
        except Exception as e:
            self.logger.error(f"Failed to load chain models: {e}")
            return {"success": False, "error": str(e)}
    
    def execute_chain(self,
                     chain_id: str,
                     input_data: Any,
                     input_type: DataType = DataType.TEXT,
                     callback: Callable = None) -> Dict[str, Any]:
        """
        Execute a model chain with input data
        - chain_id: ID of the chain to execute
        - input_data: Input data for the chain
        - input_type: Type of input data
        - callback: Optional callback for real-time updates
        """
        
        try:
            if chain_id not in self.active_chains:
                return {"success": False, "error": "Chain not found"}
            
            chain = self.active_chains[chain_id]
            if chain["status"] != "ready":
                return {"success": False, "error": f"Chain not ready: {chain['status']}"}
            
            # Create execution context
            execution_id = str(uuid.uuid4())
            execution_context = {
                "id": execution_id,
                "chain_id": chain_id,
                "input_data": input_data,
                "input_type": input_type,
                "callback": callback,
                "start_time": time.time(),
                "current_node": None,
                "results": {},
                "status": "running"
            }
            
            # Add to processing queue
            self.processing_queue.put(execution_context)
            self.metrics["total_requests"] += 1
            
            return {
                "success": True,
                "execution_id": execution_id,
                "chain_id": chain_id,
                "status": "queued"
            }
            
        except Exception as e:
            self.logger.error(f"Failed to execute chain: {e}")
            return {"success": False, "error": str(e)}
    
    def get_chain_status(self, chain_id: str) -> Dict[str, Any]:
        """Get status of a model chain"""
        try:
            if chain_id not in self.active_chains:
                return {"success": False, "error": "Chain not found"}
            
            chain = self.active_chains[chain_id]
            
            # Get model statuses
            model_statuses = {}
            for model_id in chain["models"]:
                if model_id in self.models:
                    model = self.models[model_id]
                    model_statuses[model.name] = {
                        "status": model.status.value,
                        "loaded": model_id in self.model_instances
                    }
            
            return {
                "success": True,
                "chain_id": chain_id,
                "chain_name": chain["name"],
                "status": chain["status"],
                "models": model_statuses,
                "connections": len(chain["connections"]),
                "created_at": chain["created_at"]
            }
            
        except Exception as e:
            return {"success": False, "error": str(e)}
    
    def add_model_to_chain(self,
                          chain_id: str,
                          model_config: Dict[str, Any],
                          connections: List[Dict[str, Any]] = None) -> Dict[str, Any]:
        """Add a new model to an existing chain"""
        try:
            if chain_id not in self.active_chains:
                return {"success": False, "error": "Chain not found"}
            
            chain = self.active_chains[chain_id]
            
            # Create new model node
            node = ModelNode(
                id=str(uuid.uuid4()),
                name=model_config.get("name", f"model_{len(chain['models'])}"),
                model_id=model_config.get("model_id", ""),
                platform=model_config.get("platform", "huggingface"),
                input_types=[DataType(t) for t in model_config.get("input_types", ["text"])],
                output_types=[DataType(t) for t in model_config.get("output_types", ["text"])],
                status=ModelStatus.IDLE,
                config=model_config.get("config", {}),
                dependencies=model_config.get("dependencies", []),
                position=model_config.get("position", {"x": len(chain["models"]) * 200, "y": 100}),
                created_at=datetime.now().isoformat()
            )
            
            self.models[node.id] = node
            chain["models"].append(node.id)
            
            # Add connections
            if connections:
                for conn_config in connections:
                    connection = ModelConnection(
                        id=str(uuid.uuid4()),
                        source_node=conn_config["source_node"],
                        target_node=conn_config["target_node"],
                        data_type=DataType(conn_config.get("data_type", "text")),
                        transformation=conn_config.get("transformation"),
                        created_at=datetime.now().isoformat()
                    )
                    
                    self.connections[connection.id] = connection
                    chain["connections"].append(connection.id)
            
            return {
                "success": True,
                "chain_id": chain_id,
                "model_id": node.id,
                "model_name": node.name,
                "chain_models": len(chain["models"])
            }
            
        except Exception as e:
            return {"success": False, "error": str(e)}
    
    def remove_model_from_chain(self, chain_id: str, model_id: str) -> Dict[str, Any]:
        """Remove a model from a chain"""
        try:
            if chain_id not in self.active_chains:
                return {"success": False, "error": "Chain not found"}
            
            chain = self.active_chains[chain_id]
            
            if model_id not in chain["models"]:
                return {"success": False, "error": "Model not in chain"}
            
            # Remove model from chain
            chain["models"].remove(model_id)
            
            # Remove related connections
            connections_to_remove = []
            for conn_id in chain["connections"]:
                if conn_id in self.connections:
                    conn = self.connections[conn_id]
                    if conn.source_node == model_id or conn.target_node == model_id:
                        connections_to_remove.append(conn_id)
            
            for conn_id in connections_to_remove:
                chain["connections"].remove(conn_id)
                del self.connections[conn_id]
            
            # Unload model instance if loaded
            if model_id in self.model_instances:
                del self.model_instances[model_id]
            
            # Remove model node
            if model_id in self.models:
                del self.models[model_id]
            
            return {
                "success": True,
                "chain_id": chain_id,
                "removed_model": model_id,
                "remaining_models": len(chain["models"])
            }
            
        except Exception as e:
            return {"success": False, "error": str(e)}
    
    def get_chain_results(self, chain_id: str, execution_id: str = None) -> Dict[str, Any]:
        """Get results from chain execution"""
        try:
            if execution_id:
                # Get specific execution results
                if execution_id in self.results_cache:
                    return {
                        "success": True,
                        "execution_id": execution_id,
                        "results": self.results_cache[execution_id]
                    }
                else:
                    return {"success": False, "error": "Execution not found"}
            else:
                # Get all results for chain
                chain_results = {}
                for exec_id, results in self.results_cache.items():
                    if results.get("chain_id") == chain_id:
                        chain_results[exec_id] = results
                
                return {
                    "success": True,
                    "chain_id": chain_id,
                    "results": chain_results
                }
                
        except Exception as e:
            return {"success": False, "error": str(e)}
    
    def export_chain(self, chain_id: str, export_path: str = None) -> Dict[str, Any]:
        """Export chain configuration"""
        try:
            if chain_id not in self.active_chains:
                return {"success": False, "error": "Chain not found"}
            
            chain = self.active_chains[chain_id]
            
            # Prepare export data
            export_data = {
                "chain": chain,
                "models": {model_id: asdict(self.models[model_id]) 
                          for model_id in chain["models"] 
                          if model_id in self.models},
                "connections": {conn_id: asdict(self.connections[conn_id]) 
                              for conn_id in chain["connections"] 
                              if conn_id in self.connections},
                "exported_at": datetime.now().isoformat(),
                "version": "1.0.0"
            }
            
            if export_path is None:
                export_path = f"chain_{chain['name']}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
            
            with open(export_path, 'w') as f:
                json.dump(export_data, f, indent=2, default=str)
            
            return {
                "success": True,
                "chain_id": chain_id,
                "export_path": export_path,
                "export_data": export_data
            }
            
        except Exception as e:
            return {"success": False, "error": str(e)}
    
    def get_orchestrator_metrics(self) -> Dict[str, Any]:
        """Get orchestrator performance metrics"""
        return {
            "success": True,
            "metrics": self.metrics.copy(),
            "active_chains": len(self.active_chains),
            "loaded_models": len(self.model_instances),
            "total_models": len(self.models),
            "total_connections": len(self.connections),
            "queue_size": self.processing_queue.qsize()
        }
    
    def shutdown(self):
        """Shutdown orchestrator and cleanup resources"""
        try:
            self.running = False
            
            # Wait for threads to finish
            if self.processing_thread:
                self.processing_thread.join(timeout=5)
            if self.monitoring_thread:
                self.monitoring_thread.join(timeout=5)
            
            # Clear model instances
            self.model_instances.clear()
            
            self.logger.info("Model orchestrator shutdown complete")
            
        except Exception as e:
            self.logger.error(f"Error during shutdown: {e}")
    
    # Private helper methods
    
    def _setup_logger(self) -> logging.Logger:
        """Setup logging for orchestrator"""
        logger = logging.getLogger("ModelOrchestrator")
        logger.setLevel(logging.INFO)
        
        if not logger.handlers:
            handler = logging.StreamHandler()
            formatter = logging.Formatter(
                '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
            )
            handler.setFormatter(formatter)
            logger.addHandler(handler)
        
        return logger
    
    def _auto_generate_connections(self, model_nodes: List[ModelNode]) -> List[Dict[str, Any]]:
        """Auto-generate connections between model nodes"""
        connections = []
        
        for i in range(len(model_nodes) - 1):
            source_node = model_nodes[i]
            target_node = model_nodes[i + 1]
            
            # Find compatible data types
            compatible_types = set(source_node.output_types) & set(target_node.input_types)
            if compatible_types:
                data_type = list(compatible_types)[0].value
            else:
                data_type = "text"  # Default fallback
            
            connection = {
                "source_node": source_node.id,
                "target_node": target_node.id,
                "data_type": data_type,
                "transformation": None
            }
            connections.append(connection)
        
        return connections
    
    def _load_model_instance(self, model_node: ModelNode) -> Dict[str, Any]:
        """Load a model instance"""
        try:
            model_node.status = ModelStatus.LOADING
            
            # This would integrate with the model discovery service
            # For now, create a placeholder model instance
            model_instance = {
                "id": model_node.id,
                "name": model_node.name,
                "model_id": model_node.model_id,
                "platform": model_node.platform,
                "config": model_node.config,
                "loaded_at": datetime.now().isoformat()
            }
            
            self.model_instances[model_node.id] = model_instance
            model_node.status = ModelStatus.READY
            
            return {"success": True, "model_instance": model_instance}
            
        except Exception as e:
            model_node.status = ModelStatus.ERROR
            return {"success": False, "error": str(e)}
    
    def _processing_worker(self):
        """Worker thread for processing model chains"""
        while self.running:
            try:
                # Get execution context from queue
                execution_context = self.processing_queue.get(timeout=1)
                
                # Process the chain
                result = self._process_chain(execution_context)
                
                # Store results
                self.results_cache[execution_context["id"]] = result
                
                # Call callback if provided
                if execution_context.get("callback"):
                    execution_context["callback"](result)
                
                self.processing_queue.task_done()
                
            except queue.Empty:
                continue
            except Exception as e:
                self.logger.error(f"Error in processing worker: {e}")
    
    def _monitoring_worker(self):
        """Worker thread for monitoring orchestrator health"""
        while self.running:
            try:
                # Update metrics
                self.metrics["active_chains"] = len(self.active_chains)
                
                # Check for stuck models
                for model_id, model in self.models.items():
                    if model.status == ModelStatus.PROCESSING:
                        # Check if model has been processing too long
                        # This would implement timeout logic
                        pass
                
                time.sleep(5)  # Monitor every 5 seconds
                
            except Exception as e:
                self.logger.error(f"Error in monitoring worker: {e}")
    
    def _process_chain(self, execution_context: Dict[str, Any]) -> Dict[str, Any]:
        """Process a model chain execution"""
        try:
            chain_id = execution_context["chain_id"]
            chain = self.active_chains[chain_id]
            
            # Get chain models in execution order
            execution_order = self._get_execution_order(chain)
            
            current_data = execution_context["input_data"]
            current_type = execution_context["input_type"]
            results = {}
            
            for model_id in execution_order:
                if model_id in self.models:
                    model_node = self.models[model_id]
                    
                    # Process with model
                    start_time = time.time()
                    result = self._process_with_model(model_node, current_data, current_type)
                    processing_time = time.time() - start_time
                    
                    if result["success"]:
                        current_data = result["data"]
                        current_type = result["data_type"]
                        
                        results[model_id] = ProcessingResult(
                            node_id=model_id,
                            success=True,
                            data=current_data,
                            data_type=current_type,
                            metadata=result.get("metadata", {}),
                            processing_time=processing_time,
                            timestamp=datetime.now().isoformat()
                        )
                    else:
                        results[model_id] = ProcessingResult(
                            node_id=model_id,
                            success=False,
                            data=None,
                            data_type=current_type,
                            metadata={"error": result["error"]},
                            processing_time=processing_time,
                            timestamp=datetime.now().isoformat()
                        )
                        
                        # Stop processing on error
                        break
            
            # Calculate total processing time
            total_time = time.time() - execution_context["start_time"]
            
            return {
                "execution_id": execution_context["id"],
                "chain_id": chain_id,
                "success": all(r.success for r in results.values()),
                "results": {r.node_id: asdict(r) for r in results.values()},
                "total_processing_time": total_time,
                "completed_at": datetime.now().isoformat()
            }
            
        except Exception as e:
            return {
                "execution_id": execution_context["id"],
                "chain_id": execution_context["chain_id"],
                "success": False,
                "error": str(e),
                "completed_at": datetime.now().isoformat()
            }
    
    def _get_execution_order(self, chain: Dict[str, Any]) -> List[str]:
        """Get execution order for chain models"""
        # Simple linear execution for now
        # In a more advanced implementation, this would use topological sorting
        return chain["models"]
    
    def _process_with_model(self, model_node: ModelNode, data: Any, data_type: DataType) -> Dict[str, Any]:
        """Process data with a specific model"""
        try:
            model_node.status = ModelStatus.PROCESSING
            
            # This would integrate with actual model inference
            # For now, return a placeholder result
            result = {
                "success": True,
                "data": f"Processed by {model_node.name}: {data}",
                "data_type": data_type,
                "metadata": {
                    "model_name": model_node.name,
                    "model_id": model_node.model_id,
                    "processing_time": 0.1
                }
            }
            
            model_node.status = ModelStatus.READY
            return result
            
        except Exception as e:
            model_node.status = ModelStatus.ERROR
            return {"success": False, "error": str(e)}
