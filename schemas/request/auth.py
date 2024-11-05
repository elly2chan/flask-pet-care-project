from marshmallow import Schema, fields, validates_schema, ValidationError, validates
from password_strength import PasswordPolicy

from schemas.base import BaseUserSchema


class RegisterUserRequestSchema(BaseUserSchema):
    """
    Schema for validating the request data to register a new user.

    This schema ensures that the incoming data includes required fields like first name,
    last name, phone number, and a password that meets security policies.
    """
    first_name = fields.String(min_length=2, max_length=20, required=True)
    last_name = fields.String(min_length=2, max_length=20, required=True)
    phone = fields.String(min_length=10, max_length=13, required=True)

    # Password policy enforcing at least one uppercase letter, one number, one special character,
    # and one non-letter character.
    policy = PasswordPolicy.from_names(
        uppercase=1,
        numbers=1,
        special=1,
        nonletters=1,
    )

    @validates('password')
    def validate_password(self, value):
        """
        Validates the password according to the defined policy.

        The password must meet the following requirements:
        - At least one uppercase letter
        - At least one number
        - At least one special character
        - At least one non-letter character

        Args:
            value (str): The password value to validate.

        Raises:
            ValidationError: If the password does not meet the policy requirements.
        """
        errors = self.policy.test(value)
        if errors:
            raise ValidationError("Password must have uppercase letters, numbers, and special characters.")


class LoginUserRequestSchema(BaseUserSchema):
    """
    Schema for validating the request data to log in a user.

    This schema can be extended later if login-specific fields are needed,
    but currently, it just inherits the basic user schema.
    """
    pass


class PasswordChangeRequestSchema(Schema):
    """
    Schema for validating the request data to change a user's password.

    This schema requires the old and new password and ensures that both are not the same.
    """
    old_password = fields.String(required=True)
    new_password = fields.String(required=True)

    @validates_schema
    def validate_passwords(self, data, **kwargs):
        """
        Validates that the old password is not the same as the new password.

        Args:
            data (dict): The data dictionary containing both 'old_password' and 'new_password'.

        Raises:
            ValidationError: If the old password is the same as the new password.
        """
        if data["old_password"] == data["new_password"]:
            raise ValidationError("New password cannot be the same as the old password.",
                                  field_names=["new_password"])
