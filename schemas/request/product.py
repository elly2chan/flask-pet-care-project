from marshmallow import fields, validates, ValidationError, validate

from schemas.base import BaseProductSchema


class ProductRequestSchema(BaseProductSchema):
    """Schema for validating product data before adding or updating a product."""

    title = fields.String(
        required=True,
        validate=validate.Length(min=2, max=100),
        description="The title of the product, between 2 and 100 characters long."
    )

    description = fields.String(
        required=True,
        validate=validate.Length(min=10),
        description="The description of the product, at least 10 characters long."
    )

    quantity = fields.Integer(
        required=True,
        validate=validate.Range(min=1),
        description="The quantity of the product, must be a positive integer."
    )

    price = fields.Float(
        required=True,
        validate=validate.Range(min=0.1),
        description="The price of the product, must be a positive integer."
    )

    photo_url = fields.String(
        required=True,
        validate=validate.URL(),
        description="The URL of the product photo, must be a valid URL."
    )

    @validates('title')
    def validate_title(self, value):
        """Custom validation for title to ensure it meets certain criteria."""
        if not value.strip():
            raise ValidationError("Title cannot be empty or just spaces.")

    @validates('description')
    def validate_description(self, value):
        """Custom validation for description to ensure it’s sufficiently detailed."""
        if len(value.split()) < 2:  # Ensure description has at least 2 words
            raise ValidationError("Description should be at least two words long.")
