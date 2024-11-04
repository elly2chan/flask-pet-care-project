from marshmallow import fields
from marshmallow_enum import EnumField

from models.enums import Status
from schemas.base import BaseOrderSchema


class OrderResponseSchema(BaseOrderSchema):
    id = fields.Integer(required=True)
    created_on = fields.DateTime(required=True)
    customer_id = fields.Integer(required=True)
    product_id = fields.Integer(required=True)
    status = EnumField(Status, by_value=True)
