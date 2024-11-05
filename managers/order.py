from werkzeug.exceptions import NotFound, InternalServerError

from db import db
from managers.product import ProductManager
from models import ProductModel, OrderModel, TransactionModel
from models.enums import Status
from services.wise import WiseService

wise_service = WiseService()


class OrderManager:
    @staticmethod
    def issue_transaction(amount, first_name, last_name, iban, order_id):
        quote = wise_service.create_quote(amount)
        recipient = wise_service.create_recipient(first_name, last_name, iban)
        transfer = wise_service.create_transfer(recipient["id"], quote["id"])
        transaction = TransactionModel(
            quote_id=quote["id"],
            transfer_id=transfer["id"],
            target_account_id=recipient["id"],
            amount=amount,
            order_id=order_id,
        )
        db.session.add(transaction)
        db.session.flush()

        return transaction, transfer

    @staticmethod
    def _calculate_total_price(product, quantity):
        """Calculates the total price based on product price and quantity."""
        total_price = 0.0

        if product:
            total_price = product.price * quantity
        return total_price

    @staticmethod
    def _get_order_or_404(order_id):
        """Helper function to get an order or raise NotFound."""

        order = db.session.execute(db.select(OrderModel)).filter_by(id=order_id).scalar()
        if not order:
            raise NotFound(f"Order with ID {order_id} not found.")
        return order

    @staticmethod
    def place_order(user, data):
        """Place an order by creating a new OrderModel instance."""

        data["customer_id"] = user.id

        product = db.session.execute(db.select(ProductModel).filter_by(id=data["product_id"])).scalar()
        if product is None:
            raise Exception("Product not found.")

        data["product_title"] = product.title

        order_quantity = data["quantity"]
        order_total_price = OrderManager._calculate_total_price(product, order_quantity)
        data["total_price"] = order_total_price

        order = OrderModel(**data)
        db.session.add(order)
        db.session.flush()

        try:
            # Issue the transaction and send money
            transaction, transfer = OrderManager.issue_transaction(
                amount=data["total_price"],
                first_name=user.first_name,
                last_name=user.last_name,
                iban=user.iban,
                order_id=order.id
            )

            if transfer["status"] != "incoming_payment_waiting":
                raise InternalServerError("Transaction failed. Order cannot be processed.")

            ProductManager.reduce_product_quantity(product.id, order_quantity)

            order.status = Status.approved
            db.session.add(order)
            db.session.flush()

        except Exception as e:
            order.status = Status.rejected
            db.session.add(order)
            db.session.flush()
            raise InternalServerError(f"Order processing failed: {str(e)}")

        return order
