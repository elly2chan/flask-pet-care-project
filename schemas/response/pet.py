from marshmallow import fields

from schemas.base import BasePetSchema


class PetResponseSchema(BasePetSchema):
    id = fields.Integer(required=True)
    owner_id = fields.Integer(required=True)
    owner_email = fields.String(required=True)
