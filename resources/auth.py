from flask import request
from flask_restful import Resource

from managers.auth import auth, AuthManager
from managers.user import UserManager
from schemas.request.auth import RegisterUserRequestSchema, LoginUserRequestSchema, PasswordChangeRequestSchema
from schemas.response.auth import ChangePasswordResponseSchema
from utils.decorators import validate_schema


class RegisterUser(Resource):
    @validate_schema(RegisterUserRequestSchema)
    def post(self):
        """
        Register a new user and return an authentication token.

        :return: dict with token, status code 201
        """
        data = request.get_json()
        token = UserManager.register(data)
        return {"token": token}, 201


class LoginUser(Resource):
    @validate_schema(LoginUserRequestSchema)
    def post(self):
        """
        Log in an existing user and return an authentication token.

        :return: dict with token
        """
        data = request.get_json()
        token = UserManager.login(data)
        return {"token": token}


class ChangePassword(Resource):
    @auth.login_required
    @validate_schema(PasswordChangeRequestSchema)
    def post(self):
        """
        Change the password of the authenticated user.

        :return: success message, status code 200
        """
        data = request.get_json()
        AuthManager.change_password(data)
        return ChangePasswordResponseSchema().dump({"message": "Password changed successfully"}), 200
