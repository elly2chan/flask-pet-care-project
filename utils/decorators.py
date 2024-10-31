from functools import wraps

from flask import request
from werkzeug.exceptions import BadRequest, Forbidden

from managers.auth import auth


def validate_schema(schema_name):
    def decorator(f):
        @wraps(f)
        def decorated_function(*args, **kwargs):
            schema = schema_name()
            errors = schema.validate(request.get_json())
            if errors:
                raise BadRequest(f"Invalid fields {errors}")
            return f(*args, **kwargs)
        return decorated_function
    return decorator


def permission_required(required_role):
    def decorator(func):
        @wraps(func)
        def decorated_func(*args, **kwargs):
            current_user = auth.current_user()
            if current_user.role != required_role:
                raise Forbidden("You do not have permission to access this resource.")
            return func(*args, **kwargs)
        return decorated_func
    return decorator
