from marshmallow import Schema, fields


class ChangePasswordResponseSchema(Schema):
    message = fields.String(required=True)
