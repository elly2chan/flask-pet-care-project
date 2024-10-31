from werkzeug.exceptions import NotFound

from db import db
from models.enums import State
from models.order import OrderModel
from models.product import ProductModel


class AdminManager:
    @staticmethod
    def add_product(data):
        product = ProductModel(**data)
        db.session.add(product)
        db.session.flush()

    @staticmethod
    def get_products(product_id=None):
        if product_id is not None:
            product = db.session.execute(db.select(ProductModel).filter_by(id=product_id)).scalar()
            if not product:
                raise NotFound
            return product
        products = ProductModel.query.all()
        return products

    @staticmethod
    def edit_product(product_id, data):
        product = db.session.execute(db.select(ProductModel).filter_by(id=product_id)).scalar()
        if not product:
            raise NotFound

        for key, value in data.items():
            setattr(product, key, value)

        db.session.add(product)
        db.session.flush()

    @staticmethod
    def delete_product(product_id):
        product = db.session.execute(db.select(ProductModel).filter_by(id=product_id)).scalar()
        if not product:
            raise NotFound

        db.session.delete(product)
        db.session.flush()

    @staticmethod
    def approve_order(order_id):
        order = db.session.execute(db.select(OrderModel).filter_by(id=order_id)).scalar()
        if not order:
            raise NotFound
        order.status = State.approved
        db.session.add(order)
        db.session.flush()

    @staticmethod
    def deny_order(order_id):
        order = db.session.execute(db.select(OrderModel).filter_by(id=order_id)).scalar()
        if not order:
            raise NotFound
        order.status = State.rejected
        db.session.add(order)
        db.session.flush()
