from datetime import datetime

from sqlalchemy import func
from sqlalchemy.orm import Mapped, mapped_column

from db import db
from models.enums import Status


class OrderModel(db.Model):
    __tablename__ = "orders"

    id: Mapped[int] = mapped_column(primary_key=True)
    created_on: Mapped[datetime] = mapped_column(db.DateTime, server_default=func.now())
    address: Mapped[str] = mapped_column(db.String(255), nullable=False)
    customer_id: Mapped[int] = mapped_column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    product_id: Mapped[int] = mapped_column(db.Integer, db.ForeignKey('products.id'), nullable=False)
    product_title: Mapped[str] = mapped_column(db.String(255), nullable=False)
    status: Mapped[Status] = mapped_column(
        db.Enum(Status),
        default=Status.pending.name,
        nullable=False
    )

    customer = db.relationship('UserModel')
    product = db.relationship('ProductModel')
