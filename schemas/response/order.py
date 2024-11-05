from marshmallow import fields
from marshmallow_enum import EnumField

from models.enums import Status
from schemas.base import BaseOrderSchema


class OrderResponseSchema(BaseOrderSchema):
    """
    Schema for serializing order data in the response.
    """

    id = fields.Integer(required=True)
    created_on = fields.DateTime(required=True)
    customer_id = fields.Integer(required=True)
    product_id = fields.Integer(required=True)
    product_title = fields.String(required=True)
    customer_name = fields.String()

    status = EnumField(Status, required=True, by_value=True)

    quantity = fields.Integer(required=True)
    total_price = fields.Float(required=True)
