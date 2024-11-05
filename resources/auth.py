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
        data = request.get_json()
        token = UserManager.register(data)
        return {"token": token}, 201


class LoginUser(Resource):
    @validate_schema(LoginUserRequestSchema)
    def post(self):
        data = request.get_json()
        token = UserManager.login(data)
        return {"token": token}


class ChangePassword(Resource):
    @auth.login_required
    @validate_schema(PasswordChangeRequestSchema)
    def post(self):
        data = request.get_json()
        AuthManager.change_password(data)
        return ChangePasswordResponseSchema().dump({"message": "Password changed successfully"}), 200
