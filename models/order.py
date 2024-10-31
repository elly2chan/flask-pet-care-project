from datetime import datetime

from sqlalchemy import func
from sqlalchemy.orm import Mapped, mapped_column, relationship

from db import db


class OrderModel(db.Model):
    __tablename__ = "orders"

    id: Mapped[int] = mapped_column(primary_key=True)
    created_on: Mapped[datetime] = mapped_column(db.DateTime, server_default=func.now())
    address: Mapped[str] = mapped_column(db.String(255), nullable=False)
    customer_id: Mapped[int] = mapped_column(db.Integer, nullable=False)
    product_id: Mapped[int] = mapped_column(db.Integer, nullable=False)
    status: Mapped[str] = mapped_column(db.Enum('pending', 'approved', 'rejected', name='state'), nullable=False)

    customer = db.relationship('UserModel', backref='orders')
    product = db.relationship('ProductModel', backref='orders')
