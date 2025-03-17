### **3. user_service.py** (Business Logic for Users)
from backend.models.user import User

def get_all_users():
    """
    This function retrieves all users from the database.
    """
    return [user.to_dict() for user in User.query.all()]
