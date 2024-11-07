from sqlalchemy.orm import Mapped, mapped_column

from db import db
from models.enums import RoleType


class UserModel(db.Model):
    """
    Represents a user in the system.

    This model contains user details including their personal information,
    authentication credentials, role, and bank account (IBAN) information.

    Attributes:
        id (int): Unique identifier for the user (primary key).
        email (str): The user's email address. This field must be unique and cannot be null.
        password (str): The hashed password for the user, used for authentication.
        first_name (str): The user's first name (optional).
        last_name (str): The user's last name (optional).
        phone (str): The user's phone number (optional).
        role (RoleType): The user's role in the system (default is 'user').
                         This determines the level of access the user has within the system.
        iban (str): The user's International Bank Account Number (IBAN).
                    This field is required and defaults to "BE41967053490210" if not provided.
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
