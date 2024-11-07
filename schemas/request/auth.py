from marshmallow import Schema, fields, validates, validates_schema, ValidationError
from password_strength import PasswordPolicy

from schemas.base import BaseUserSchema


class RegisterUserRequestSchema(BaseUserSchema):
    """
    Schema for user registration request, which validates the user's
    first name, last name, phone, iban and password.
    """

    first_name = fields.String(min_length=2, max_length=20, required=True, error_messages={
        'required': 'First name is required.',
        'min_length': 'First name must be between 2 and 20 characters.',
        'max_length': 'First name must be between 2 and 20 characters.'
    })

    last_name = fields.String(min_length=2, max_length=20, required=True, error_messages={
        'required': 'Last name is required.',
        'min_length': 'Last name must be between 2 and 20 characters.',
        'max_length': 'Last name must be between 2 and 20 characters.'
    })

    phone = fields.String(min_length=10, max_length=13, required=True, error_messages={
        'required': 'Phone number is required.',
        'min_length': 'Phone number must be between 10 and 13 digits.',
        'max_length': 'Phone number must be between 10 and 13 digits.'
    })

    iban = fields.String(min_length=10, max_length=40, required=False, error_messages={
        'required': 'IBAN is required.',
        'min_length': 'IBAN must be between 10 and 13 digits.',
        'max_length': 'IBAN must be between 10 and 13 digits.'
    })

    # Define password policy with at least one uppercase, one number, one special character
    policy = PasswordPolicy.from_names(
        uppercase=1,
        numbers=1,
        special=1,
        nonletters=1
    )

    @validates('password')
    def validate_password(self, value):
        """
        Validates the password to ensure it meets the defined policy requirements.
        """
        errors = self.policy.test(value)
        if errors:
            raise ValidationError(
                "Password must contain at least one uppercase letter, one number, and one special character."
            )


class LoginUserRequestSchema(BaseUserSchema):
    """
    Schema for user login request.
    No additional validation rules are applied to this schema.
    """
    pass


class PasswordChangeRequestSchema(Schema):
    """
    Schema for changing a user's password. It requires the old password
    and the new password with additional checks to ensure they are not the same.
    """
    old_password = fields.String(required=True, error_messages={'required': 'Old password is required.'})
    new_password = fields.String(required=True, error_messages={'required': 'New password is required.'})

    @validates_schema
    def validate_passwords(self, data, **kwargs):
        """
        Ensures that the new password is different from the old password.
        """
        if data["old_password"] == data["new_password"]:
            raise ValidationError(
                "New password cannot be the same as the old password.",
                field_names=["new_password"]
            )
