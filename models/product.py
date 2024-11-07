from datetime import datetime

from sqlalchemy import func
from sqlalchemy.orm import Mapped, mapped_column

from db import db


class ProductModel(db.Model):
    """
    Represents a product in the inventory system.

    This model defines the structure for a product, including essential details such as
    the product's title, description, quantity, price, and the timestamp when it was added.
    It also allows the system to track the product's image URL.

    Attributes:
        id (int): A unique identifier for the product. Automatically assigned by the database.
        title (str): The name or title of the product. Must be unique across the product catalog.
        description (str): A detailed description of the product, providing information about its features.
        quantity (int): The number of units available in stock. Defaults to 0 if not specified.
        price (float): The price of the product in the system's currency. Defaults to 0.0 if not specified.
        added_on (datetime): The timestamp of when the product was added to the system. Automatically set to the current time when created.
        photo_url (str): An optional URL linking to an image of the product, if available. Defaults to `None`.
    """

    __tablename__ = "products"

    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(db.String(100), nullable=False, unique=True)
    description: Mapped[str] = mapped_column(db.Text, nullable=False)
    quantity: Mapped[int] = mapped_column(db.Integer, nullable=False, default=0)
    price: Mapped[float] = mapped_column(db.Float, nullable=False, default=0.0)
    added_on: Mapped[datetime] = mapped_column(db.DateTime, server_default=func.now())
    photo_url: Mapped[str] = mapped_column(db.String(255), nullable=True)
