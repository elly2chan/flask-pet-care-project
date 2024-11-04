from werkzeug.exceptions import NotFound

from db import db
from models import ProductModel, OrderModel
from models.enums import Status


class OrderManager:
    @staticmethod
    def place_order(user, data):
        data["customer_id"] = user.id

        product = db.session.execute(db.select(ProductModel).filter_by(id=data['product_id'])).scalar()
        if product is None:
            raise Exception("Product not found.")

        data["product_title"] = product.title

        order = OrderModel(**data)
        db.session.add(order)
        db.session.flush()

    @staticmethod
    def approve(order_id):
        #TODO decrease quantity of the product
        order = db.session.execute(db.select(OrderModel).filter_by(id=order_id)).scalar()
        if not order:
            raise NotFound
        order.status = Status.approved
        db.session.add(order)
        db.session.flush()

    @staticmethod
    def reject(order_id):
        order = db.session.execute(db.select(OrderModel).filter_by(id=order_id)).scalar()
        if not order:
            raise NotFound
        order.status = Status.rejected
        db.session.add(order)
        db.session.flush()
