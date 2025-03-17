### **1. app.py** (Main Flask Application)
from flask import Flask
from backend.routes.user_routes import user_blueprint

def create_app():
    """
    This function initializes the Flask application,
    registers blueprints (routes), and configures settings.
    """
    app = Flask(__name__)
    app.config.from_pyfile('config.py')
    app.register_blueprint(user_blueprint)
    return app

if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)