# Project_Setup
This repository automatically created a full stack project setup
# Project Structure

```
/flask_project
│── /backend
│   │── /controllers            # Handles requests and responses, acts as the business logic layer.
│   │   │── user_controller.py  # Handles user-related requests
│   │── /models                 # Contains database models using SQLAlchemy, defining tables and relationships.
│   │   │── user.py             # Defines User model
│   │── /routes                 # Defines API endpoints and maps URLs to specific functions.
│   │   │── user_routes.py      # Defines API endpoints for users
│   │── /services               # Implements core business logic, such as processing data before saving to DB.
│   │   │── user_service.py     # Implements user-related business logic
│   │── /middlewares            # Includes authentication, request logging, rate limiting, and error handling.
│   │   │── auth_middleware.py  # Handles authentication and logging
│   │── /static                 # Stores static files like CSS, JavaScript, images, and fonts.
│   │   │── styles.css          # CSS styles for the frontend
│   │── /templates              # Contains Jinja2 templates for rendering HTML pages dynamically.
│   │   │── index.html          # HTML template using Jinja2
│   │── config.py               # Configuration file for environment variables, database, and third-party services.
│   │── app.py                  # Main Flask application entry point, initializes the app and registers components.
│   │── wsgi.py                 # WSGI entry point for running the app with a production-ready server like Gunicorn.
│       
│── /migrations                 # Stores database migration files when using Flask-Migrate (Alembic under the hood).
│── /tests  
│   │── test_user.py            # Contains unit and integration tests for both backend and frontend.
│── /scripts                    # Contains automation scripts for deployment, database seeding, and backups.
│   │── build.sh                # Shell script to build the application.
│   │── deploy.sh               # Automates deployment process.
│   │── seed_db.py              # Populates the database with initial or test data.
│   │── backup_db.py            # Backs up the database for disaster recovery.
│       
│── .env                        # Environment variables file (NEVER commit to Git for security reasons).
│── requirements.txt            # Lists all dependencies needed for the Flask app.
│── run.py                      # Starts the application (alternative to app.py for local development).
│── README.md                   # Documentation explaining how to install, run, and contribute to the project.
│── Dockerfile                  # Defines how to containerize the application for deployment with Docker.
