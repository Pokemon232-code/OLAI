#!/usr/bin/env python3
"""
Stripe Integration Module
Integrates with Stripe payment processing API
"""

import stripe
import os
import json
from typing import Dict, List, Any, Optional
from datetime import datetime
import logging

logger = logging.getLogger(__name__)

class StripeIntegration:
    """Stripe payment processing integration"""
    
    def __init__(self, config: Dict[str, Any] = None):
        self.config = config or {}
        self.api_key = self.config.get("api_key") or os.getenv("STRIPE_API_KEY")
        self.webhook_secret = self.config.get("webhook_secret") or os.getenv("STRIPE_WEBHOOK_SECRET")
        
        if not self.api_key:
            logger.warning("Stripe API key not provided")
        else:
            stripe.api_key = self.api_key
    
    def create_payment_intent(self, amount: int, currency: str = "usd", customer_id: str = None, 
                            metadata: Dict[str, Any] = None) -> Dict[str, Any]:
        """Create a payment intent for processing payments"""
        try:
            intent_data = {
                "amount": amount,
                "currency": currency,
                "automatic_payment_methods": {"enabled": True}
            }
            
            if customer_id:
                intent_data["customer"] = customer_id
            
            if metadata:
                intent_data["metadata"] = metadata
            
            intent = stripe.PaymentIntent.create(**intent_data)
            
            return {
                "status": "success",
                "payment_intent": {
                    "id": intent.id,
                    "client_secret": intent.client_secret,
                    "amount": intent.amount,
                    "currency": intent.currency,
                    "status": intent.status
                },
                "message": "Payment intent created successfully",
                "timestamp": datetime.now().isoformat()
            }
        except stripe.error.StripeError as e:
            logger.error(f"Stripe payment intent creation failed: {e}")
            return {"status": "error", "error": str(e)}
        except Exception as e:
            logger.error(f"Unexpected error creating payment intent: {e}")
            return {"status": "error", "error": str(e)}
    
    def create_customer(self, email: str, name: str = None, metadata: Dict[str, Any] = None) -> Dict[str, Any]:
        """Create a customer in Stripe"""
        try:
            customer_data = {"email": email}
            
            if name:
                customer_data["name"] = name
            
            if metadata:
                customer_data["metadata"] = metadata
            
            customer = stripe.Customer.create(**customer_data)
            
            return {
                "status": "success",
                "customer": {
                    "id": customer.id,
                    "email": customer.email,
                    "name": customer.name,
                    "created": customer.created
                },
                "message": "Customer created successfully",
                "timestamp": datetime.now().isoformat()
            }
        except stripe.error.StripeError as e:
            logger.error(f"Stripe customer creation failed: {e}")
            return {"status": "error", "error": str(e)}
        except Exception as e:
            logger.error(f"Unexpected error creating customer: {e}")
            return {"status": "error", "error": str(e)}
    
    def create_subscription(self, customer_id: str, price_id: str, metadata: Dict[str, Any] = None) -> Dict[str, Any]:
        """Create a subscription for a customer"""
        try:
            subscription_data = {
                "customer": customer_id,
                "items": [{"price": price_id}]
            }
            
            if metadata:
                subscription_data["metadata"] = metadata
            
            subscription = stripe.Subscription.create(**subscription_data)
            
            return {
                "status": "success",
                "subscription": {
                    "id": subscription.id,
                    "customer": subscription.customer,
                    "status": subscription.status,
                    "current_period_start": subscription.current_period_start,
                    "current_period_end": subscription.current_period_end
                },
                "message": "Subscription created successfully",
                "timestamp": datetime.now().isoformat()
            }
        except stripe.error.StripeError as e:
            logger.error(f"Stripe subscription creation failed: {e}")
            return {"status": "error", "error": str(e)}
        except Exception as e:
            logger.error(f"Unexpected error creating subscription: {e}")
            return {"status": "error", "error": str(e)}
    
    def create_invoice(self, customer_id: str, items: List[Dict[str, Any]], metadata: Dict[str, Any] = None) -> Dict[str, Any]:
        """Create an invoice for a customer"""
        try:
            invoice_data = {
                "customer": customer_id,
                "auto_advance": True
            }
            
            if metadata:
                invoice_data["metadata"] = metadata
            
            invoice = stripe.Invoice.create(**invoice_data)
            
            # Add invoice items
            for item in items:
                stripe.InvoiceItem.create(
                    customer=customer_id,
                    invoice=invoice.id,
                    amount=item.get("amount"),
                    currency=item.get("currency", "usd"),
                    description=item.get("description")
                )
            
            # Finalize and send the invoice
            invoice.finalize_invoice()
            
            return {
                "status": "success",
                "invoice": {
                    "id": invoice.id,
                    "customer": invoice.customer,
                    "amount_due": invoice.amount_due,
                    "currency": invoice.currency,
                    "status": invoice.status,
                    "hosted_invoice_url": invoice.hosted_invoice_url
                },
                "message": "Invoice created and sent successfully",
                "timestamp": datetime.now().isoformat()
            }
        except stripe.error.StripeError as e:
            logger.error(f"Stripe invoice creation failed: {e}")
            return {"status": "error", "error": str(e)}
        except Exception as e:
            logger.error(f"Unexpected error creating invoice: {e}")
            return {"status": "error", "error": str(e)}
    
    def process_refund(self, payment_intent_id: str, amount: int = None, reason: str = "requested_by_customer") -> Dict[str, Any]:
        """Process a refund for a payment"""
        try:
            refund_data = {
                "payment_intent": payment_intent_id,
                "reason": reason
            }
            
            if amount:
                refund_data["amount"] = amount
            
            refund = stripe.Refund.create(**refund_data)
            
            return {
                "status": "success",
                "refund": {
                    "id": refund.id,
                    "amount": refund.amount,
                    "currency": refund.currency,
                    "status": refund.status,
                    "reason": refund.reason
                },
                "message": "Refund processed successfully",
                "timestamp": datetime.now().isoformat()
            }
        except stripe.error.StripeError as e:
            logger.error(f"Stripe refund processing failed: {e}")
            return {"status": "error", "error": str(e)}
        except Exception as e:
            logger.error(f"Unexpected error processing refund: {e}")
            return {"status": "error", "error": str(e)}
    
    def get_payment_methods(self, customer_id: str) -> Dict[str, Any]:
        """Get payment methods for a customer"""
        try:
            payment_methods = stripe.PaymentMethod.list(customer=customer_id, type="card")
            
            return {
                "status": "success",
                "payment_methods": [
                    {
                        "id": pm.id,
                        "type": pm.type,
                        "card": {
                            "brand": pm.card.brand,
                            "last4": pm.card.last4,
                            "exp_month": pm.card.exp_month,
                            "exp_year": pm.card.exp_year
                        }
                    } for pm in payment_methods.data
                ],
                "timestamp": datetime.now().isoformat()
            }
        except stripe.error.StripeError as e:
            logger.error(f"Stripe payment methods retrieval failed: {e}")
            return {"status": "error", "error": str(e)}
        except Exception as e:
            logger.error(f"Unexpected error retrieving payment methods: {e}")
            return {"status": "error", "error": str(e)}
    
    def create_price(self, amount: int, currency: str = "usd", product_name: str = None, 
                    recurring: bool = False, interval: str = "month") -> Dict[str, Any]:
        """Create a price for a product"""
        try:
            # Create product first if product_name is provided
            product = None
            if product_name:
                product = stripe.Product.create(name=product_name)
            
            price_data = {
                "unit_amount": amount,
                "currency": currency
            }
            
            if product:
                price_data["product"] = product.id
            
            if recurring:
                price_data["recurring"] = {"interval": interval}
            
            price = stripe.Price.create(**price_data)
            
            return {
                "status": "success",
                "price": {
                    "id": price.id,
                    "unit_amount": price.unit_amount,
                    "currency": price.currency,
                    "recurring": price.recurring,
                    "product": price.product
                },
                "message": "Price created successfully",
                "timestamp": datetime.now().isoformat()
            }
        except stripe.error.StripeError as e:
            logger.error(f"Stripe price creation failed: {e}")
            return {"status": "error", "error": str(e)}
        except Exception as e:
            logger.error(f"Unexpected error creating price: {e}")
            return {"status": "error", "error": str(e)}
    
    def handle_webhook(self, payload: str, signature: str) -> Dict[str, Any]:
        """Handle Stripe webhook events"""
        try:
            event = stripe.Webhook.construct_event(
                payload, signature, self.webhook_secret
            )
            
            # Handle different event types
            if event['type'] == 'payment_intent.succeeded':
                return self._handle_payment_succeeded(event['data']['object'])
            elif event['type'] == 'payment_intent.payment_failed':
                return self._handle_payment_failed(event['data']['object'])
            elif event['type'] == 'customer.subscription.created':
                return self._handle_subscription_created(event['data']['object'])
            elif event['type'] == 'customer.subscription.deleted':
                return self._handle_subscription_deleted(event['data']['object'])
            else:
                return {
                    "status": "info",
                    "message": f"Unhandled event type: {event['type']}",
                    "timestamp": datetime.now().isoformat()
                }
        except ValueError as e:
            logger.error(f"Invalid payload in webhook: {e}")
            return {"status": "error", "error": "Invalid payload"}
        except stripe.error.SignatureVerificationError as e:
            logger.error(f"Invalid signature in webhook: {e}")
            return {"status": "error", "error": "Invalid signature"}
        except Exception as e:
            logger.error(f"Webhook handling failed: {e}")
            return {"status": "error", "error": str(e)}
    
    def _handle_payment_succeeded(self, payment_intent: Dict[str, Any]) -> Dict[str, Any]:
        """Handle successful payment event"""
        return {
            "status": "success",
            "event_type": "payment_intent.succeeded",
            "payment_intent_id": payment_intent.get("id"),
            "amount": payment_intent.get("amount"),
            "message": "Payment succeeded",
            "timestamp": datetime.now().isoformat()
        }
    
    def _handle_payment_failed(self, payment_intent: Dict[str, Any]) -> Dict[str, Any]:
        """Handle failed payment event"""
        return {
            "status": "success",
            "event_type": "payment_intent.payment_failed",
            "payment_intent_id": payment_intent.get("id"),
            "error": payment_intent.get("last_payment_error", {}).get("message"),
            "message": "Payment failed",
            "timestamp": datetime.now().isoformat()
        }
    
    def _handle_subscription_created(self, subscription: Dict[str, Any]) -> Dict[str, Any]:
        """Handle subscription created event"""
        return {
            "status": "success",
            "event_type": "customer.subscription.created",
            "subscription_id": subscription.get("id"),
            "customer_id": subscription.get("customer"),
            "message": "Subscription created",
            "timestamp": datetime.now().isoformat()
        }
    
    def _handle_subscription_deleted(self, subscription: Dict[str, Any]) -> Dict[str, Any]:
        """Handle subscription deleted event"""
        return {
            "status": "success",
            "event_type": "customer.subscription.deleted",
            "subscription_id": subscription.get("id"),
            "customer_id": subscription.get("customer"),
            "message": "Subscription deleted",
            "timestamp": datetime.now().isoformat()
        }

# Factory function
def create_stripe_integration(config: Dict[str, Any] = None) -> StripeIntegration:
    """Create a Stripe integration instance"""
    return StripeIntegration(config)

# Example usage
if __name__ == "__main__":
    # Example configuration
    config = {
        "api_key": "your_stripe_api_key",
        "webhook_secret": "your_stripe_webhook_secret"
    }
    
    stripe_integration = create_stripe_integration(config)
    
    # Test creating a payment intent
    result = stripe_integration.create_payment_intent(2000, "usd")  # $20.00
    print(f"Payment intent result: {result}")
    
    # Test creating a customer
    customer = stripe_integration.create_customer("test@example.com", "Test Customer")
    print(f"Customer result: {customer}")
