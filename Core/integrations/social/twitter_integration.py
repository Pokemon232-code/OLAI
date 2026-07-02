#!/usr/bin/env python3
"""
Twitter Integration Module
Integrates with Twitter API for tweets, analytics, and engagement
"""

import requests
import json
import os
from typing import Dict, List, Any, Optional
from datetime import datetime
import logging

logger = logging.getLogger(__name__)

class TwitterIntegration:
    """Twitter API integration for tweets, analytics, and engagement"""
    
    def __init__(self, config: Dict[str, Any] = None):
        self.config = config or {}
        self.bearer_token = self.config.get("bearer_token") or os.getenv("TWITTER_BEARER_TOKEN")
        self.api_key = self.config.get("api_key") or os.getenv("TWITTER_API_KEY")
        self.api_secret = self.config.get("api_secret") or os.getenv("TWITTER_API_SECRET")
        self.access_token = self.config.get("access_token") or os.getenv("TWITTER_ACCESS_TOKEN")
        self.access_token_secret = self.config.get("access_token_secret") or os.getenv("TWITTER_ACCESS_TOKEN_SECRET")
        
        self.base_url = "https://api.twitter.com/2"
        self.session = requests.Session()
        
        if not self.bearer_token:
            logger.warning("Twitter bearer token not provided")
    
    def _make_request(self, method: str, endpoint: str, data: Dict[str, Any] = None, params: Dict[str, Any] = None) -> Dict[str, Any]:
        """Make authenticated request to Twitter API"""
        url = f"{self.base_url}{endpoint}"
        
        headers = {
            "Authorization": f"Bearer {self.bearer_token}",
            "Content-Type": "application/json"
        }
        
        try:
            if method.upper() == "GET":
                response = self.session.get(url, headers=headers, params=params)
            elif method.upper() == "POST":
                response = self.session.post(url, headers=headers, json=data)
            elif method.upper() == "DELETE":
                response = self.session.delete(url, headers=headers, params=params)
            else:
                raise ValueError(f"Unsupported HTTP method: {method}")
            
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            logger.error(f"Twitter API request failed: {e}")
            return {"error": str(e), "status": "error"}
    
    def post_tweet(self, text: str, reply_to_tweet_id: str = None, media_ids: List[str] = None) -> Dict[str, Any]:
        """Post a tweet to Twitter"""
        try:
            endpoint = "/tweets"
            
            data = {
                "text": text
            }
            
            if reply_to_tweet_id:
                data["reply"] = {
                    "in_reply_to_tweet_id": reply_to_tweet_id
                }
            
            if media_ids:
                data["media"] = {
                    "media_ids": media_ids
                }
            
            result = self._make_request("POST", endpoint, data=data)
            
            if "error" not in result:
                return {
                    "status": "success",
                    "tweet_id": result.get("data", {}).get("id"),
                    "text": result.get("data", {}).get("text"),
                    "message": "Tweet posted successfully",
                    "timestamp": datetime.now().isoformat()
                }
            else:
                return {
                    "status": "error",
                    "error": result.get("error", {}).get("detail", "Unknown error")
                }
        except Exception as e:
            logger.error(f"Twitter post failed: {e}")
            return {"status": "error", "error": str(e)}
    
    def get_user_tweets(self, user_id: str = None, username: str = None, max_results: int = 10) -> Dict[str, Any]:
        """Get tweets from a specific user"""
        try:
            if user_id:
                endpoint = f"/users/{user_id}/tweets"
            elif username:
                # First get user ID from username
                user_info = self.get_user_info(username=username)
                if user_info.get("status") == "error":
                    return user_info
                user_id = user_info.get("user_info", {}).get("data", {}).get("id")
                endpoint = f"/users/{user_id}/tweets"
            else:
                return {"status": "error", "error": "Either user_id or username must be provided"}
            
            params = {
                "max_results": max_results,
                "tweet.fields": "created_at,public_metrics,context_annotations"
            }
            
            result = self._make_request("GET", endpoint, params=params)
            
            if "error" not in result:
                return {
                    "status": "success",
                    "tweets": result.get("data", []),
                    "timestamp": datetime.now().isoformat()
                }
            else:
                return {
                    "status": "error",
                    "error": result.get("error", {}).get("detail", "Unknown error")
                }
        except Exception as e:
            logger.error(f"Twitter user tweets retrieval failed: {e}")
            return {"status": "error", "error": str(e)}
    
    def get_user_info(self, user_id: str = None, username: str = None) -> Dict[str, Any]:
        """Get user information"""
        try:
            if user_id:
                endpoint = f"/users/{user_id}"
                params = {"user.fields": "public_metrics,verified,description,created_at"}
            elif username:
                endpoint = "/users/by/username/{username}".format(username=username)
                params = {"user.fields": "public_metrics,verified,description,created_at"}
            else:
                return {"status": "error", "error": "Either user_id or username must be provided"}
            
            result = self._make_request("GET", endpoint, params=params)
            
            if "error" not in result:
                return {
                    "status": "success",
                    "user_info": result,
                    "timestamp": datetime.now().isoformat()
                }
            else:
                return {
                    "status": "error",
                    "error": result.get("error", {}).get("detail", "Unknown error")
                }
        except Exception as e:
            logger.error(f"Twitter user info retrieval failed: {e}")
            return {"status": "error", "error": str(e)}
    
    def get_trending_topics(self, woeid: int = 1) -> Dict[str, Any]:
        """Get trending topics (requires Twitter API v1.1)"""
        try:
            # This would require Twitter API v1.1 which has different authentication
            # For now, we'll return a placeholder
            return {
                "status": "info",
                "message": "Trending topics require Twitter API v1.1 access",
                "woeid": woeid,
                "timestamp": datetime.now().isoformat()
            }
        except Exception as e:
            logger.error(f"Twitter trending topics retrieval failed: {e}")
            return {"status": "error", "error": str(e)}
    
    def get_tweet_analytics(self, tweet_id: str) -> Dict[str, Any]:
        """Get analytics for a specific tweet"""
        try:
            endpoint = f"/tweets/{tweet_id}"
            params = {
                "tweet.fields": "public_metrics,created_at,context_annotations"
            }
            
            result = self._make_request("GET", endpoint, params=params)
            
            if "error" not in result:
                return {
                    "status": "success",
                    "analytics": result.get("data", {}),
                    "timestamp": datetime.now().isoformat()
                }
            else:
                return {
                    "status": "error",
                    "error": result.get("error", {}).get("detail", "Unknown error")
                }
        except Exception as e:
            logger.error(f"Twitter tweet analytics retrieval failed: {e}")
            return {"status": "error", "error": str(e)}
    
    def create_thread(self, tweets: List[str]) -> Dict[str, Any]:
        """Create a Twitter thread by posting multiple tweets in sequence"""
        try:
            thread_results = []
            reply_to_tweet_id = None
            
            for i, tweet_text in enumerate(tweets):
                result = self.post_tweet(tweet_text, reply_to_tweet_id=reply_to_tweet_id)
                
                if result.get("status") == "success":
                    thread_results.append(result)
                    reply_to_tweet_id = result.get("tweet_id")
                else:
                    return {
                        "status": "error",
                        "error": f"Failed to post tweet {i+1}: {result.get('error')}",
                        "partial_results": thread_results
                    }
            
            return {
                "status": "success",
                "thread_tweets": thread_results,
                "thread_length": len(tweets),
                "message": "Twitter thread created successfully",
                "timestamp": datetime.now().isoformat()
            }
        except Exception as e:
            logger.error(f"Twitter thread creation failed: {e}")
            return {"status": "error", "error": str(e)}
    
    def search_tweets(self, query: str, max_results: int = 10) -> Dict[str, Any]:
        """Search for tweets"""
        try:
            endpoint = "/tweets/search/recent"
            params = {
                "query": query,
                "max_results": max_results,
                "tweet.fields": "created_at,public_metrics,author_id"
            }
            
            result = self._make_request("GET", endpoint, params=params)
            
            if "error" not in result:
                return {
                    "status": "success",
                    "tweets": result.get("data", []),
                    "meta": result.get("meta", {}),
                    "timestamp": datetime.now().isoformat()
                }
            else:
                return {
                    "status": "error",
                    "error": result.get("error", {}).get("detail", "Unknown error")
                }
        except Exception as e:
            logger.error(f"Twitter search failed: {e}")
            return {"status": "error", "error": str(e)}

# Factory function
def create_twitter_integration(config: Dict[str, Any] = None) -> TwitterIntegration:
    """Create a Twitter integration instance"""
    return TwitterIntegration(config)

# Example usage
if __name__ == "__main__":
    # Example configuration
    config = {
        "bearer_token": "your_twitter_bearer_token",
        "api_key": "your_twitter_api_key",
        "api_secret": "your_twitter_api_secret"
    }
    
    twitter = create_twitter_integration(config)
    
    # Test posting a tweet
    result = twitter.post_tweet("Hello from OLAI Twitter integration!")
    print(f"Tweet result: {result}")
    
    # Test creating a thread
    thread = twitter.create_thread([
        "Thread tweet 1: Introduction",
        "Thread tweet 2: Main content",
        "Thread tweet 3: Conclusion"
    ])
    print(f"Thread result: {thread}")
