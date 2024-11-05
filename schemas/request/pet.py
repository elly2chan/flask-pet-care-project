from marshmallow import validates, ValidationError, fields, validate
from models.enums import Gender, PetType
from schemas.base import BasePetSchema


class PetRequestSchema(BasePetSchema):
    """
    Schema for validating the request data to add or update a pet.

    This schema validates the following fields:
    - `gender`: A required string that must be one of the predefined `Gender` values.
    - `date_of_birth`: An optional field to specify the pet's date of birth.
    - `breed`: An optional field to specify the breed of the pet (with a minimum length of 2 and a maximum of 40 characters).
    - `pet_type`: A required string that must be one of the predefined `PetType` values.
    - `is_stray`: An optional boolean field indicating whether the pet is a stray.
    - `european_passport`: An optional boolean indicating if the pet has a European passport.
    - `microchip`: An optional boolean indicating if the pet has a microchip.
    - `microchip_id`: An optional string representing the microchip ID (must be between 10 to 20 characters long).
    """
    gender = fields.String(
        required=True,
        validate=validate.OneOf([gender.value for gender in Gender])
    )
    date_of_birth = fields.Date(required=False)
    breed = fields.String(min_length=2, max_length=40, required=False)
    pet_type = fields.String(
        required=True,
        validate=validate.OneOf([type.value for type in PetType])
    )
    is_stray = fields.Boolean(required=False)
    european_passport = fields.Boolean(required=False)
    microchip = fields.Boolean(required=False)
    microchip_id = fields.String(min_length=10, max_length=20, required=False)

    @validates('name')
    def validate_name(self, value):
        """
        Validates the name field.

        The name must be at least 2 characters long. If the provided name
        does not meet this requirement, a validation error will be raised.

        Args:
            value (str): The name of the pet.

        Raises:
            ValidationError: If the name is shorter than 2 characters.
        """
        if len(value) < 2:
            raise ValidationError("Name must be at least 2 characters long.")
