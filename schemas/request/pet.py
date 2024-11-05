from marshmallow import validates, ValidationError, fields, validate

from models.enums import Gender, PetType
from schemas.base import BasePetSchema


class PetRequestSchema(BasePetSchema):
    """
    Schema for validating incoming requests to create or update a pet's information.

    This schema ensures that the required fields are provided and are in the correct format,
    including validations for 'gender', 'pet_type', and 'microchip_id'. Optional fields like
    'breed' and 'date_of_birth' are also validated for correct lengths or formats where applicable.
    """

    gender = fields.String(
        required=True,
        validate=validate.OneOf([gender.value for gender in Gender]),
        error_messages={'required': 'Gender is required.', 'invalid': 'Invalid gender value.'}
    )

    date_of_birth = fields.Date(
        required=False,
        missing=None,
        error_messages={'invalid': 'Date of birth must be in the format YYYY-MM-DD.'}
    )

    breed = fields.String(
        min_length=2,
        max_length=40,
        required=False,
        error_messages={
            'min_length': 'Breed must be at least 2 characters long.',
            'max_length': 'Breed must be no longer than 40 characters.'
        }
    )

    pet_type = fields.String(
        required=True,
        validate=validate.OneOf([type.value for type in PetType]),
        error_messages={'required': 'Pet type is required.', 'invalid': 'Invalid pet type value.'}
    )

    is_stray = fields.Boolean(
        required=False,
        missing=False,
        error_messages={'invalid': 'Invalid value for is_stray. It must be a boolean.'}
    )

    european_passport = fields.Boolean(
        required=False,
        missing=False,
        error_messages={'invalid': 'Invalid value for european_passport. It must be a boolean.'}
    )

    microchip = fields.Boolean(
        required=False,
        missing=False,
        error_messages={'invalid': 'Invalid value for microchip. It must be a boolean.'}
    )

    microchip_id = fields.String(
        min_length=10,
        max_length=20,
        required=False,
        validate=validate.Regexp(r'^[a-zA-Z0-9]+$', error="Microchip ID must be alphanumeric."),
        error_messages={
            'min_length': 'Microchip ID must be at least 10 characters long.',
            'max_length': 'Microchip ID must be no longer than 20 characters.',
            'invalid': 'Microchip ID must be alphanumeric.'
        }
    )

    @validates('name')
    def validate_name(self, value):
        """
        Validates the pet's name to ensure it is at least 2 characters long.
        """
        if len(value) < 2:
            raise ValidationError("Name must be at least 2 characters long.")
