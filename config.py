import os

from decouple import config
from flask import Flask
from flask_cors import CORS
from flask_migrate import Migrate
from flask_restful import Api

from db import db
from resources.routes import routes

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))


class ProductionConfig:
    """
    Configuration settings for the production environment.

    Attributes:
        FLASK_ENV (str): Environment for Flask (production).
        DEBUG (bool): Disable debugging in production.
        TESTING (bool): Disable testing in production.
        SQLALCHEMY_DATABASE_URI (str): Database URI for connecting to the PostgreSQL database.
    """
    FLASK_ENV = "prod"
    DEBUG = False
    TESTING = False
    SQLALCHEMY_DATABASE_URI = (
        f"postgresql://{config('DB_USER')}:{config('DB_PASSWORD')}"
        f"@localhost:{config('DB_PORT')}/{config('DB_NAME')}"
    )


class DevelopmentConfig:
    """
    Configuration settings for the development environment.

    Attributes:
        FLASK_ENV (str): Environment for Flask (development).
        DEBUG (bool): Enable debugging in development.
        TESTING (bool): Enable testing in development.
        SQLALCHEMY_DATABASE_URI (str): Database URI for connecting to the PostgreSQL database.
    """
    FLASK_ENV = "development"
    DEBUG = True
    TESTING = True
    SQLALCHEMY_DATABASE_URI = (
        f"postgresql://{config('DB_USER')}:{config('DB_PASSWORD')}"
        f"@localhost:{config('DB_PORT')}/{config('DB_NAME')}"
    )


class TestingConfig:
    """
    Configuration settings for the testing environment.

    Attributes:
        FLASK_ENV (str): Environment for Flask (testing).
        DEBUG (bool): Enable debugging in testing.
        TESTING (bool): Enable testing in testing.
        SQLALCHEMY_DATABASE_URI (str): Database URI for connecting to the test PostgreSQL database.
    """
    FLASK_ENV = "testing"
    DEBUG = True
    TESTING = True
    SQLALCHEMY_DATABASE_URI = (
        f"postgresql://{config('DB_USER')}:{config('DB_PASSWORD')}"
        f"@localhost:{config('DB_PORT')}/{config('TEST_DB_NAME')}"
    )


def create_app(environment):
    """
    Creates and configures the Flask app based on the provided environment.

    This function initializes the Flask application, sets up database connections,
    configures CORS, adds routes to the API, and integrates Flask-Migrate for database migrations.

    Args:
        environment (str): The environment configuration to use (e.g., ProductionConfig,
                            DevelopmentConfig, or TestingConfig).

    Returns:
        Flask: The initialized Flask app with all necessary configurations.
    """
    app = Flask(__name__)
    app.config.from_object(environment)  # Load configuration based on environment
    db.init_app(app)  # Initialize SQLAlchemy with the Flask app
    migrate = Migrate(app, db)  # Initialize Flask-Migrate for database migrations
    api = Api(app)  # Initialize Flask-RESTful API

    CORS(app)  # Enable Cross-Origin Resource Sharing (CORS)

    # Add the routes from the routes module to the API
    [api.add_resource(*route) for route in routes]

    return app
