from flask import request
from flask_restful import Resource

from managers.auth import auth
from managers.product import ProductManager
from models import RoleType
from schemas.request.product import ProductRequestSchema
from schemas.response.product import ProductResponseSchema
from utils.decorators import permission_required, validate_schema


class AddProduct(Resource):
    @auth.login_required
    @permission_required(RoleType.admin)
    @validate_schema(ProductRequestSchema)
    def post(self):
        """
        Adds a new product to the system.

        Validates the incoming product request, processes the product data, and returns the added product details.

        :return: dict with product details, status code 201
        """
        data = request.get_json()
        product = ProductManager.add_product(data)
        return ProductResponseSchema().dump(product), 201


class GetProducts(Resource):
    def get(self):
        """
        Retrieves a list of all products.

        This method fetches all products and returns them in the response.

        :return: list of product details, status code 200
        """
        products = ProductManager.get_products()
        return ProductResponseSchema().dump(products, many=True), 200


class GetProduct(Resource):
    @auth.login_required
    def get(self, product_id):
        """
        Retrieves the details of a specific product.

        This method fetches a single product by its ID and returns its details.

        :param product_id: The ID of the product to retrieve.
        :return: dict with product details, status code 200
        """
        product = ProductManager.get_product(product_id)
        return ProductResponseSchema().dump(product), 200


class EditProduct(Resource):
    @auth.login_required
    @permission_required(RoleType.admin)
    def put(self, product_id):
        """
        Edits the details of an existing product.

        Validates the incoming product data and updates the product's details in the system.

        :param product_id: The ID of the product to edit.
        :return: HTTP status code 204 indicating the product was successfully updated.
        """
        data = request.get_json()
        ProductManager.edit_product(product_id, data)
        return 204


class DeleteProduct(Resource):
    @auth.login_required
    @permission_required(RoleType.admin)
    def delete(self, product_id):
        """
        Deletes a specific product.

        The method removes the product from the system based on the provided product ID.

        :param product_id: The ID of the product to be deleted.
        :return: HTTP status code 204 indicating the product was successfully deleted.
        """
        ProductManager.delete_product(product_id)
        return 204
