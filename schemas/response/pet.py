from marshmallow import fields
from marshmallow_enum import EnumField

from models.enums import PetType, Gender
from schemas.base import BasePetSchema


class PetResponseSchema(BasePetSchema):
    """Schema for serializing pet response data."""

    name = fields.String(required=True)
    gender = EnumField(Gender, required=True, by_value=True)
    date_of_birth = fields.Date(required=False)
    breed = fields.String(required=False)
    pet_type = EnumField(PetType, required=True, by_value=True)
    is_stray = fields.Boolean(required=False)
    european_passport = fields.Boolean(required=False)
    microchip = fields.Boolean(required=False)
    microchip_id = fields.String(required=False)
