from werkzeug.exceptions import BadRequest
from werkzeug.security import generate_password_hash, check_password_hash

from db import db
from managers.auth import AuthManager
from models.enums import RoleType
from models.user import UserModel


class UserManager:
    @staticmethod
    def register(user_data):
        user_data["password"] = generate_password_hash(
            user_data["password"], method="pbkdf2:sha256"
        )
        user_data["role"] = RoleType.user.name
        user = UserModel(**user_data)
        try:
            db.session.add(user)
            db.session.flush()
            return AuthManager.encode_token(user)
        except Exception as ex:
            raise BadRequest(str(ex))

    @staticmethod
    def login(data):
        user = db.session.execute(db.select(UserModel).filter_by(email=data["email"])).scalar()
        if not user or not check_password_hash(user.password, data["password"]):
            raise BadRequest("Invalid username or password.")
        return AuthManager.encode_token(user)
