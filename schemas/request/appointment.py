from marshmallow import Schema, fields, validate


class AppointmentRequestSchema(Schema):
    """
    Validates data for booking a pet appointment.
    """

    appointment_datetime = fields.DateTime(
        required=True, format="%Y-%m-%d %H:%M:%S",
        error_messages={"required": "Appointment datetime is required."}
    )
    pet_name = fields.String(
        required=True,
        error_messages={"required": "Pet name is required."}
    )
    appointment_reason = fields.String(
        required=True,
        validate=validate.Length(min=5),
        error_messages={"required": "Appointment reason is required.",
                        "min_length": "Reason must be at least 5 characters long."}
    )
