from datetime import datetime

from sqlalchemy import func
from sqlalchemy.orm import Mapped, mapped_column, relationship

from db import db


class TransactionModel(db.Model):
    """
    Represents a financial transaction associated with an order.

    This model tracks a transaction's details, such as the quote ID, transfer ID,
    target account, transaction amount, and the timestamp of creation. It also
    maintains a relationship to the related order in the system, enabling the
    tracking of payments or financial actions tied to customer orders.

    Attributes:
        id (int): The unique identifier for the transaction (primary key).
        quote_id (str): The unique identifier for the quote associated with this transaction.
        transfer_id (str): The unique identifier for the transfer related to the transaction.
        target_account_id (str): The ID of the account receiving the transfer.
        amount (float): The monetary amount of the transaction.
        created_on (datetime): The timestamp when the transaction was created. Automatically set to the current time.
        order_id (int): Foreign key referencing the associated order.

    Relationships:
        order (OrderModel): A relationship to the `OrderModel`, representing the order associated with this transaction.
    """
    __tablename__ = 'transactions'

    id: Mapped[int] = mapped_column(primary_key=True)
    quote_id: Mapped[str] = mapped_column(db.String(100), nullable=False)
    transfer_id: Mapped[str] = mapped_column(db.String(100), nullable=False)
    target_account_id: Mapped[str] = mapped_column(db.String(100), nullable=False)
    amount: Mapped[float] = mapped_column(db.Float, nullable=False)
    created_on: Mapped[datetime] = mapped_column(db.DateTime, server_default=func.now())
    order_id: Mapped[int] = mapped_column(db.Integer, db.ForeignKey('orders.id'))

    # Relationships
    order = relationship('OrderModel')
