from datetime import datetime

from sqlalchemy.orm import Mapped, mapped_column, relationship

from db import db


class AppointmentModel(db.Model):
    """
    Represents an appointment for a pet at a veterinary clinic or similar service.

    This model defines the structure of an appointment, including details such as the scheduled date and time,
    the associated pet, and the reason for the appointment.

    Attributes:
        id (int): A unique identifier for the appointment. Automatically assigned by the database.
        appointment_datetime (datetime): The date and time of the appointment. This field is required and must be unique.
        pet_id (int): The ID of the pet associated with the appointment. This is a foreign key referencing the `pets` table.
        pet_name (str): The name of the pet associated with the appointment. This is a required field.
        appointment_reason (str): A detailed description of the reason for the appointment. This is a required field.

    Relationships:
        pet (PetModel): The pet associated with the appointment. This creates a one-to-many relationship with the
        `PetModel` class.
    """

    __tablename__ = "appointments"

    id: Mapped[int] = mapped_column(primary_key=True)
    appointment_datetime: Mapped[datetime] = mapped_column(db.DateTime, nullable=False, unique=True)
    owner_id: Mapped[int] = mapped_column(db.Integer, db.ForeignKey('users.id', ondelete='CASCADE'), nullable=False)
    owner_name: Mapped[str] = mapped_column(db.String(255), nullable=False)
    owner_phone: Mapped[str] = mapped_column(db.String(20), nullable=False)
    pet_id: Mapped[int] = mapped_column(db.Integer, db.ForeignKey('pets.id', ondelete='CASCADE'), nullable=False)
    pet_name: Mapped[str] = mapped_column(db.String, nullable=False)
    appointment_reason: Mapped[str] = mapped_column(db.Text, nullable=False)

    pet = relationship('PetModel')
    owner = relationship('UserModel')
