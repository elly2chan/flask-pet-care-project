import pytest
from werkzeug.exceptions import NotFound

from db import db
from models import UserModel
from tests.base import app, database, client
from tests.factories import UserFactory
from utils.files import get_json_file_content

USER_PASSWORD = 'test'


def test_register_user(client, database):
    """
    Test user registration.
    """
    # Ensure there are no users initially
    users = UserModel.query.all()
    assert len(users) == 0

    # Load user data from a JSON file
    user_data = get_json_file_content('test_data/resources_test_data/user_data.json')

    # Send POST request to register the user
    response = client.post("/register", json=user_data)
    assert response.status_code == 201

    # Ensure the token is returned in the response
    token = response.json["token"]
    assert token is not None

    # Verify that the user was created in the database
    email = user_data["email"]
    password = user_data["password"]
    user = UserModel.query.filter_by(email=email).first()
    assert user is not None
    assert user.email == email
    assert user.password != password  # Ensure password is hashed


def test_register_user_missing_fields(client, database):
    """
    Test user registration with missing required fields.
    """
    user_data = {
        "email": "test@example.com"  # Missing password
    }

    response = client.post("/register", json=user_data)
    assert response.status_code == 400
    assert "password" in response.json["message"]  # Password is required


def login_data():
    """
    Helper function to generate login data for the first user in the database.
    """
    user = db.session.query(UserModel).first()

    data = {
        "email": user.email,
        "password": USER_PASSWORD
    }

    return user, data


def test_login_user(client, database):
    """
    Test user login.
    """
    # Create a user with a predefined password using the factory
    UserFactory(password=USER_PASSWORD)

    # Prepare login data
    user, data = login_data()

    # Send POST request to log in
    response = client.post("/login", json=data)
    assert response.status_code == 200

    # Ensure the token is returned in the response
    token = response.json["token"]
    assert token is not None


def test_login_user_incorrect_password(client, database):
    """
    Test user login with an incorrect password.
    """
    UserFactory(password=USER_PASSWORD)

    # Attempt to log in with an incorrect password
    user, data = login_data()
    data["password"] = "wrongpassword"  # Modify password

    response = client.post("/login", json=data)
    assert response.status_code == 400  # Unauthorized
    assert "Invalid username or password." in response.json["message"]


def test_change_password(client, database):
    """
    Test password change functionality.
    """
    # Create a user with a predefined password using the factory
    UserFactory(password=USER_PASSWORD)

    # Prepare login data
    _, data = login_data()

    # Send POST request to log in
    response = client.post("/login", json=data)
    token = response.json["token"]

    # Set the authorization header with the token
    headers = {"Authorization": f"Bearer {token}"}

    # Prepare data for changing the password
    change_password_data = {
        "old_password": USER_PASSWORD,
        "new_password": USER_PASSWORD + 'test'
    }

    # Send POST request to change the password
    response = client.post("users/change_password", json=change_password_data, headers=headers)
    assert response.status_code == 200
    assert response.json == {'message': 'Password changed successfully'}
