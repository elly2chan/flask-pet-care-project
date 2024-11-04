from werkzeug.exceptions import NotFound

from db import db
from models import ProductModel


class ProductManager:
    @staticmethod
    def add_product(data):
        product = ProductModel(**data)
        db.session.add(product)
        db.session.flush()
        return product

    @staticmethod
    def get_products():
        return db.session.execute(db.select(ProductModel)).scalars().all()

    @staticmethod
    def get_product(product_id):
        product = db.session.execute(db.select(ProductModel).filter_by(id=product_id)).scalar()
        if not product:
            raise NotFound
        return product

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
