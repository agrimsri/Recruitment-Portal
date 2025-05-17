from functools import wraps
from flask import request, jsonify
import jwt
from jwt import PyJWKClient
from .config import config_map

# Initializing JWKS client with the JWKS URL from the configuration
jwks_url = config_map['development'].CLERK_JWKS_URL
jwk_client = PyJWKClient(jwks_url)

def token_required(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        auth_header = request.headers.get('Authorization', '')
        if not auth_header.startswith('Bearer '):
            return jsonify({"message": "Token is missing"})

        token = auth_header.split(' ', 1)[1]
        try:
            # Retrieve the RSA public key from JWKS
            public_key = jwk_client.get_signing_key_from_jwt(token).key

            # Decode and verify signature using RS256
            decoded = jwt.decode(
                token,
                public_key,
                algorithms=["RS256"],
                options={"verify_signature": True, "verify_aud": False}
            )

            # Attach token data to request context
            request.token_data = decoded
            request.clerk_id = decoded.get('sub') or decoded.get('clerk_id')
            request.public_metadata = decoded.get('public_metadata')
            return func(*args, **kwargs)

        except jwt.ExpiredSignatureError:
            return jsonify({"message": "Token has expired"})
        except jwt.InvalidTokenError as e:
            return jsonify({"message": f"Invalid token: {str(e)}"})
        except Exception as e:
            return jsonify({"message": f"Authentication error: {str(e)}"}), 500

    return wrapper

def roles_accepted(*roles):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            if not hasattr(request, 'public_metadata'):
                return jsonify({"message": "Unauthorized - No user metadata found"})
            
            user_role = request.public_metadata.get('role')
            if not user_role:
                return jsonify({"message": "Unauthorized - No role specified"})
            
            if user_role not in roles:
                return jsonify({"message": "Unauthorized - Insufficient role"})
                
            return func(*args, **kwargs)
        return wrapper
    return decorator
