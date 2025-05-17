from flask_restful import Resource
from flask import request, current_app
from app.models.user import User
from app.extensions import db
from svix.webhooks import Webhook, WebhookVerificationError
import os
from dotenv import load_dotenv
from clerk_backend_api import Clerk
from app.config import config_map

load_dotenv()

class ClerkWebhook(Resource):
    def post(self):
        """Handle Clerk webhook events"""
        payload_raw = request.get_data()
            
        webhook_secret = os.getenv('WEBHOOK_SECRET') or current_app.config.get('WEBHOOK_SECRET')
        if not webhook_secret:
            current_app.logger.error("Webhook secret is not configured")
            return {'error': 'Webhook secret not configured'}, 500
            
        try:
            wh = Webhook(webhook_secret)
            msg = wh.verify(payload_raw, request.headers)
        except WebhookVerificationError as e:
            current_app.logger.error(f"Webhook verification failed: {str(e)}")
            return {'error': 'Webhook verification failed'}, 401

        payload = request.get_json()

        event_type = payload.get('type')

        if event_type == 'user.created':
            # Create user in our database
            user_data = payload['data']
            try:
                user = User(
                    clerk_id=user_data['id'],
                    email=user_data['email_addresses'][0]['email_address'],
                    role=user_data['unsafe_metadata']['role'] if 'unsafe_metadata' in user_data and 'role' in user_data['unsafe_metadata'] else 'user',
                )
                db.session.add(user)
                db.session.commit()
            except KeyError as e:
                current_app.logger.error(f"Missing data in user creation payload: {str(e)}")
                return {'error': 'Invalid user data'}, 400
            except Exception as e:  # Catch any other exceptions
                current_app.logger.error(f"Error creating user: {str(e)}")
                return {'error': 'Error creating user'}, 500
                
            
        elif event_type == 'user.updated':
            # Update user in our database
            user_data = payload['data']
            user = User.query.filter_by(clerk_id=user_data['id']).first()
            if user:
                user.email = user_data['email_addresses'][0]['email_address']
                db.session.commit()
                
        elif event_type == 'user.deleted':
            # Delete user from our database
            user_data = payload['data']
            user = User.query.filter_by(clerk_id=user_data['id']).first()
            if user:
                db.session.delete(user)
                db.session.commit()
                
        return {'message': 'Webhook processed successfully'}, 200

class UpdateMetadata(Resource):
    def post(self):
        """Update user metadata in the database"""
        data = request.get_json()
        
        if not data or 'user_id' not in data:
            return {'error': 'user_id is required'}, 400
        
        user_id = data['user_id']
            
        with Clerk(
            bearer_auth=config_map['development'].CLERK_SECRET_KEY,
        ) as clerk:
        
            user = clerk.users.get(user_id=user_id)

            if user.unsafe_metadata.get("role") == "hr":
                res = clerk.users.update_metadata(user_id=user_id, public_metadata={
                    "role": "hr",
                }, unsafe_metadata={
                    "role": None,
                })
            else:
                res = clerk.users.update_metadata(user_id=user_id, public_metadata={
                    "role": "user",
                }, unsafe_metadata={
                    "role": None,
                })
