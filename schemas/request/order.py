import re

from marshmallow import validates, ValidationError, fields, validate

from schemas.base import BaseOrderSchema


class OrderRequestSchema(BaseOrderSchema):
    """
    Schema to validate order requests. It includes the product ID and address validation.
    Ensures the provided address meets basic validation rules (e.g., length >= 5).
    """

    product_id = fields.Integer(required=True, error_messages={'required': 'Product ID is required.'})
    quantity = fields.Integer(
        required=True,
        validate=validate.Range(min=1),
        description="The quantity of products in the order, must be a positive integer."
    )

    @validates('address')
    def validate_address(self, value):
        """
        Validates the address to ensure it meets the minimum length requirement.
        The address must be at least 5 characters long.
        """
        if len(value) < 5:
            raise ValidationError("Address must be at least 5 characters long.")

        # Regex for a more specific address pattern
        address_pattern = r"^[a-zA-Z0-9\s,.'-]+$"
        if not re.match(address_pattern, value):
            raise ValidationError("Address contains invalid characters.")
