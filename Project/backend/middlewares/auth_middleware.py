### **5. auth_middleware.py** (Middleware for Authentication)
from flask import request, jsonify

def token_required(f):
    """
    Decorator to check if the user provides a valid token.
    """
    def decorated(*args, **kwargs):
        token = request.headers.get('Authorization')
        if not token:
            return jsonify({"message": "Token is missing!"}), 403
        return f(*args, **kwargs)
    return decorated
