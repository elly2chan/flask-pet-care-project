from marshmallow import fields

from schemas.base import BasePetSchema

class PetResponseSchema(BasePetSchema):
    """
    Schema for serializing a pet response.

    This schema represents the structure of a pet response, including details
    about the pet such as its name, gender, date of birth, breed, type, and
    various attributes related to the pet's status (e.g., whether it is a stray,
    whether it has a microchip, and whether it has an European passport).

    Fields:
        name (str): The name of the pet. This is a required field.
        gender (str): The gender of the pet. This is a required field.
        date_of_birth (date): The date of birth of the pet. This is an optional field.
        breed (str): The breed of the pet. This is an optional field.
        pet_type (str): The type of pet (e.g., dog, cat). This is a required field.
        is_stray (bool): Indicates if the pet is a stray. This is an optional field.
        european_passport (bool): Indicates if the pet has a European passport. This is an optional field.
        microchip (bool): Indicates if the pet has a microchip. This is an optional field.
        microchip_id (str): The ID of the pet's microchip. This is an optional field.

    Example Response:
        {
            "name": "Buddy",
            "gender": "Male",
            "date_of_birth": "2018-04-20",
            "breed": "Golden Retriever",
            "pet_type": "dog",
            "is_stray": false,
            "european_passport": true,
            "microchip": true,
            "microchip_id": "1234567890ABC"
        }
    """
    name = fields.String(required=True)
    gender = fields.String(required=True)
    date_of_birth = fields.Date(required=False)
    breed = fields.String(required=False)
    pet_type = fields.String(required=True)
    is_stray = fields.Boolean(required=False)
    european_passport = fields.Boolean(required=False)
    microchip = fields.Boolean(required=False)
    microchip_id = fields.String(required=False)
