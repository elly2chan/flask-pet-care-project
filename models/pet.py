from datetime import datetime

from sqlalchemy.orm import Mapped, mapped_column, relationship

from db import db
from models.enums import Gender, PetType
from models.user import UserModel


class PetModel(db.Model):
    __tablename__ = 'pets'

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(db.String(255), nullable=False)
    gender: Mapped[str] = mapped_column(db.Enum('female', 'male', name='gender'), nullable=False)
    date_of_birth: Mapped[datetime] = mapped_column(db.DateTime, nullable=True)
    breed: Mapped[str] = mapped_column(db.String(255), nullable=True)
    owner_id: Mapped[int] = mapped_column(db.Integer, nullable=False)
    owner_email: Mapped[str] = mapped_column(db.String(255), nullable=False)
    pet_type: Mapped[str] = mapped_column(db.Enum('dog', 'cat', name='pettype'), nullable=False)
    is_stray: Mapped[bool] = mapped_column(db.Boolean, nullable=True)
    european_passport: Mapped[bool] = mapped_column(db.Boolean, nullable=True)
    microchip: Mapped[bool] = mapped_column(db.Boolean, nullable=True)
    microchip_id: Mapped[str] = mapped_column(db.String(), nullable=True)

    owner = db.relationship('UserModel', foreign_keys=[owner_id], backref='pets')
