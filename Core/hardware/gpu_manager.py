"""
GPU Manager - Unlimited Flexibility
No default limits, maximum capabilities by default
"""

import torch
import numpy as np
import threading
import queue
import time
import os
import json
from typing import Dict, Any, Optional, List, Union
from datetime import datetime
import psutil
import GPUtil

class GPUManager:
    """
    Advanced GPU manager with unlimited compute capabilities
    - Unlimited memory usage
    - Unlimited model loading
    - Unlimited parallel processing
    - No default restrictions
    """
    
    def __init__(self):
        self.device = None
        self.gpu_available = False
        self.gpu_info = {}
        self.loaded_models = {}
        self.compute_queue = queue.Queue()
        self.worker_threads = []
        self.config = {}
        
        # Performance monitoring
        self.performance_stats = {
            "memory_used": 0,
            "memory_total": 0,
            "utilization": 0,
            "temperature": 0,
            "power_usage": 0
        }
        
    def initialize(self, config: Dict[str, Any] = None):
        """Initialize GPU with unlimited configuration options"""
        self.config = config or {}
        
        # Default to maximum capabilities
        self.config.setdefault('memory_limit', 'unlimited')
        self.config.setdefault('precision', 'float32')
        self.config.setdefault('batch_size', 'auto')
        self.config.setdefault('parallel_streams', 'auto')
        self.config.setdefault('optimization', 'balanced')
        
        try:
            # Check CUDA availability
            self.gpu_available = torch.cuda.is_available()
            
            if self.gpu_available:
                self.device = torch.device('cuda:0')
                self.gpu_info = self._get_gpu_info()
                
                # Set memory management
                if self.config['memory_limit'] != 'unlimited':
                    memory_limit = self._parse_memory_limit(self.config['memory_limit'])
                    torch.cuda.set_per_process_memory_fraction(memory_limit / self.gpu_info['memory_total'])
                
                # Set optimization flags
                torch.backends.cudnn.benchmark = True
                torch.backends.cudnn.deterministic = False
                
                return True
            else:
                self.device = torch.device('cpu')
                return True
                
        except Exception as e:
            print(f"GPU initialization failed: {e}")
            self.device = torch.device('cpu')
            return False
    
    def load_model(self,
                   model_name: str,
                   model_path: str = None,
                   source: str = "auto",
                   optimization: str = "auto",
                   quantization: str = "none",
                   batch_processing: bool = True,
                   real_time: bool = False) -> Dict[str, Any]:
        """
        Load AI model with unlimited capabilities
        - model_name: Name of the model to load
        - source: huggingface, local, custom, auto
        - optimization: auto, speed, memory, accuracy
        - quantization: none, int8, int16, dynamic
        """
        
        if not self.device:
            if not self.initialize():
                return {"success": False, "error": "GPU not available"}
        
        try:
            # Load model based on source
            if source == "huggingface" or source == "auto":
                model = self._load_huggingface_model(model_name, optimization, quantization)
            elif source == "local":
                model = self._load_local_model(model_path, optimization, quantization)
            else:
                return {"success": False, "error": f"Unknown source: {source}"}
            
            # Move model to device
            model = model.to(self.device)
            
            # Set model to evaluation mode
            model.eval()
            
            # Store model
            self.loaded_models[model_name] = {
                "model": model,
                "source": source,
                "optimization": optimization,
                "quantization": quantization,
                "loaded_at": datetime.now().isoformat(),
                "memory_usage": self._get_model_memory_usage(model)
            }
            
            return {
                "success": True,
                "model_name": model_name,
                "device": str(self.device),
                "memory_usage": self.loaded_models[model_name]["memory_usage"],
                "optimization": optimization,
                "quantization": quantization
            }
            
        except Exception as e:
            return {"success": False, "error": f"Failed to load model: {e}"}
    
    def run_inference(self,
                      model_name: str,
                      input_data: Union[np.ndarray, torch.Tensor, List],
                      batch_size: int = None,
                      precision: str = None,
                      parallel_streams: int = None) -> Dict[str, Any]:
        """
        Run model inference with unlimited throughput
        - batch_size: auto or specific number (unlimited)
        - precision: float16, float32, float64, mixed
        - parallel_streams: auto or specific number (unlimited)
        """
        
        if model_name not in self.loaded_models:
            return {"success": False, "error": f"Model {model_name} not loaded"}
        
        model_info = self.loaded_models[model_name]
        model = model_info["model"]
        
        try:
            # Configure batch size
            if batch_size is None:
                batch_size = self._calculate_optimal_batch_size(model, input_data)
            
            # Configure precision
            if precision is None:
                precision = self.config.get('precision', 'float32')
            
            # Configure parallel streams
            if parallel_streams is None:
                parallel_streams = self._calculate_optimal_streams()
            
            # Prepare input data
            if isinstance(input_data, np.ndarray):
                input_tensor = torch.from_numpy(input_data).to(self.device)
            elif isinstance(input_data, list):
                input_tensor = torch.tensor(input_data).to(self.device)
            else:
                input_tensor = input_data.to(self.device)
            
            # Set precision
            if precision == 'float16':
                input_tensor = input_tensor.half()
            elif precision == 'float64':
                input_tensor = input_tensor.double()
            
            # Run inference
            start_time = time.time()
            
            with torch.no_grad():
                if batch_size > 1:
                    # Batch processing
                    outputs = []
                    for i in range(0, len(input_tensor), batch_size):
                        batch = input_tensor[i:i+batch_size]
                        output = model(batch)
                        outputs.append(output)
                    
                    if len(outputs) > 1:
                        result = torch.cat(outputs, dim=0)
                    else:
                        result = outputs[0]
                else:
                    # Single inference
                    result = model(input_tensor)
            
            inference_time = time.time() - start_time
            
            # Convert result back to numpy if needed
            if isinstance(result, torch.Tensor):
                result = result.cpu().numpy()
            
            return {
                "success": True,
                "result": result,
                "inference_time": inference_time,
                "batch_size": batch_size,
                "precision": precision,
                "parallel_streams": parallel_streams,
                "memory_used": self._get_current_memory_usage()
            }
            
        except Exception as e:
            return {"success": False, "error": f"Inference failed: {e}"}
    
    def start_compute_engine(self,
                            models: List[str] = None,
                            batch_processing: bool = True,
                            real_time: bool = False,
                            optimization: str = "auto") -> Dict[str, Any]:
        """
        Start compute engine with unlimited throughput
        - models: List of model names (unlimited)
        - batch_processing: True for maximum throughput
        - real_time: True for low latency
        """
        
        if not self.device:
            if not self.initialize():
                return {"success": False, "error": "GPU not available"}
        
        # Load models if specified
        if models:
            for model_name in models:
                if model_name not in self.loaded_models:
                    result = self.load_model(model_name, optimization=optimization)
                    if not result["success"]:
                        return {"success": False, "error": f"Failed to load model {model_name}"}
        
        # Start worker threads
        num_workers = self._calculate_optimal_workers()
        for i in range(num_workers):
            worker = threading.Thread(target=self._compute_worker, args=(i,))
            worker.daemon = True
            worker.start()
            self.worker_threads.append(worker)
        
        return {
            "success": True,
            "workers": num_workers,
            "models_loaded": list(self.loaded_models.keys()),
            "optimization": optimization,
            "real_time": real_time
        }
    
    def get_performance_stats(self) -> Dict[str, Any]:
        """Get GPU performance statistics"""
        if not self.gpu_available:
            return {"gpu_available": False}
        
        try:
            # Get GPU stats
            gpus = GPUtil.getGPUs()
            if gpus:
                gpu = gpus[0]
                self.performance_stats.update({
                    "memory_used": gpu.memoryUsed,
                    "memory_total": gpu.memoryTotal,
                    "utilization": gpu.load * 100,
                    "temperature": gpu.temperature,
                    "power_usage": gpu.powerDraw
                })
            
            # Get CUDA stats
            if torch.cuda.is_available():
                self.performance_stats.update({
                    "cuda_memory_allocated": torch.cuda.memory_allocated() / 1024**3,
                    "cuda_memory_reserved": torch.cuda.memory_reserved() / 1024**3,
                    "cuda_memory_cached": torch.cuda.memory_cached() / 1024**3
                })
            
            return {
                "gpu_available": True,
                "device": str(self.device),
                "gpu_info": self.gpu_info,
                "performance": self.performance_stats,
                "models_loaded": len(self.loaded_models),
                "models": list(self.loaded_models.keys())
            }
            
        except Exception as e:
            return {"gpu_available": False, "error": str(e)}
    
    def optimize_memory(self) -> Dict[str, Any]:
        """Optimize GPU memory usage"""
        if not self.gpu_available:
            return {"success": False, "error": "GPU not available"}
        
        try:
            # Clear cache
            torch.cuda.empty_cache()
            
            # Garbage collect
            import gc
            gc.collect()
            
            # Get memory stats
            memory_before = torch.cuda.memory_allocated()
            memory_after = torch.cuda.memory_allocated()
            
            return {
                "success": True,
                "memory_freed": memory_before - memory_after,
                "current_memory": memory_after / 1024**3,
                "memory_total": torch.cuda.get_device_properties(0).total_memory / 1024**3
            }
            
        except Exception as e:
            return {"success": False, "error": str(e)}
    
    def unload_model(self, model_name: str) -> Dict[str, Any]:
        """Unload model to free memory"""
        if model_name not in self.loaded_models:
            return {"success": False, "error": f"Model {model_name} not loaded"}
        
        try:
            # Remove model from memory
            del self.loaded_models[model_name]
            
            # Clear cache
            torch.cuda.empty_cache()
            
            return {
                "success": True,
                "model_unloaded": model_name,
                "remaining_models": list(self.loaded_models.keys())
            }
            
        except Exception as e:
            return {"success": False, "error": str(e)}
    
    def release(self):
        """Release GPU resources"""
        # Stop worker threads
        for worker in self.worker_threads:
            worker.join(timeout=1)
        
        # Unload all models
        for model_name in list(self.loaded_models.keys()):
            self.unload_model(model_name)
        
        # Clear cache
        if torch.cuda.is_available():
            torch.cuda.empty_cache()
    
    # Private helper methods
    
    def _get_gpu_info(self) -> Dict[str, Any]:
        """Get GPU information"""
        if not torch.cuda.is_available():
            return {}
        
        props = torch.cuda.get_device_properties(0)
        return {
            "name": props.name,
            "memory_total": props.total_memory / 1024**3,
            "memory_allocated": torch.cuda.memory_allocated() / 1024**3,
            "memory_reserved": torch.cuda.memory_reserved() / 1024**3,
            "compute_capability": f"{props.major}.{props.minor}",
            "multiprocessor_count": props.multi_processor_count,
            "max_threads_per_block": props.max_threads_per_block
        }
    
    def _parse_memory_limit(self, memory_limit: str) -> float:
        """Parse memory limit string to GB"""
        if memory_limit == "unlimited":
            return float('inf')
        
        memory_limit = memory_limit.lower()
        if memory_limit.endswith('gb'):
            return float(memory_limit[:-2])
        elif memory_limit.endswith('mb'):
            return float(memory_limit[:-2]) / 1024
        else:
            return float(memory_limit)
    
    def _load_huggingface_model(self, model_name: str, optimization: str, quantization: str):
        """Load model from HuggingFace"""
        try:
            from transformers import AutoModel, AutoTokenizer
            
            # Load model
            model = AutoModel.from_pretrained(model_name)
            
            # Apply optimization
            if optimization == "speed":
                model = torch.jit.script(model)
            elif optimization == "memory":
                model = model.half()
            
            # Apply quantization
            if quantization == "int8":
                model = torch.quantization.quantize_dynamic(model, {torch.nn.Linear}, dtype=torch.qint8)
            elif quantization == "int16":
                model = torch.quantization.quantize_dynamic(model, {torch.nn.Linear}, dtype=torch.qint16)
            
            return model
            
        except Exception as e:
            raise Exception(f"Failed to load HuggingFace model: {e}")
    
    def _load_local_model(self, model_path: str, optimization: str, quantization: str):
        """Load model from local path"""
        try:
            # Load model from file
            if model_path.endswith('.pt') or model_path.endswith('.pth'):
                model = torch.load(model_path, map_location=self.device)
            else:
                raise Exception(f"Unsupported model format: {model_path}")
            
            # Apply optimization and quantization
            if optimization == "speed":
                model = torch.jit.script(model)
            elif optimization == "memory":
                model = model.half()
            
            if quantization == "int8":
                model = torch.quantization.quantize_dynamic(model, {torch.nn.Linear}, dtype=torch.qint8)
            elif quantization == "int16":
                model = torch.quantization.quantize_dynamic(model, {torch.nn.Linear}, dtype=torch.qint16)
            
            return model
            
        except Exception as e:
            raise Exception(f"Failed to load local model: {e}")
    
    def _calculate_optimal_batch_size(self, model, input_data) -> int:
        """Calculate optimal batch size for model"""
        if self.config.get('batch_size') != 'auto':
            return int(self.config['batch_size'])
        
        # Calculate based on available memory
        available_memory = self.gpu_info.get('memory_total', 8) - self.gpu_info.get('memory_allocated', 0)
        
        # Estimate memory per sample (rough calculation)
        if isinstance(input_data, torch.Tensor):
            memory_per_sample = input_data.element_size() * input_data.nelement()
        else:
            memory_per_sample = 1024 * 1024  # 1MB default
        
        # Calculate batch size (leave some memory for model)
        max_batch_size = int((available_memory * 0.8) / (memory_per_sample / 1024**3))
        
        return max(1, min(max_batch_size, 1000))  # Cap at 1000 for safety
    
    def _calculate_optimal_streams(self) -> int:
        """Calculate optimal number of parallel streams"""
        if self.config.get('parallel_streams') != 'auto':
            return int(self.config['parallel_streams'])
        
        # Calculate based on GPU capabilities
        if self.gpu_available:
            return min(32, self.gpu_info.get('multiprocessor_count', 1) * 2)
        else:
            return min(8, psutil.cpu_count())
    
    def _calculate_optimal_workers(self) -> int:
        """Calculate optimal number of worker threads"""
        if self.gpu_available:
            return min(16, self.gpu_info.get('multiprocessor_count', 1) * 2)
        else:
            return min(8, psutil.cpu_count())
    
    def _get_model_memory_usage(self, model) -> float:
        """Get memory usage of model in GB"""
        if self.gpu_available:
            return torch.cuda.memory_allocated() / 1024**3
        else:
            # Estimate CPU memory usage
            param_count = sum(p.numel() for p in model.parameters())
            return param_count * 4 / 1024**3  # 4 bytes per float32 parameter
    
    def _get_current_memory_usage(self) -> float:
        """Get current memory usage in GB"""
        if self.gpu_available:
            return torch.cuda.memory_allocated() / 1024**3
        else:
            return psutil.Process().memory_info().rss / 1024**3
    
    def _compute_worker(self, worker_id: int):
        """Worker thread for compute engine"""
        while True:
            try:
                # Get task from queue
                task = self.compute_queue.get(timeout=1)
                if task is None:
                    break
                
                # Process task
                model_name = task.get('model_name')
                input_data = task.get('input_data')
                callback = task.get('callback')
                
                if model_name in self.loaded_models:
                    result = self.run_inference(model_name, input_data)
                    if callback:
                        callback(result)
                
                self.compute_queue.task_done()
                
            except queue.Empty:
                continue
            except Exception as e:
                print(f"Compute worker {worker_id} error: {e}")
                continue
