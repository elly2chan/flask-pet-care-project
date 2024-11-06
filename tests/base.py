import pytest

from config import create_app
from db import db
from managers.auth import AuthManager


# Utility function to generate tokens (mocked in some cases for isolation)
def generate_token(user):
    return AuthManager.encode_token(user)


# Fixture to create the app instance
@pytest.fixture(scope="module")
def app():
    app = create_app("config.TestingConfig")
    yield app


# Fixture to create the Flask test client
@pytest.fixture(scope="function")
def client(app):
    """Create a test client for the app."""
    return app.test_client()


# Fixture to set up the database before each test
@pytest.fixture(scope="function")
def database(app):
    """Create and tear down the database."""
    with app.app_context():
        db.create_all()  # Create all tables
        yield db  # Provide the db session to the test
        db.session.remove()
        db.drop_all()  # Drop all tables after the test
