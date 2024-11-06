from sqlalchemy.orm import Mapped, mapped_column

from db import db
from models.enums import RoleType


class UserModel(db.Model):
    """
    Represents a user in the system.

    Attributes:
        id (int): Unique identifier for the user (primary key).
        email (str): The user's email address. This is unique and cannot be null.
        password (str): The user's password (hashed).
        first_name (str): The user's first name. This is an optional field.
        last_name (str): The user's last name. This is an optional field.
        phone (str): The user's phone number. This is an optional field.
        role (str): The user's role in the system (default is 'user'). This is a required field.
        iban (str): The user's iban. This is a required field.
    """

    __tablename__ = 'users'

    id: Mapped[int] = mapped_column(primary_key=True)
    email: Mapped[str] = mapped_column(db.String(120), unique=True, nullable=False)
    password: Mapped[str] = mapped_column(db.String(255), nullable=False)
    first_name: Mapped[str] = mapped_column(db.String(255), nullable=True)
    last_name: Mapped[str] = mapped_column(db.String(255), nullable=True)
    phone: Mapped[str] = mapped_column(db.String(20), nullable=True)
    role: Mapped[RoleType] = mapped_column(
        db.Enum(RoleType),
        default=RoleType.user.name,
        nullable=False
    )
    iban: Mapped[str] = mapped_column(db.String(255), nullable=False, default="BE41967053490210",
                                      server_default="BE41967053490210")
