from datetime import datetime

from sqlalchemy import func
from sqlalchemy.orm import Mapped, mapped_column

from db import db
from models.enums import Gender, PetType


class PetModel(db.Model):
    __tablename__ = 'pets'

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(db.String(255), nullable=False)
    gender: Mapped[Gender] = mapped_column(db.Enum(Gender), nullable=False)
    date_of_birth: Mapped[datetime] = mapped_column(db.DateTime, nullable=True)
    breed: Mapped[str] = mapped_column(db.String(255), nullable=True)
    owner_id: Mapped[int] = mapped_column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    owner_email: Mapped[str] = mapped_column(db.String(255), nullable=False)
    pet_type: Mapped[PetType] = mapped_column(db.Enum(PetType), nullable=False)
    is_stray: Mapped[bool] = mapped_column(db.Boolean, nullable=True)
    european_passport: Mapped[bool] = mapped_column(db.Boolean, nullable=True)
    microchip: Mapped[bool] = mapped_column(db.Boolean, nullable=True)
    microchip_id: Mapped[str] = mapped_column(db.String(), nullable=True)
    added_on: Mapped[datetime] = mapped_column(db.DateTime, server_default=func.now())

    owner = db.relationship('UserModel', foreign_keys=[owner_id])
