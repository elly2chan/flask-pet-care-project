from datetime import datetime

from sqlalchemy import func
from sqlalchemy.orm import Mapped, mapped_column, relationship

from db import db
from models.enums import State
from models.product import ProductModel
from models.user import UserModel


class OrderModel(db.Model):
    __tablename__ = "orders"

    id: Mapped[int] = mapped_column(primary_key=True)
    created_on: Mapped[datetime] = mapped_column(db.DateTime, server_default=func.now())
    address: Mapped[str] = mapped_column(db.String(255), nullable=False)
    customer_id: Mapped[int] = mapped_column(db.Integer, db.ForeignKey("users.id"))
    customer: Mapped["UserModel"] = relationship("UserModel")
    product_id: Mapped[int] = mapped_column(db.Integer, db.ForeignKey("products.id"))
    product_title: Mapped[str] = mapped_column(db.String(100), db.ForeignKey("products.title"))
    product_description: Mapped[str] = mapped_column(db.Text, db.ForeignKey("products.description"))
    product: Mapped["ProductModel"] = relationship("ProductModel")
    status: Mapped[State] = mapped_column(
        db.Enum(State),
        nullable=False,
        default=State.pending.name
    )
