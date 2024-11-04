from marshmallow import fields

from schemas.base import BaseProductSchema


class ProductResponseSchema(BaseProductSchema):
    title = fields.String(required=True)
    description = fields.String(required=True)
    amount = fields.Integer(required=True)
    photo_url = fields.String(required=True)
