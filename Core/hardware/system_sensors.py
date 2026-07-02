"""
System Sensors - Unlimited Flexibility
No default limits, maximum capabilities by default
"""

import psutil
import time
import threading
import queue
import json
import os
from typing import Dict, Any, Optional, List, Callable
from datetime import datetime
import GPUtil
import platform

class SystemSensors:
    """
    Advanced system monitoring with unlimited metrics
    - Unlimited monitoring duration
    - Unlimited metrics collection
    - Unlimited alerting capabilities
    - No default restrictions
    """
    
    def __init__(self):
        self.is_monitoring = False
        self.monitor_thread = None
        self.metrics_queue = queue.Queue()
        self.callbacks = {}
        self.config = {}
        self.metrics_history = []
        self.alerts = []
        
        # Performance tracking
        self.performance_data = {
            "cpu": [],
            "memory": [],
            "disk": [],
            "network": [],
            "gpu": [],
            "temperature": [],
            "power": []
        }
        
    def initialize(self, config: Dict[str, Any] = None):
        """Initialize system sensors with unlimited configuration options"""
        self.config = config or {}
        
        # Default to maximum capabilities
        self.config.setdefault('metrics', ['all'])
        self.config.setdefault('interval', '1s')
        self.config.setdefault('duration', 'unlimited')
        self.config.setdefault('alerts', False)
        self.config.setdefault('logging', True)
        self.config.setdefault('visualization', False)
        
        return True
    
    def start_monitor(self,
                     metrics: List[str] = None,
                     interval: str = "1s",
                     duration: str = "unlimited",
                     alerts: bool = False,
                     logging: bool = True,
                     visualization: bool = False,
                     callback: Callable = None) -> Dict[str, Any]:
        """
        Start system monitoring with unlimited capabilities
        - metrics: cpu, memory, disk, network, gpu, temperature, power, all
        - interval: 100ms, 500ms, 1s, 5s, 10s, 30s, 1m, custom
        - duration: unlimited, 1m, 5m, 10m, 1h, 24h, custom
        """
        
        if not self.initialize():
            return {"success": False, "error": "System sensors not available"}
        
        # Configure monitoring
        if metrics is None:
            metrics = self.config.get('metrics', ['all'])
        
        if 'all' in metrics:
            metrics = ['cpu', 'memory', 'disk', 'network', 'gpu', 'temperature', 'power']
        
        # Parse interval and duration
        interval_seconds = self._parse_duration(interval)
        duration_seconds = self._parse_duration(duration)
        
        self.is_monitoring = True
        self.callbacks['monitor'] = callback
        
        # Start monitoring thread
        self.monitor_thread = threading.Thread(
            target=self._monitor_worker,
            args=(metrics, interval_seconds, duration_seconds, alerts, logging, visualization)
        )
        self.monitor_thread.start()
        
        return {
            "success": True,
            "monitoring": True,
            "metrics": metrics,
            "interval": interval,
            "duration": duration,
            "alerts": alerts,
            "logging": logging
        }
    
    def get_system_info(self) -> Dict[str, Any]:
        """Get comprehensive system information"""
        try:
            # CPU Information
            cpu_info = {
                "count_physical": psutil.cpu_count(logical=False),
                "count_logical": psutil.cpu_count(logical=True),
                "freq_current": psutil.cpu_freq().current if psutil.cpu_freq() else 0,
                "freq_max": psutil.cpu_freq().max if psutil.cpu_freq() else 0,
                "usage_percent": psutil.cpu_percent(interval=1),
                "usage_per_core": psutil.cpu_percent(interval=1, percpu=True),
                "load_average": os.getloadavg() if hasattr(os, 'getloadavg') else [0, 0, 0]
            }
            
            # Memory Information
            memory = psutil.virtual_memory()
            memory_info = {
                "total_gb": round(memory.total / 1024**3, 2),
                "available_gb": round(memory.available / 1024**3, 2),
                "used_gb": round(memory.used / 1024**3, 2),
                "free_gb": round(memory.free / 1024**3, 2),
                "usage_percent": memory.percent,
                "cached_gb": round(getattr(memory, 'cached', 0) / 1024**3, 2),
                "buffers_gb": round(getattr(memory, 'buffers', 0) / 1024**3, 2)
            }
            
            # Disk Information
            disk_info = []
            for partition in psutil.disk_partitions():
                try:
                    partition_usage = psutil.disk_usage(partition.mountpoint)
                    disk_info.append({
                        "device": partition.device,
                        "mountpoint": partition.mountpoint,
                        "fstype": partition.fstype,
                        "total_gb": round(partition_usage.total / 1024**3, 2),
                        "used_gb": round(partition_usage.used / 1024**3, 2),
                        "free_gb": round(partition_usage.free / 1024**3, 2),
                        "usage_percent": round((partition_usage.used / partition_usage.total) * 100, 2)
                    })
                except PermissionError:
                    continue
            
            # Network Information
            network_info = {
                "interfaces": [],
                "connections": len(psutil.net_connections()),
                "io_counters": {}
            }
            
            # Network interfaces
            for interface, addrs in psutil.net_if_addrs().items():
                interface_info = {
                    "name": interface,
                    "addresses": []
                }
                for addr in addrs:
                    interface_info["addresses"].append({
                        "family": str(addr.family),
                        "address": addr.address,
                        "netmask": addr.netmask,
                        "broadcast": addr.broadcast
                    })
                network_info["interfaces"].append(interface_info)
            
            # Network I/O counters
            net_io = psutil.net_io_counters()
            if net_io:
                network_info["io_counters"] = {
                    "bytes_sent": net_io.bytes_sent,
                    "bytes_recv": net_io.bytes_recv,
                    "packets_sent": net_io.packets_sent,
                    "packets_recv": net_io.packets_recv,
                    "errin": net_io.errin,
                    "errout": net_io.errout,
                    "dropin": net_io.dropin,
                    "dropout": net_io.dropout
                }
            
            # GPU Information
            gpu_info = []
            try:
                gpus = GPUtil.getGPUs()
                for gpu in gpus:
                    gpu_info.append({
                        "id": gpu.id,
                        "name": gpu.name,
                        "memory_total_mb": gpu.memoryTotal,
                        "memory_used_mb": gpu.memoryUsed,
                        "memory_free_mb": gpu.memoryFree,
                        "utilization_percent": gpu.load * 100,
                        "temperature_c": gpu.temperature,
                        "power_usage_w": gpu.powerDraw,
                        "power_limit_w": gpu.powerLimit
                    })
            except:
                pass
            
            # System Information
            system_info = {
                "platform": platform.system(),
                "platform_release": platform.release(),
                "platform_version": platform.version(),
                "architecture": platform.architecture()[0],
                "processor": platform.processor(),
                "hostname": platform.node(),
                "python_version": platform.python_version(),
                "boot_time": datetime.fromtimestamp(psutil.boot_time()).isoformat(),
                "uptime_seconds": time.time() - psutil.boot_time()
            }
            
            # Process Information
            process_info = {
                "total_processes": len(psutil.pids()),
                "running_processes": len([p for p in psutil.process_iter(['status']) if p.info['status'] == psutil.STATUS_RUNNING]),
                "sleeping_processes": len([p for p in psutil.process_iter(['status']) if p.info['status'] == psutil.STATUS_SLEEPING]),
                "zombie_processes": len([p for p in psutil.process_iter(['status']) if p.info['status'] == psutil.STATUS_ZOMBIE])
            }
            
            return {
                "success": True,
                "timestamp": datetime.now().isoformat(),
                "system": system_info,
                "cpu": cpu_info,
                "memory": memory_info,
                "disk": disk_info,
                "network": network_info,
                "gpu": gpu_info,
                "processes": process_info
            }
            
        except Exception as e:
            return {"success": False, "error": str(e)}
    
    def get_current_metrics(self, metrics: List[str] = None) -> Dict[str, Any]:
        """Get current system metrics"""
        if metrics is None:
            metrics = ['cpu', 'memory', 'disk', 'network', 'gpu']
        
        current_metrics = {
            "timestamp": datetime.now().isoformat(),
            "metrics": {}
        }
        
        try:
            if 'cpu' in metrics:
                current_metrics["metrics"]["cpu"] = {
                    "usage_percent": psutil.cpu_percent(interval=0.1),
                    "usage_per_core": psutil.cpu_percent(interval=0.1, percpu=True),
                    "freq_current": psutil.cpu_freq().current if psutil.cpu_freq() else 0,
                    "load_average": os.getloadavg() if hasattr(os, 'getloadavg') else [0, 0, 0]
                }
            
            if 'memory' in metrics:
                memory = psutil.virtual_memory()
                current_metrics["metrics"]["memory"] = {
                    "usage_percent": memory.percent,
                    "used_gb": round(memory.used / 1024**3, 2),
                    "available_gb": round(memory.available / 1024**3, 2),
                    "total_gb": round(memory.total / 1024**3, 2)
                }
            
            if 'disk' in metrics:
                disk_usage = psutil.disk_usage('/')
                current_metrics["metrics"]["disk"] = {
                    "usage_percent": round((disk_usage.used / disk_usage.total) * 100, 2),
                    "used_gb": round(disk_usage.used / 1024**3, 2),
                    "free_gb": round(disk_usage.free / 1024**3, 2),
                    "total_gb": round(disk_usage.total / 1024**3, 2)
                }
            
            if 'network' in metrics:
                net_io = psutil.net_io_counters()
                if net_io:
                    current_metrics["metrics"]["network"] = {
                        "bytes_sent": net_io.bytes_sent,
                        "bytes_recv": net_io.bytes_recv,
                        "packets_sent": net_io.packets_sent,
                        "packets_recv": net_io.packets_recv
                    }
            
            if 'gpu' in metrics:
                try:
                    gpus = GPUtil.getGPUs()
                    if gpus:
                        gpu = gpus[0]
                        current_metrics["metrics"]["gpu"] = {
                            "utilization_percent": gpu.load * 100,
                            "memory_used_mb": gpu.memoryUsed,
                            "memory_total_mb": gpu.memoryTotal,
                            "temperature_c": gpu.temperature,
                            "power_usage_w": gpu.powerDraw
                        }
                except:
                    current_metrics["metrics"]["gpu"] = {"available": False}
            
            return current_metrics
            
        except Exception as e:
            return {"success": False, "error": str(e)}
    
    def get_metrics_history(self, metric_type: str = None, limit: int = 1000) -> Dict[str, Any]:
        """Get historical metrics data"""
        try:
            if metric_type:
                history = self.performance_data.get(metric_type, [])[-limit:]
            else:
                history = {}
                for metric_type, data in self.performance_data.items():
                    history[metric_type] = data[-limit:]
            
            return {
                "success": True,
                "metric_type": metric_type,
                "limit": limit,
                "history": history,
                "total_points": sum(len(data) for data in self.performance_data.values())
            }
            
        except Exception as e:
            return {"success": False, "error": str(e)}
    
    def set_alert_threshold(self, metric: str, threshold: float, condition: str = "greater") -> Dict[str, Any]:
        """Set alert threshold for specific metric"""
        try:
            alert_config = {
                "metric": metric,
                "threshold": threshold,
                "condition": condition,
                "enabled": True,
                "created_at": datetime.now().isoformat()
            }
            
            self.alerts.append(alert_config)
            
            return {
                "success": True,
                "alert": alert_config,
                "total_alerts": len(self.alerts)
            }
            
        except Exception as e:
            return {"success": False, "error": str(e)}
    
    def stop_monitoring(self):
        """Stop system monitoring"""
        self.is_monitoring = False
        if self.monitor_thread:
            self.monitor_thread.join()
    
    def export_metrics(self, file_path: str = None, format: str = "json") -> Dict[str, Any]:
        """Export metrics data to file"""
        try:
            if file_path is None:
                timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
                file_path = f"metrics_export_{timestamp}.{format}"
            
            os.makedirs(os.path.dirname(file_path), exist_ok=True)
            
            export_data = {
                "export_timestamp": datetime.now().isoformat(),
                "system_info": self.get_system_info(),
                "metrics_history": self.performance_data,
                "alerts": self.alerts
            }
            
            if format.lower() == "json":
                with open(file_path, 'w') as f:
                    json.dump(export_data, f, indent=2)
            elif format.lower() == "csv":
                # Convert to CSV format
                self._export_to_csv(export_data, file_path)
            
            return {
                "success": True,
                "file_path": file_path,
                "format": format,
                "data_points": sum(len(data) for data in self.performance_data.values())
            }
            
        except Exception as e:
            return {"success": False, "error": str(e)}
    
    def release(self):
        """Release system sensor resources"""
        self.stop_monitoring()
    
    # Private helper methods
    
    def _parse_duration(self, duration: str) -> float:
        """Parse duration string to seconds"""
        if duration == "unlimited" or duration == "continuous":
            return 0
        
        duration = duration.lower()
        if duration.endswith('ms'):
            return float(duration[:-2]) / 1000
        elif duration.endswith('s'):
            return float(duration[:-1])
        elif duration.endswith('m'):
            return float(duration[:-1]) * 60
        elif duration.endswith('h'):
            return float(duration[:-1]) * 3600
        elif duration.endswith('d'):
            return float(duration[:-1]) * 86400
        else:
            return float(duration)
    
    def _monitor_worker(self, metrics, interval_seconds, duration_seconds, alerts, logging, visualization):
        """Worker thread for system monitoring"""
        start_time = time.time()
        
        while self.is_monitoring:
            try:
                # Get current metrics
                current_metrics = self.get_current_metrics(metrics)
                
                if current_metrics.get("success"):
                    # Store metrics
                    for metric_type, data in current_metrics["metrics"].items():
                        if metric_type in self.performance_data:
                            self.performance_data[metric_type].append({
                                "timestamp": current_metrics["timestamp"],
                                "data": data
                            })
                            
                            # Keep only recent data (last 10000 points)
                            if len(self.performance_data[metric_type]) > 10000:
                                self.performance_data[metric_type] = self.performance_data[metric_type][-10000:]
                    
                    # Check alerts
                    if alerts:
                        self._check_alerts(current_metrics)
                    
                    # Log metrics
                    if logging:
                        self._log_metrics(current_metrics)
                    
                    # Callback if provided
                    if self.callbacks.get('monitor'):
                        self.callbacks['monitor'](current_metrics)
                
                # Check duration limit
                if duration_seconds > 0 and (time.time() - start_time) >= duration_seconds:
                    break
                
                # Wait for next interval
                time.sleep(interval_seconds)
                
            except Exception as e:
                print(f"Monitoring error: {e}")
                time.sleep(interval_seconds)
    
    def _check_alerts(self, metrics):
        """Check if any metrics exceed alert thresholds"""
        for alert in self.alerts:
            if not alert.get("enabled", True):
                continue
            
            metric_name = alert["metric"]
            threshold = alert["threshold"]
            condition = alert["condition"]
            
            # Get metric value
            metric_value = None
            if metric_name in metrics["metrics"]:
                metric_data = metrics["metrics"][metric_name]
                if isinstance(metric_data, dict):
                    # Try to find a percentage or usage value
                    for key in ["usage_percent", "percent", "utilization_percent"]:
                        if key in metric_data:
                            metric_value = metric_data[key]
                            break
                elif isinstance(metric_data, (int, float)):
                    metric_value = metric_data
            
            if metric_value is not None:
                # Check condition
                alert_triggered = False
                if condition == "greater" and metric_value > threshold:
                    alert_triggered = True
                elif condition == "less" and metric_value < threshold:
                    alert_triggered = True
                elif condition == "equal" and metric_value == threshold:
                    alert_triggered = True
                
                if alert_triggered:
                    alert_message = {
                        "timestamp": datetime.now().isoformat(),
                        "metric": metric_name,
                        "value": metric_value,
                        "threshold": threshold,
                        "condition": condition,
                        "message": f"{metric_name} {condition} {threshold} (current: {metric_value})"
                    }
                    
                    # Store alert
                    self.alerts.append(alert_message)
                    
                    # Callback if provided
                    if self.callbacks.get('alert'):
                        self.callbacks['alert'](alert_message)
    
    def _log_metrics(self, metrics):
        """Log metrics to file"""
        try:
            log_file = f"system_metrics_{datetime.now().strftime('%Y%m%d')}.log"
            with open(log_file, 'a') as f:
                f.write(f"{metrics['timestamp']}: {json.dumps(metrics['metrics'])}\n")
        except Exception as e:
            print(f"Logging error: {e}")
    
    def _export_to_csv(self, data, file_path):
        """Export data to CSV format"""
        import csv
        
        with open(file_path, 'w', newline='') as f:
            writer = csv.writer(f)
            
            # Write header
            writer.writerow(['timestamp', 'metric_type', 'metric_name', 'value'])
            
            # Write data
            for metric_type, history in data["metrics_history"].items():
                for point in history:
                    timestamp = point["timestamp"]
                    metric_data = point["data"]
                    
                    if isinstance(metric_data, dict):
                        for key, value in metric_data.items():
                            writer.writerow([timestamp, metric_type, key, value])
                    else:
                        writer.writerow([timestamp, metric_type, 'value', metric_data])
