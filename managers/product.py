from werkzeug.exceptions import NotFound

from db import db
from models import ProductModel


class ProductManager:
    @staticmethod
    def add_product(data):
        """Adds a new product to the database."""

        product = ProductModel(**data)
        db.session.add(product)
        db.session.flush()
        return product

    @staticmethod
    def _get_product_or_404(product_id):
        """Helper function to fetch a product or raise NotFound."""

        product = db.session.execute(db.select(ProductModel).filter_by(id=product_id)).scalar()
        if not product:
            raise NotFound(f"Product with ID {product_id} not found.")
        return product

    @staticmethod
    def get_products():
        """Fetches all products."""

        return db.session.execute(db.select(ProductModel)).scalars().all()

    @staticmethod
    def get_product(product_id):
        """Fetches a single product by ID."""

        return ProductManager._get_product_or_404(product_id)

    @staticmethod
    def edit_product(product_id, data):
        """Edits an existing product."""

        product = ProductManager._get_product_or_404(product_id)

        for key, value in data.items():
            setattr(product, key, value)

        db.session.add(product)
        db.session.flush()

    @staticmethod
    def reduce_product_quantity(product_id, ordered_quantity):
        """Reduce quantity of an existing product."""

        product = ProductManager._get_product_or_404(product_id)

        if product.quantity - ordered_quantity >= 0:
            product.quantity -= ordered_quantity
        else:
            raise ValueError(f"Not enough items. Currently product {product.title} has quantity {product.quantity}.")

        db.session.add(product)
        db.session.flush()

    @staticmethod
    def delete_product(product_id):
        """Deletes a product by ID."""

        product = ProductManager._get_product_or_404(product_id)

        db.session.delete(product)
        db.session.flush()
