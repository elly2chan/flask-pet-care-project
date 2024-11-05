from datetime import datetime

from sqlalchemy import func, Enum
from sqlalchemy.orm import Mapped, mapped_column, relationship

from db import db
from models.enums import Status


class OrderModel(db.Model):
    """
    Represents an order placed by a customer for a specific product.

    Attributes:
        id (int): The unique identifier for the order.
        created_on (datetime): The timestamp when the order was created.
        address (str): The delivery address for the order.
        customer_id (int): The ID of the customer who placed the order.
        product_id (int): The ID of the product that was ordered.
        product_title (str): The title of the product ordered.
        status (Status): The current status of the order (e.g., pending, approved, rejected).
        customer (UserModel): The customer who placed the order, represented by a relationship.
        product (ProductModel): The product that was ordered, represented by a relationship.
    """

    __tablename__ = "orders"

    id: Mapped[int] = mapped_column(primary_key=True)
    created_on: Mapped[datetime] = mapped_column(db.DateTime, default=func.now())
    address: Mapped[str] = mapped_column(db.String(255), nullable=False)
    customer_id: Mapped[int] = mapped_column(db.Integer, db.ForeignKey('users.id', ondelete='CASCADE'), nullable=False)
    product_id: Mapped[int] = mapped_column(db.Integer, db.ForeignKey('products.id', ondelete='CASCADE'),
                                            nullable=False)
    product_title: Mapped[str] = mapped_column(db.String(255), nullable=False)
    status: Mapped[Status] = mapped_column(Enum(Status), default=Status.pending, nullable=False)

    customer = relationship('UserModel', backref='orders', cascade="all, delete-orphan")
    product = relationship('ProductModel', backref='orders', cascade="all, delete-orphan")
