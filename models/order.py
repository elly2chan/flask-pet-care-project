from datetime import datetime

from sqlalchemy import func
from sqlalchemy.orm import Mapped, mapped_column, relationship

from db import db


class OrderModel(db.Model):
    __tablename__ = "orders"

    id: Mapped[int] = mapped_column(primary_key=True)
    created_on: Mapped[datetime] = mapped_column(db.DateTime, server_default=func.now())
    address: Mapped[str] = mapped_column(db.String(255), nullable=False)
    customer_id: Mapped[int] = mapped_column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    product_id: Mapped[int] = mapped_column(db.Integer, db.ForeignKey('products.id'), nullable=False)
    status: Mapped[str] = mapped_column(db.Enum('pending', 'approved', 'rejected', name='state'), nullable=False)

    customer = db.relationship('UserModel')
    product = db.relationship('ProductModel')
