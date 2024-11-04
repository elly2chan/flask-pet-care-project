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
        data = request.get_json()
        product = ProductManager.add_product(data)
        return ProductResponseSchema().dump(product), 201


class GetProducts(Resource):
    @validate_schema(ProductRequestSchema)
    def get(self):
        products = ProductManager.get_products()
        return ProductResponseSchema().dump(products, many=True), 201


class GetProduct(Resource):
    @auth.login_required
    def get(self, product_id):
        product = ProductManager.get_product(product_id)
        return ProductResponseSchema().dump(product), 201


class EditProduct(Resource):
    @auth.login_required
    @permission_required(RoleType.admin)
    def patch(self, product_id):
        data = request.get_json()
        ProductManager.edit_product(product_id, data)
        return 204


class DeleteProduct(Resource):
    @auth.login_required
    @permission_required(RoleType.admin)
    def delete(self, product_id):
        ProductManager.delete_product(product_id)
        return 204
