from functools import wraps
from flask import request, jsonify
from clerk_backend_api import Clerk
from clerk_backend_api.jwks_helpers import authenticate_request, AuthenticateRequestOptions
from .config import config_map

def require_auth(f):
    @wraps(f)
    def wrapper(*args, **kwargs):
        sdk = Clerk(bearer_auth=config_map['development'].CLERK_SECRET_KEY)
        # Authenticate the incoming Flask request
        try:
            state = sdk.authenticate_request(
                request,
                AuthenticateRequestOptions(
                    authorized_parties=[config_map['development'].FRONTEND_URL]
                )
            )
            if not state.is_signed_in:
                return jsonify({"error": str(state.reason)}), 401
            request.user = state.payload
        except Exception as e:
            print(f"Authentication error: {str(e)}")
            return jsonify({"error": "Authentication failed"}), 401
        return f(*args, **kwargs)
    return wrapper

def assign_role(user_id):
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