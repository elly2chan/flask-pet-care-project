from marshmallow import Schema, fields


class AppointmentResponseSchema(Schema):
    """
    Schema for serializing appointment data in the response.
    """

    id = fields.Integer(required=True)
    appointment_datetime = fields.String(required=True)
    owner_id = fields.Integer(required=True)
    owner_name = fields.String(required=True)
    owner_phone = fields.String(required=True)
    pet_id = fields.Integer(required=True)
    pet_name = fields.String(required=True)
    appointment_reason = fields.String(required=True)
