from datetime import datetime

from sqlalchemy.orm import Mapped, mapped_column, relationship

from db import db
from models.enums import Gender, PetType
from models.user import UserModel


class PetModel(db.Model):
    __tablename__ = 'pets'

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(db.String(255), nullable=False)
    gender: Mapped[Gender] = mapped_column(db.Enum(Gender), nullable=False)
    date_of_birth: Mapped[datetime] = mapped_column(db.DateTime, nullable=True)
    breed: Mapped[str] = mapped_column(db.String(255), nullable=True)
    owner_name: Mapped[str] = mapped_column(db.String(255), nullable=False)
    pet_type: Mapped[PetType] = mapped_column(db.Enum(PetType), nullable=False)
    is_stray: Mapped[bool] = mapped_column(db.Boolean, nullable=True, default=False)
    european_passport: Mapped[bool] = mapped_column(db.Boolean, nullable=True, default=False)
    microchip: Mapped[bool] = mapped_column(db.Boolean, nullable=True, default=False)
    microchip_id: Mapped[str] = mapped_column(db.String, nullable=True)
    owner_id: Mapped[int] = mapped_column(db.Integer, db.ForeignKey("users.id"))
    owner_email: Mapped[str] = mapped_column(db.String, db.ForeignKey("users.email"))
    owner: Mapped["UserModel"] = relationship("UserModel")
