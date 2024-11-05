from sqlalchemy import func
from sqlalchemy.orm import relationship

from db import db


class TransactionModel(db.Model):
    """
    Represents a transaction record in the database.

    This model stores details about a financial transaction, including identifiers
    for the quote, transfer, and target account, the transaction amount, the creation
    timestamp, and a relationship to an associated order.

    Attributes:
        id (int): The primary key of the transaction.
        quote_id (str): The unique identifier for the quote associated with the transaction.
        transfer_id (str): The unique identifier for the transfer related to the transaction.
        target_account_id (str): The target account receiving the transfer.
        amount (float): The amount of the transaction.
        created_on (datetime): Timestamp for when the transaction was created.
        order_id (int): Foreign key to the associated order.
        order (OrderModel): Relationship to the related order (potentially for a complaint).
    """
    __tablename__ = 'transactions'

    id = db.Column(db.Integer, primary_key=True)
    quote_id = db.Column(db.String(100), nullable=False)
    transfer_id = db.Column(db.String(100), nullable=False)
    target_account_id = db.Column(db.String(100), nullable=False)
    amount = db.Column(db.Float, nullable=False)
    created_on = db.Column(db.DateTime, server_default=func.now())
    order_id = db.Column(db.Integer, db.ForeignKey('orders.id'))

    # Relationships
    order = relationship('OrderModel')
