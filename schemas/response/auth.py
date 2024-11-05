from marshmallow import Schema, fields

class ChangePasswordResponseSchema(Schema):
    """
    Schema for the response when a user's password is successfully changed.

    This schema defines the structure of the response sent after a user
    has successfully changed their password. It contains a message field
    that indicates the status of the password change operation.

    Fields:
        message (str): A message indicating the success or failure of
                       the password change process. This is a required field.

    Example Response:
        {
            "message": "Password changed successfully"
        }
    """
    message = fields.String(required=True)
