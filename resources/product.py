from flask import request
from flask_restful import Resource

from managers.auth import auth
from managers.product import ProductManager
from models import RoleType
from schemas.request.product import ProductRequestSchema
from schemas.response.product import ProductResponseSchema
from utils.decorators import permission_required, validate_schema


class AddProduct(Resource):
    """
    Endpoint for adding a new product.

    This endpoint allows an authenticated user with admin permissions to add a new product to the system.
    The product details are returned in the response.
    """
    @auth.login_required
    @permission_required(RoleType.admin)
    @validate_schema(ProductRequestSchema)
    def post(self):
        """
        Adds a new product to the system.

        Validates the incoming product request, processes the product data, and returns the added product details.

        Args:
            request: The incoming HTTP request containing the product data.

        Returns:
            dict: A dictionary containing the added product details.
            int: HTTP status code 201 indicating that the product was successfully added.
        """
        data = request.get_json()
        product = ProductManager.add_product(data)
        return ProductResponseSchema().dump(product), 201


class GetProducts(Resource):
    """
    Endpoint for retrieving all products.

    This endpoint allows anyone (no authentication required) to fetch a list of all products in the system.
    """
    def get(self):
        """
        Retrieves a list of all products.

        This method fetches all products and returns them in the response.

        Args:
            None

        Returns:
            list: A list of dictionaries containing product details.
            int: HTTP status code 200 indicating the request was successful.
        """
        products = ProductManager.get_products()
        return ProductResponseSchema().dump(products, many=True), 200


class GetProduct(Resource):
    """
    Endpoint for retrieving a specific product by its ID.

    This endpoint allows an authenticated user to fetch a specific product by providing its ID.
    """
    @auth.login_required
    def get(self, product_id):
        """
        Retrieves the details of a specific product.

        This method fetches a single product by its ID and returns its details.

        Args:
            product_id (int): The ID of the product to retrieve.

        Returns:
            dict: A dictionary containing the product details.
            int: HTTP status code 201 indicating the request was successful.
        """
        product = ProductManager.get_product(product_id)
        return ProductResponseSchema().dump(product), 201


class EditProduct(Resource):
    """
    Endpoint for editing an existing product.

    This endpoint allows an authenticated user with admin permissions to edit the details of a specific product.
    """
    @auth.login_required
    @permission_required(RoleType.admin)
    def put(self, product_id):
        """
        Edits the details of an existing product.

        Validates the incoming product data and updates the product's details in the system.

        Args:
            product_id (int): The ID of the product to edit.
            request: The incoming HTTP request containing the updated product data.

        Returns:
            int: HTTP status code 204 indicating the product was successfully updated.
        """
        data = request.get_json()
        ProductManager.edit_product(product_id, data)
        return 204


class DeleteProduct(Resource):
    """
    Endpoint for deleting a product.

    This endpoint allows an authenticated user with admin permissions to delete a specific product from the system.
    """
    @auth.login_required
    @permission_required(RoleType.admin)
    def delete(self, product_id):
        """
        Deletes a specific product.

        The method removes the product from the system based on the provided product ID.

        Args:
            product_id (int): The ID of the product to be deleted.

        Returns:
            int: HTTP status code 204 indicating the product was successfully deleted.
        """
        ProductManager.delete_product(product_id)
        return 204
