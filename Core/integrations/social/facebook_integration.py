#!/usr/bin/env python3
"""
Facebook Integration Module
Integrates with Facebook API for posts, pages, and analytics
"""

import requests
import json
import os
from typing import Dict, List, Any, Optional
from datetime import datetime
import logging

logger = logging.getLogger(__name__)

class FacebookIntegration:
    """Facebook API integration for posts, pages, and analytics"""
    
    def __init__(self, config: Dict[str, Any] = None):
        self.config = config or {}
        self.access_token = self.config.get("access_token") or os.getenv("FACEBOOK_ACCESS_TOKEN")
        self.app_id = self.config.get("app_id") or os.getenv("FACEBOOK_APP_ID")
        self.app_secret = self.config.get("app_secret") or os.getenv("FACEBOOK_APP_SECRET")
        self.base_url = "https://graph.facebook.com/v18.0"
        self.session = requests.Session()
        
        if not self.access_token:
            logger.warning("Facebook access token not provided")
    
    def _make_request(self, method: str, endpoint: str, data: Dict[str, Any] = None, params: Dict[str, Any] = None) -> Dict[str, Any]:
        """Make authenticated request to Facebook API"""
        url = f"{self.base_url}{endpoint}"
        
        if not params:
            params = {}
        params["access_token"] = self.access_token
        
        try:
            if method.upper() == "GET":
                response = self.session.get(url, params=params)
            elif method.upper() == "POST":
                response = self.session.post(url, json=data, params=params)
            elif method.upper() == "DELETE":
                response = self.session.delete(url, params=params)
            else:
                raise ValueError(f"Unsupported HTTP method: {method}")
            
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            logger.error(f"Facebook API request failed: {e}")
            return {"error": str(e), "status": "error"}
    
    def post_content(self, message: str, page_id: str = None, link: str = None, image_url: str = None) -> Dict[str, Any]:
        """Post content to Facebook page or personal profile"""
        try:
            endpoint = f"/{page_id}/feed" if page_id else "/me/feed"
            
            data = {
                "message": message
            }
            
            if link:
                data["link"] = link
            if image_url:
                data["picture"] = image_url
            
            result = self._make_request("POST", endpoint, data=data)
            
            if "error" not in result:
                return {
                    "status": "success",
                    "post_id": result.get("id"),
                    "message": "Content posted successfully",
                    "timestamp": datetime.now().isoformat()
                }
            else:
                return {
                    "status": "error",
                    "error": result.get("error", {}).get("message", "Unknown error")
                }
        except Exception as e:
            logger.error(f"Facebook post failed: {e}")
            return {"status": "error", "error": str(e)}
    
    def get_page_info(self, page_id: str) -> Dict[str, Any]:
        """Get Facebook page information"""
        try:
            endpoint = f"/{page_id}"
            params = {
                "fields": "id,name,about,fan_count,website,phone,emails"
            }
            
            result = self._make_request("GET", endpoint, params=params)
            
            if "error" not in result:
                return {
                    "status": "success",
                    "page_info": result,
                    "timestamp": datetime.now().isoformat()
                }
            else:
                return {
                    "status": "error",
                    "error": result.get("error", {}).get("message", "Unknown error")
                }
        except Exception as e:
            logger.error(f"Facebook page info retrieval failed: {e}")
            return {"status": "error", "error": str(e)}
    
    def get_analytics(self, page_id: str, metric: str = "page_impressions", period: str = "day") -> Dict[str, Any]:
        """Get Facebook page analytics"""
        try:
            endpoint = f"/{page_id}/insights"
            params = {
                "metric": metric,
                "period": period
            }
            
            result = self._make_request("GET", endpoint, params=params)
            
            if "error" not in result:
                return {
                    "status": "success",
                    "analytics": result.get("data", []),
                    "timestamp": datetime.now().isoformat()
                }
            else:
                return {
                    "status": "error",
                    "error": result.get("error", {}).get("message", "Unknown error")
                }
        except Exception as e:
            logger.error(f"Facebook analytics retrieval failed: {e}")
            return {"status": "error", "error": str(e)}
    
    def get_posts(self, page_id: str, limit: int = 25) -> Dict[str, Any]:
        """Get recent posts from Facebook page"""
        try:
            endpoint = f"/{page_id}/posts"
            params = {
                "limit": limit,
                "fields": "id,message,created_time,likes.summary(true),comments.summary(true),shares"
            }
            
            result = self._make_request("GET", endpoint, params=params)
            
            if "error" not in result:
                return {
                    "status": "success",
                    "posts": result.get("data", []),
                    "timestamp": datetime.now().isoformat()
                }
            else:
                return {
                    "status": "error",
                    "error": result.get("error", {}).get("message", "Unknown error")
                }
        except Exception as e:
            logger.error(f"Facebook posts retrieval failed: {e}")
            return {"status": "error", "error": str(e)}
    
    def schedule_post(self, message: str, scheduled_time: str, page_id: str = None) -> Dict[str, Any]:
        """Schedule a post for later publishing"""
        try:
            endpoint = f"/{page_id}/feed" if page_id else "/me/feed"
            
            data = {
                "message": message,
                "scheduled_publish_time": scheduled_time,
                "published": False
            }
            
            result = self._make_request("POST", endpoint, data=data)
            
            if "error" not in result:
                return {
                    "status": "success",
                    "post_id": result.get("id"),
                    "scheduled_time": scheduled_time,
                    "message": "Post scheduled successfully",
                    "timestamp": datetime.now().isoformat()
                }
            else:
                return {
                    "status": "error",
                    "error": result.get("error", {}).get("message", "Unknown error")
                }
        except Exception as e:
            logger.error(f"Facebook post scheduling failed: {e}")
            return {"status": "error", "error": str(e)}
    
    def get_user_engagement(self, post_id: str) -> Dict[str, Any]:
        """Get user engagement metrics for a specific post"""
        try:
            endpoint = f"/{post_id}/insights"
            params = {
                "metric": "post_impressions,post_engaged_users,post_clicks"
            }
            
            result = self._make_request("GET", endpoint, params=params)
            
            if "error" not in result:
                return {
                    "status": "success",
                    "engagement": result.get("data", []),
                    "timestamp": datetime.now().isoformat()
                }
            else:
                return {
                    "status": "error",
                    "error": result.get("error", {}).get("message", "Unknown error")
                }
        except Exception as e:
            logger.error(f"Facebook engagement retrieval failed: {e}")
            return {"status": "error", "error": str(e)}

# Factory function
def create_facebook_integration(config: Dict[str, Any] = None) -> FacebookIntegration:
    """Create a Facebook integration instance"""
    return FacebookIntegration(config)

# Example usage
if __name__ == "__main__":
    # Example configuration
    config = {
        "access_token": "your_facebook_access_token",
        "app_id": "your_facebook_app_id",
        "app_secret": "your_facebook_app_secret"
    }
    
    facebook = create_facebook_integration(config)
    
    # Test posting content
    result = facebook.post_content("Hello from OLAI Facebook integration!")
    print(f"Post result: {result}")
    
    # Test getting analytics
    analytics = facebook.get_analytics("your_page_id")
    print(f"Analytics result: {analytics}")
