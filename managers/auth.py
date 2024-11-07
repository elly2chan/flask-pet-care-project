from datetime import datetime, timedelta

import jwt
import pytz
from decouple import config
from flask_httpauth import HTTPTokenAuth
from werkzeug.exceptions import Unauthorized
from werkzeug.security import check_password_hash, generate_password_hash

from db import db
from models.user import UserModel

auth = HTTPTokenAuth(scheme="Bearer")


class AuthManager:
    @staticmethod
    def encode_token(user):
        """Generates a JWT token for a user."""
        try:
            payload = {
                "sub": user.id,
                "exp": datetime.now(pytz.utc) + timedelta(days=2),
                "role": user.role if isinstance(user.role, str) else user.role.name,
            }
            token = jwt.encode(payload, key=config('SECRET_KEY'), algorithm='HS256')
            return token
        except Exception as e:
            raise Exception(f'Token generation failed: {e}')

    @staticmethod
    def decode_token(token):
        """Validates a JWT token and retrieves the user information."""
        try:
            info = jwt.decode(jwt=token, key=config('SECRET_KEY'), algorithms=['HS256'])
            return info['sub'], info['role']
        except jwt.ExpiredSignatureError:
            raise Unauthorized('Token has expired.')
        except jwt.InvalidTokenError:
            raise Unauthorized('Invalid token.')
        except Exception as e:
            raise Unauthorized(f'Token decoding failed: {str(e)}')

    @staticmethod
    def change_password(pass_data):
        """Changes the password for the current authenticated user."""
        try:
            if 'old_password' not in pass_data or 'new_password' not in pass_data:
                raise ValueError('Both old and new passwords must be provided.')

            user = auth.current_user()

            if not check_password_hash(user.password, pass_data['old_password']):
                raise Unauthorized('Incorrect old password.')

            new_password_hash = generate_password_hash(pass_data['new_password'], method='pbkdf2:sha256')
            user.password = new_password_hash
            db.session.flush()
        except Exception as e:
            raise Exception(f'Password change failed: {e}')


@auth.verify_token
def verify_token(token):
    """Verifies the token and retrieves the user from the database."""
    try:
        user_id, user_role = AuthManager.decode_token(token)
        user = db.session.query(UserModel).filter_by(id=user_id).first()
        if user:
            return user
        raise Unauthorized('User not found.')
    except Exception as e:
        raise Unauthorized(f'Invalid or missing token: {str(e)}')
