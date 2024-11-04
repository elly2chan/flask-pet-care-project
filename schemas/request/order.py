from marshmallow import validates, ValidationError

from schemas.base import BaseOrderSchema


class OrderRequestSchema(BaseOrderSchema):
    @validates('address')
    def validate_address(self, value):
        if len(value) < 5:
            raise ValidationError("Address must be at least 5 characters long.")
