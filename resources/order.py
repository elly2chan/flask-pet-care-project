from flask import request
from flask_restful import Resource

from managers.auth import auth
from managers.order import OrderManager
from schemas.request.order import OrderRequestSchema
from schemas.response.order import OrderResponseSchema
from utils.decorators import validate_schema


class PlaceOrder(Resource):
    """
    Endpoint for placing a new order.

    This endpoint allows an authenticated user to place a new order by providing the necessary order details.
    The order will be processed and stored in the system. The order details are returned in the response.
    """

    @auth.login_required
    @validate_schema(OrderRequestSchema)
    def post(self):
        """
        Places a new order for the authenticated user.

        Validates the incoming order request, processes the order, and returns the order details.

        Args:
            request: The incoming HTTP request containing the order data.

        Returns:
            dict: A dictionary containing the order details.
            int: HTTP status code 201 indicating the order was successfully placed.
        """
        user = auth.current_user()
        data = request.get_json()
        order = OrderManager.place_order(user, data)
        return OrderResponseSchema().dump(order), 201
