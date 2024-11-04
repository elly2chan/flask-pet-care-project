from flask import request
from flask_restful import Resource

from managers.auth import auth
from managers.order import OrderManager
from models import RoleType
from schemas.request.order import OrderRequestSchema
from schemas.response.order import OrderResponseSchema
from utils.decorators import validate_schema, permission_required


class PlaceOrder(Resource):
    @auth.login_required
    @validate_schema(OrderRequestSchema)
    def post(self):
        user = auth.current_user()
        data = request.get_json()
        order = OrderManager.place_order(user, data)
        return OrderResponseSchema().dump(order), 201


class ApproveOrder(Resource):
    @auth.login_required
    @permission_required(RoleType.admin)
    def put(self, order_id):
        OrderManager.approve(order_id)
        return 204


class RejectOrder(Resource):
    @auth.login_required
    @permission_required(RoleType.admin)
    def put(self, order_id):
        OrderManager.reject(order_id)
        return 204
