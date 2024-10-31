from flask import request
from flask_restful import Resource

from managers.auth import auth, AuthManager
from managers.user import UserManager
from schemas.request.auth import RequestRegisterUserSchema, RequestLoginUserSchema, PasswordChangeSchema
from utils.decorators import validate_schema


class RegisterUser(Resource):
    @validate_schema(RequestRegisterUserSchema)
    def post(self):
        data = request.get_json()
        token = UserManager.register(data)
        return {"token": token}, 201


class LoginUser(Resource):
    @validate_schema(RequestLoginUserSchema)
    def post(self):
        data = request.get_json()
        token = UserManager.login(data)
        return {"token": token}


class ChangePassword(Resource):
    @auth.login_required
    @validate_schema(PasswordChangeSchema)
    def post(self):
        data = request.get_json()
        AuthManager.change_password(data)
        return 204
