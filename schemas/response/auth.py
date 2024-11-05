from marshmallow import Schema, fields


class ChangePasswordResponseSchema(Schema):
    """
    Schema for the response when a user's password is successfully changed.

    Example Response:
        {
            "message": "Password changed successfully"
        }
    """

    message = fields.String(required=True)
