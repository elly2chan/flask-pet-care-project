from werkzeug.exceptions import NotFound

from db import db
from models import ProductModel, OrderModel
from models.enums import Status


class OrderManager:
    @staticmethod
    def place_order(user, data):
        """Place an order by creating a new OrderModel instance."""

        data["customer_id"] = user.id

        product = db.session.execute(db.select(ProductModel).filter_by(id=data['product_id'])).scalar()
        if product is None:
            raise Exception("Product not found.")

        data["product_title"] = product.title

        order = OrderModel(**data)
        db.session.add(order)
        db.session.flush()

    @staticmethod
    def _get_order_or_404(order_id):
        """Helper function to get an order or raise NotFound."""

        order = db.session.exexcute(db.select(OrderModel)).filter_by(id=order_id).scalar()
        if not order:
            raise NotFound(f"Order with ID {order_id} not found.")
        return order

    @staticmethod
    def approve(order_id):
        """Approve an order and adjust the product quantity."""

        # TODO decrease quantity of the product
        order = OrderManager._get_order_or_404(order_id)
        order.status = Status.approved
        db.session.add(order)
        db.session.flush()

    @staticmethod
    def reject(order_id):
        """Reject an order."""

        order = OrderManager._get_order_or_404(order_id)
        order.status = Status.rejected
        db.session.add(order)
        db.session.flush()
