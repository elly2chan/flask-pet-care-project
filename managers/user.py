from werkzeug.exceptions import BadRequest
from werkzeug.security import generate_password_hash, check_password_hash

from db import db
from managers.auth import AuthManager
from models.enums import RoleType
from models.user import UserModel


class UserManager:
    @staticmethod
    def register(user_data):
        """Registers a new user."""
        hashed_password = generate_password_hash(user_data["password"], method="pbkdf2:sha256")
        user_data["password"] = hashed_password
        user_data["role"] = RoleType.user.name
        user = UserModel(**user_data)

        try:
            db.session.add(user)
            db.session.flush()
            return AuthManager.encode_token(user)
        except Exception as ex:
            raise BadRequest(f"User registration failed: {ex}.")

    @staticmethod
    def login(data):
        """Logs in a user."""
        user = db.session.execute(db.select(UserModel).filter_by(email=data["email"])).scalar()

        if not user:
            raise BadRequest("Invalid username or password.")

        if not check_password_hash(user.password, data["password"]):
            raise BadRequest("Invalid username or password.")

        return AuthManager.encode_token(user)
