from flask import request
from flask_restful import Resource

from managers.auth import auth
from managers.order import OrderManager
from schemas.request.order import OrderRequestSchema
from schemas.response.order import OrderResponseSchema
from utils.decorators import validate_schema


class PlaceOrder(Resource):
    @auth.login_required
    @validate_schema(OrderRequestSchema)
    def post(self):
        """
        Place a new order for the authenticated user.

        :return: dict with order details, status code 201
        """
        user = auth.current_user()
        data = request.get_json()
        order = OrderManager.place_order(user, data)
        return OrderResponseSchema().dump(order), 201
