from datetime import datetime

from sqlalchemy import func
from sqlalchemy.orm import Mapped, mapped_column

from db import db


class ProductModel(db.Model):
    __tablename__ = "products"

    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(db.String(100), nullable=False)
    description: Mapped[str] = mapped_column(db.Text, nullable=False)
    amount: Mapped[int] = mapped_column(db.Integer, nullable=False)
    added_on: Mapped[datetime] = mapped_column(db.DateTime, server_default=func.now())
    photo_url: Mapped[str] = mapped_column(db.String(255), nullable=False)
