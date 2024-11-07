from marshmallow import Schema, fields
from marshmallow_enum import EnumField

from models.enums import Gender, PetType


class BaseUserSchema(Schema):
    """Base schema for user authentication with email and password fields."""

    email = fields.Email(required=True)
    password = fields.String(required=True)


class BasePetSchema(Schema):
    """
    Base schema for pet data including name, gender, type, and optional details like birth date, breed, and microchip.
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
    """Base schema for order data, requiring a delivery address."""

    address = fields.String(required=True)


class BaseProductSchema(Schema):
    """Base schema for product data, including title, description, quantity, price, and photo URL."""
    
    title = fields.String(required=True)
    description = fields.String(required=True)
    quantity = fields.Integer(required=True)
    price = fields.Float(required=True)
    photo_url = fields.String(required=True)
