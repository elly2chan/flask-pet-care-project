from marshmallow import fields

from schemas.base import BasePetSchema


class PetResponseSchema(BasePetSchema):
    name = fields.String(required=True)
    gender = fields.String(required=True)
    date_of_birth = fields.Date(required=False)
    breed = fields.String(required=False)
    pet_type = fields.String(required=True)
    is_stray = fields.Boolean(required=False)
    european_passport = fields.Boolean(required=False)
    microchip = fields.Boolean(required=False)
    microchip_id = fields.String(required=False)
