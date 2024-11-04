from marshmallow import validates, ValidationError

from schemas.base import BasePetSchema


class PetRequestSchema(BasePetSchema):
    @validates('name')
    def validate_name(self, value):
        if len(value) < 2:
            raise ValidationError("Name must be at least 2 characters long.")
