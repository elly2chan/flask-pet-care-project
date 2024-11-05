from marshmallow import Schema, fields, validates_schema, ValidationError, validates
from password_strength import PasswordPolicy

from schemas.base import BaseUserSchema


class RegisterUserRequestSchema(BaseUserSchema):
    first_name = fields.String(min_length=2, max_length=20, required=True)
    last_name = fields.String(min_length=2, max_length=20, required=True)
    phone = fields.String(min_length=10, max_length=13, required=True)

    policy = PasswordPolicy.from_names(
        uppercase=1,
        numbers=1,
        special=1,
        nonletters=1,
    )

    @validates('password')
    def validate_password(self, value):
        errors = self.policy.test(value)
        if errors:
            raise ValidationError("Password must have uppercase letters, numbers and special characters.")


class LoginUserRequestSchema(BaseUserSchema):
    pass


class PasswordChangeRequestSchema(Schema):
    old_password = fields.String(required=True)
    new_password = fields.String(required=True)

    @validates_schema
    def validate_passwords(self, data, **kwargs):
        if data["old_password"] == data["new_password"]:
            raise ValidationError("New password cannot be the same as the old password.",
                                  field_names=["new_password"], )
