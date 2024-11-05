from flask import request
from flask_restful import Resource

from managers.auth import auth, AuthManager
from managers.user import UserManager
from schemas.request.auth import RegisterUserRequestSchema, LoginUserRequestSchema, PasswordChangeRequestSchema
from schemas.response.auth import ChangePasswordResponseSchema
from utils.decorators import validate_schema


class RegisterUser(Resource):
    """
    Endpoint for registering a new user.

    This endpoint allows a user to register by providing their username, email, and password.
    If successful, a token will be returned for the newly registered user.
    """
    @validate_schema(RegisterUserRequestSchema)
    def post(self):
        """
        Registers a new user.

        Validates the incoming registration request, creates a new user, and returns an authentication token.

        Returns:
            dict: A dictionary containing the authentication token.
            int: HTTP status code 201 for successful registration.
        """
        data = request.get_json()
        token = UserManager.register(data)
        return {"token": token}, 201


class LoginUser(Resource):
    """
    Endpoint for logging in an existing user.

    This endpoint allows a user to log in using their email and password. If successful, an authentication token will be returned.
    """
    @validate_schema(LoginUserRequestSchema)
    def post(self):
        """
        Logs in a user and returns an authentication token.

        Validates the incoming login request, logs the user in, and returns an authentication token.

        Returns:
            dict: A dictionary containing the authentication token.
        """
        data = request.get_json()
        token = UserManager.login(data)
        return {"token": token}


class ChangePassword(Resource):
    """
    Endpoint for changing the password of the currently authenticated user.

    This endpoint allows a user to change their password by providing their old and new passwords.
    The user must be authenticated to access this endpoint.
    """
    @auth.login_required
    @validate_schema(PasswordChangeRequestSchema)
    def post(self):
        """
        Changes the password of the authenticated user.

        Validates the request, verifies the old password, updates the password with the new one,
        and returns a success message.

        Returns:
            dict: A success message indicating the password change was successful.
            int: HTTP status code 200 for successful password change.
        """
        data = request.get_json()
        AuthManager.change_password(data)
        return ChangePasswordResponseSchema().dump({"message": "Password changed successfully"}), 200
