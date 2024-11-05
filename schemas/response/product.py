from marshmallow import fields

from schemas.base import BaseProductSchema


class ProductResponseSchema(BaseProductSchema):
    """
    Schema for serializing a product response.
    """

    title = fields.String(required=True)
    description = fields.String(required=True)
    quantity = fields.Integer(required=True)
    price = fields.Float(required=True)
    photo_url = fields.String(required=True)
