from marshmallow import validates, ValidationError, fields
from schemas.base import BaseOrderSchema


class OrderRequestSchema(BaseOrderSchema):
    """
    Schema for validating the request data to place a new order.

    This schema requires a `product_id` and validates the `address` field to ensure
    that the address is at least 5 characters long.
    """
    product_id = fields.Integer(required=True)

    @validates('address')
    def validate_address(self, value):
        """
        Validates the address field.

        The address must be at least 5 characters long. If the provided address
        does not meet this requirement, a validation error will be raised.

        Args:
            value (str): The address to validate.

        Raises:
            ValidationError: If the address is shorter than 5 characters.
        """
        if len(value) < 5:
            raise ValidationError("Address must be at least 5 characters long.")
