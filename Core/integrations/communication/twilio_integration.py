#!/usr/bin/env python3
"""
Twilio Integration Module
Integrates with Twilio communication services (SMS, Voice, Video, WhatsApp)
"""

from twilio.rest import Client
from twilio.twiml import VoiceResponse, MessagingResponse
import os
import json
from typing import Dict, List, Any, Optional
from datetime import datetime
import logging

logger = logging.getLogger(__name__)

class TwilioIntegration:
    """Twilio communication services integration"""
    
    def __init__(self, config: Dict[str, Any] = None):
        self.config = config or {}
        self.account_sid = self.config.get("account_sid") or os.getenv("TWILIO_ACCOUNT_SID")
        self.auth_token = self.config.get("auth_token") or os.getenv("TWILIO_AUTH_TOKEN")
        self.phone_number = self.config.get("phone_number") or os.getenv("TWILIO_PHONE_NUMBER")
        
        if not self.account_sid or not self.auth_token:
            logger.warning("Twilio credentials not provided")
        else:
            self.client = Client(self.account_sid, self.auth_token)
    
    def send_sms(self, to_number: str, message: str, from_number: str = None) -> Dict[str, Any]:
        """Send SMS message"""
        try:
            if not from_number:
                from_number = self.phone_number
            
            message_obj = self.client.messages.create(
                body=message,
                from_=from_number,
                to=to_number
            )
            
            return {
                "status": "success",
                "message_sid": message_obj.sid,
                "to_number": to_number,
                "from_number": from_number,
                "message": "SMS sent successfully",
                "timestamp": datetime.now().isoformat()
            }
        except Exception as e:
            logger.error(f"SMS sending failed: {e}")
            return {"status": "error", "error": str(e)}
    
    def send_whatsapp_message(self, to_number: str, message: str, from_number: str = None) -> Dict[str, Any]:
        """Send WhatsApp message"""
        try:
            if not from_number:
                from_number = f"whatsapp:{self.phone_number}"
            
            # Ensure numbers are in whatsapp: format
            if not to_number.startswith("whatsapp:"):
                to_number = f"whatsapp:{to_number}"
            
            message_obj = self.client.messages.create(
                body=message,
                from_=from_number,
                to=to_number
            )
            
            return {
                "status": "success",
                "message_sid": message_obj.sid,
                "to_number": to_number,
                "from_number": from_number,
                "message": "WhatsApp message sent successfully",
                "timestamp": datetime.now().isoformat()
            }
        except Exception as e:
            logger.error(f"WhatsApp message sending failed: {e}")
            return {"status": "error", "error": str(e)}
    
    def make_voice_call(self, to_number: str, twiml_url: str, from_number: str = None) -> Dict[str, Any]:
        """Make a voice call"""
        try:
            if not from_number:
                from_number = self.phone_number
            
            call = self.client.calls.create(
                to=to_number,
                from_=from_number,
                url=twiml_url
            )
            
            return {
                "status": "success",
                "call_sid": call.sid,
                "to_number": to_number,
                "from_number": from_number,
                "status": call.status,
                "message": "Voice call initiated successfully",
                "timestamp": datetime.now().isoformat()
            }
        except Exception as e:
            logger.error(f"Voice call failed: {e}")
            return {"status": "error", "error": str(e)}
    
    def send_voice_message(self, to_number: str, message: str, from_number: str = None, 
                          voice: str = "alice", language: str = "en") -> Dict[str, Any]:
        """Send a voice message using text-to-speech"""
        try:
            if not from_number:
                from_number = self.phone_number
            
            # Create TwiML for text-to-speech
            response = VoiceResponse()
            response.say(message, voice=voice, language=language)
            
            # Save TwiML to a temporary URL or use inline TwiML
            twiml = str(response)
            
            call = self.client.calls.create(
                to=to_number,
                from_=from_number,
                twiml=twiml
            )
            
            return {
                "status": "success",
                "call_sid": call.sid,
                "to_number": to_number,
                "from_number": from_number,
                "message_text": message,
                "voice": voice,
                "language": language,
                "message": "Voice message sent successfully",
                "timestamp": datetime.now().isoformat()
            }
        except Exception as e:
            logger.error(f"Voice message sending failed: {e}")
            return {"status": "error", "error": str(e)}
    
    def create_video_room(self, room_name: str, max_participants: int = 10) -> Dict[str, Any]:
        """Create a video room for video calls"""
        try:
            room = self.client.video.rooms.create(
                unique_name=room_name,
                max_participants=max_participants
            )
            
            return {
                "status": "success",
                "room_sid": room.sid,
                "room_name": room.unique_name,
                "max_participants": room.max_participants,
                "status": room.status,
                "message": "Video room created successfully",
                "timestamp": datetime.now().isoformat()
            }
        except Exception as e:
            logger.error(f"Video room creation failed: {e}")
            return {"status": "error", "error": str(e)}
    
    def get_call_history(self, limit: int = 20) -> Dict[str, Any]:
        """Get call history"""
        try:
            calls = self.client.calls.list(limit=limit)
            
            call_history = []
            for call in calls:
                call_history.append({
                    "sid": call.sid,
                    "from_number": call.from_formatted,
                    "to_number": call.to_formatted,
                    "status": call.status,
                    "start_time": call.start_time.isoformat() if call.start_time else None,
                    "end_time": call.end_time.isoformat() if call.end_time else None,
                    "duration": call.duration
                })
            
            return {
                "status": "success",
                "calls": call_history,
                "total_calls": len(call_history),
                "timestamp": datetime.now().isoformat()
            }
        except Exception as e:
            logger.error(f"Call history retrieval failed: {e}")
            return {"status": "error", "error": str(e)}
    
    def get_message_history(self, limit: int = 20) -> Dict[str, Any]:
        """Get message history"""
        try:
            messages = self.client.messages.list(limit=limit)
            
            message_history = []
            for message in messages:
                message_history.append({
                    "sid": message.sid,
                    "from_number": message.from_formatted,
                    "to_number": message.to_formatted,
                    "body": message.body,
                    "status": message.status,
                    "date_sent": message.date_sent.isoformat() if message.date_sent else None,
                    "direction": message.direction
                })
            
            return {
                "status": "success",
                "messages": message_history,
                "total_messages": len(message_history),
                "timestamp": datetime.now().isoformat()
            }
        except Exception as e:
            logger.error(f"Message history retrieval failed: {e}")
            return {"status": "error", "error": str(e)}
    
    def send_bulk_sms(self, phone_numbers: List[str], message: str, from_number: str = None) -> Dict[str, Any]:
        """Send SMS to multiple phone numbers"""
        try:
            results = []
            successful_sends = 0
            failed_sends = 0
            
            for phone_number in phone_numbers:
                result = self.send_sms(phone_number, message, from_number)
                results.append({
                    "phone_number": phone_number,
                    "result": result
                })
                
                if result.get("status") == "success":
                    successful_sends += 1
                else:
                    failed_sends += 1
            
            return {
                "status": "success",
                "total_numbers": len(phone_numbers),
                "successful_sends": successful_sends,
                "failed_sends": failed_sends,
                "results": results,
                "message": f"Bulk SMS completed: {successful_sends} successful, {failed_sends} failed",
                "timestamp": datetime.now().isoformat()
            }
        except Exception as e:
            logger.error(f"Bulk SMS sending failed: {e}")
            return {"status": "error", "error": str(e)}
    
    def create_messaging_webhook(self, webhook_url: str, http_method: str = "POST") -> Dict[str, Any]:
        """Create a webhook for incoming messages"""
        try:
            # This would typically be configured in your Twilio console
            # But we can provide the webhook URL for configuration
            return {
                "status": "success",
                "webhook_url": webhook_url,
                "http_method": http_method,
                "message": "Webhook configuration details provided",
                "instructions": "Configure this webhook URL in your Twilio console under Phone Numbers > Manage > Active Numbers",
                "timestamp": datetime.now().isoformat()
            }
        except Exception as e:
            logger.error(f"Webhook creation failed: {e}")
            return {"status": "error", "error": str(e)}
    
    def handle_incoming_sms(self, request_data: Dict[str, Any]) -> Dict[str, Any]:
        """Handle incoming SMS webhook"""
        try:
            from_number = request_data.get('From')
            to_number = request_data.get('To')
            message_body = request_data.get('Body')
            
            # Create TwiML response
            response = MessagingResponse()
            
            # Auto-reply logic
            auto_reply = f"Thank you for your message: '{message_body}'. This is an automated response from OLAI."
            response.message(auto_reply)
            
            return {
                "status": "success",
                "from_number": from_number,
                "to_number": to_number,
                "message_body": message_body,
                "twiml_response": str(response),
                "message": "Incoming SMS handled successfully",
                "timestamp": datetime.now().isoformat()
            }
        except Exception as e:
            logger.error(f"Incoming SMS handling failed: {e}")
            return {"status": "error", "error": str(e)}
    
    def get_account_info(self) -> Dict[str, Any]:
        """Get Twilio account information"""
        try:
            account = self.client.api.accounts(self.account_sid).fetch()
            
            return {
                "status": "success",
                "account_sid": account.sid,
                "friendly_name": account.friendly_name,
                "status": account.status,
                "type": account.type,
                "timestamp": datetime.now().isoformat()
            }
        except Exception as e:
            logger.error(f"Account info retrieval failed: {e}")
            return {"status": "error", "error": str(e)}

# Factory function
def create_twilio_integration(config: Dict[str, Any] = None) -> TwilioIntegration:
    """Create a Twilio integration instance"""
    return TwilioIntegration(config)

# Example usage
if __name__ == "__main__":
    # Example configuration
    config = {
        "account_sid": "your_twilio_account_sid",
        "auth_token": "your_twilio_auth_token",
        "phone_number": "+1234567890"
    }
    
    twilio = create_twilio_integration(config)
    
    # Test sending SMS
    result = twilio.send_sms("+1987654321", "Hello from OLAI Twilio integration!")
    print(f"SMS result: {result}")
    
    # Test account info
    account_info = twilio.get_account_info()
    print(f"Account info: {account_info}")
