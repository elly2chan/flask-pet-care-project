from datetime import datetime

from sqlalchemy import func, Enum
from sqlalchemy.orm import Mapped, mapped_column, relationship

from db import db
from models.enums import Status


class OrderModel(db.Model):
    """
    Represents an order placed by a customer for a specific product in the system.

    This model captures the essential details of an order, including the customer who placed the order,
    the product being ordered, and the order's status throughout its lifecycle (e.g., pending, approved, rejected).

    Attributes:
        id (int): A unique identifier for the order.
        created_on (datetime): The date and time when the order was created. Automatically set to the current timestamp.
        address (str): The delivery address associated with the order.
        customer_id (int): The ID of the customer who placed the order. This is a foreign key referencing the `UserModel`.
        product_id (int): The ID of the ordered product. This is a foreign key referencing the `ProductModel`.
        product_title (str): The title/name of the ordered product, stored for reference.
        status (Status): The current status of the order, which can be one of the following: `pending`, `approved`, or `rejected`.
        quantity (int): The quantity of the product ordered. Defaults to 1 if not specified.
        total_price (float): The total price for the order, calculated based on the product price and quantity.
        customer (UserModel): A relationship to the `UserModel` representing the customer who placed the order.
        product (ProductModel): A relationship to the `ProductModel` representing the ordered product.

    Relationships:
        customer (UserModel): The customer who placed the order.
        product (ProductModel): The product that was ordered.
    """

    __tablename__ = "orders"

    id: Mapped[int] = mapped_column(primary_key=True)
    created_on: Mapped[datetime] = mapped_column(db.DateTime, default=func.now())
    address: Mapped[str] = mapped_column(db.String(255), nullable=False)

    customer_id: Mapped[int] = mapped_column(db.Integer, db.ForeignKey('users.id', ondelete='CASCADE'), nullable=False)
    product_id: Mapped[int] = mapped_column(db.Integer, db.ForeignKey('products.id'), nullable=False)

    product_title: Mapped[str] = mapped_column(db.String(255), nullable=False)
    status: Mapped[Status] = mapped_column(Enum(Status), default=Status.pending, nullable=False)
    quantity: Mapped[int] = mapped_column(db.Integer, nullable=False, default=1)
    total_price: Mapped[float] = mapped_column(db.Float, nullable=False, default=0.0)

    # Relationships
    customer = relationship('UserModel')
    product = relationship('ProductModel')
