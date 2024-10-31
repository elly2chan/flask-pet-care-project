from marshmallow import Schema, fields, validates_schema, ValidationError

from schemas.base import BaseUserSchema


class RequestRegisterUserSchema(BaseUserSchema):
    first_name = fields.String(min_length=2, max_length=20, required=True)
    last_name = fields.String(min_length=2, max_length=20, required=True)
    phone = fields.String(min_length=10, max_length=13, required=True)


class RequestLoginUserSchema(BaseUserSchema):
    pass


class PasswordChangeSchema(Schema):
    old_password = fields.String(required=True)
    new_password = fields.String(required=True)

    @validates_schema
    def validate_passwords(self, data, **kwargs):
        if data["old_password"] == data["new_password"]:
            raise ValidationError("New password cannot be the same as the old password.",
                                  field_names=["new_password"], )
