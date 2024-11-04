from marshmallow import validates, ValidationError, fields

from schemas.base import BaseOrderSchema


class OrderRequestSchema(BaseOrderSchema):
    product_id = fields.Integer(required=True)

    @validates('address')
    def validate_address(self, value):
        if len(value) < 5:
            raise ValidationError("Address must be at least 5 characters long.")
