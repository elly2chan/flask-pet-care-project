from marshmallow import fields
from marshmallow_enum import EnumField

from models.enums import Status
from schemas.base import BaseOrderSchema


class OrderResponseSchema(BaseOrderSchema):
    """
    Schema for serializing an order response.

    This schema represents the structure of an order response, which includes
    details about an order such as the order ID, creation date, associated customer
    and product, and the order's current status.

    Fields:
        id (int): The unique identifier for the order. This is a required field.
        created_on (datetime): The timestamp when the order was created. This is a required field.
        customer_id (int): The ID of the customer who placed the order. This is a required field.
        product_id (int): The ID of the product associated with the order. This is a required field.
        status (Status): The current status of the order. This is represented as an enum from the `Status` enum class.

    Example Response:
        {
            "id": 123,
            "created_on": "2024-11-01T15:30:00",
            "customer_id": 456,
            "product_id": 789,
            "status": "pending"
        }
    """
    id = fields.Integer(required=True)
    created_on = fields.DateTime(required=True)
    customer_id = fields.Integer(required=True)
    product_id = fields.Integer(required=True)
    status = EnumField(Status, by_value=True)
