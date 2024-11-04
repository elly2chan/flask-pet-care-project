from marshmallow import validates, ValidationError, fields, validate

from models.enums import Gender, PetType
from schemas.base import BasePetSchema


class PetRequestSchema(BasePetSchema):
    gender = fields.String(required=True, validate=validate.OneOf([gender.value for gender in Gender]))
    date_of_birth = fields.Date(required=False)
    breed = fields.String(min_length=2, max_length=40, required=False)
    pet_type = fields.String(required=True, validate=validate.OneOf([type.value for type in PetType]))
    is_stray = fields.Boolean(required=False)
    european_passport = fields.Boolean(required=False)
    microchip = fields.Boolean(required=False)
    microchip_id = fields.String(min_length=10, max_length=20, required=False)

    @validates('name')
    def validate_name(self, value):
        if len(value) < 2:
            raise ValidationError("Name must be at least 2 characters long.")
