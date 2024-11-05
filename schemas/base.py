from marshmallow import Schema, fields
from marshmallow_enum import EnumField

from models.enums import Gender, PetType


class BaseUserSchema(Schema):
    """
    Base schema for user-related data.

    This schema defines the fields required for user authentication, such as email and password.

    Fields:
        email (str): The user's email address. This field is required and must be a valid email format.
        password (str): The user's password. This field is required.

    Example:
        {
            "email": "user@example.com",
            "password": "supersecret"
        }
    """
    email = fields.Email(required=True)
    password = fields.String(required=True)


class BasePetSchema(Schema):
    """
    Base schema for pet-related data.

    This schema defines the common attributes of a pet, including name, gender, type, and optional details
    such as date of birth, breed, microchip ID, etc.

    Fields:
        name (str): The name of the pet. This field is required.
        gender (str): The gender of the pet. This field is optional and uses an Enum for validation.
        date_of_birth (date): The pet's date of birth. This field is optional.
        breed (str): The breed of the pet. This field is optional.
        pet_type (str): The type of pet (e.g., dog, cat). This field is required and uses an Enum for validation.
        is_stray (bool): A flag indicating whether the pet is a stray. This field is optional.
        european_passport (bool): A flag indicating whether the pet has a European passport. This field is optional.
        microchip (bool): A flag indicating whether the pet has a microchip. This field is optional.
        microchip_id (str): The microchip ID of the pet. This field is optional.

    Example:
        {
            "name": "Buddy",
            "gender": "Male",
            "date_of_birth": "2018-05-21",
            "breed": "Golden Retriever",
            "pet_type": "Dog",
            "is_stray": False,
            "european_passport": False,
            "microchip": True,
            "microchip_id": "1234567890"
        }
    """
    name = fields.String(required=True)
    gender = EnumField(Gender, by_value=True)
    date_of_birth = fields.Date(allow_none=True)
    breed = fields.String(allow_none=True)
    pet_type = EnumField(PetType, by_value=True)
    is_stray = fields.Boolean(allow_none=True)
    european_passport = fields.Boolean(allow_none=True)
    microchip = fields.Boolean(allow_none=True)
    microchip_id = fields.String(allow_none=True)


class BaseOrderSchema(Schema):
    """
    Base schema for order-related data.

    This schema defines the common fields required to place an order, such as the delivery address.

    Fields:
        address (str): The delivery address for the order. This field is required.

    Example:
        {
            "address": "123 Pet Street, Pet City"
        }
    """
    address = fields.String(required=True)


class BaseProductSchema(Schema):
    """
    Base schema for product-related data.

    This schema defines the basic details of a product, such as title, description, quantity, price and photo URL.

    Fields:
        title (str): The title or name of the product. This field is required.
        description (str): A brief description of the product. This field is required.
        quantity (int): The quantity of the product. This field is required.
        price (float): The price of the product. This field is required.
        photo_url (str): A URL pointing to the product's image. This field is required.

    Example:
        {
            "title": "Cool Dog T-shirt",
            "description": "A comfortable cotton t-shirt for your dog.",
            "quantity": 19,
            "price": 10.50,
            "photo_url": "https://example.com/tshirt.jpg"
        }
    """
    title = fields.String(required=True)
    description = fields.String(required=True)
    quantity = fields.Integer(required=True)
    price = fields.Float(required=True)
    photo_url = fields.String(required=True)
