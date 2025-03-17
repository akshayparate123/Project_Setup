### **2. user_routes.py** (Routes for User API)
from flask import Blueprint, jsonify
from backend.services.user_service import get_all_users

user_blueprint = Blueprint('user', __name__)

@user_blueprint.route('/users', methods=['GET'])
def fetch_users():
    """
    API endpoint to fetch all users from the database.
    """
    users = get_all_users()
    return jsonify(users)
