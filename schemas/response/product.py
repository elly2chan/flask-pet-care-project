from marshmallow import fields

from schemas.base import BaseProductSchema

class ProductResponseSchema(BaseProductSchema):
    """
    Schema for serializing a product response.

    This schema represents the structure of a product response, including details
    about the product such as its title, description, amount, and photo URL. This schema
    will be used when serializing product data to be returned in API responses.

    Fields:
        title (str): The title of the product. This is a required field.
        description (str): A brief description of the product. This is a required field.
        amount (int): The amount of the product (e.g., price or stock count). This is a required field.
        photo_url (str): The URL of the product's photo or image. This is a required field.

    Example Response:
        {
            "title": "Cool Dog T-shirt",
            "description": "A comfortable cotton t-shirt for your dog with a cool design.",
            "amount": 19,
            "photo_url": "https://example.com/photo.jpg"
        }
    """
    title = fields.String(required=True)
    description = fields.String(required=True)
    amount = fields.Integer(required=True)
    photo_url = fields.String(required=True)
