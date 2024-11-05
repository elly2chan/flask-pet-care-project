from datetime import datetime

from sqlalchemy import func, Date
from sqlalchemy.orm import Mapped, mapped_column, relationship

from db import db
from models.enums import Gender, PetType


class PetModel(db.Model):
    """
    Represents a pet owned by a user.

    Attributes:
        id (int): The unique identifier for the pet.
        name (str): The name of the pet.
        gender (Gender): The gender of the pet (either 'male' or 'female').
        date_of_birth (datetime.date): The pet's date of birth.
        breed (str): The breed of the pet.
        owner_id (int): The ID of the pet's owner (foreign key to the 'users' table).
        owner_email (str): The email of the pet's owner.
        pet_type (PetType): The type of pet (e.g., dog, cat).
        is_stray (bool): Indicates if the pet is a stray (default is False).
        european_passport (bool): Indicates if the pet has a European passport (default is False).
        microchip (bool): Indicates if the pet has a microchip (default is False).
        microchip_id (str): The microchip ID of the pet, if applicable.
        added_on (datetime): The timestamp when the pet record was added (default is current time).
        owner (UserModel): The pet's owner, represented by a relationship with the 'UserModel'.
    """

    __tablename__ = 'pets'

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(db.String(255), nullable=False)
    gender: Mapped[Gender] = mapped_column(db.Enum(Gender), nullable=False)
    date_of_birth: Mapped[datetime.date] = mapped_column(Date, nullable=True)
    breed: Mapped[str] = mapped_column(db.String(255), nullable=True)

    owner_id: Mapped[int] = mapped_column(db.Integer, db.ForeignKey('users.id', ondelete='CASCADE'), nullable=False)
    owner_email: Mapped[str] = mapped_column(db.String(255), nullable=False)

    pet_type: Mapped[PetType] = mapped_column(db.Enum(PetType), nullable=False)
    is_stray: Mapped[bool] = mapped_column(db.Boolean, nullable=False, default=False)
    european_passport: Mapped[bool] = mapped_column(db.Boolean, nullable=False, default=False)
    microchip: Mapped[bool] = mapped_column(db.Boolean, nullable=False, default=False)
    microchip_id: Mapped[str] = mapped_column(db.String(20), nullable=True)

    added_on: Mapped[datetime] = mapped_column(db.DateTime, server_default=func.now())

    # Relationships
    owner = relationship('UserModel')
