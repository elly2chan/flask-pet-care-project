from marshmallow import fields

from schemas.base import BaseProductSchema


class ProductResponseSchema(BaseProductSchema):
    id = fields.Integer(required=True)
    added_on = fields.DateTime(required=True)
