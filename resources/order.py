from flask import request
from flask_restful import Resource

from managers.auth import auth
from managers.order import OrderManager
from models import RoleType
from schemas.request.order import OrderRequestSchema
from schemas.response.order import OrderResponseSchema
from utils.decorators import validate_schema, permission_required


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


class ApproveOrder(Resource):
    """
    Endpoint for approving an order.

    This endpoint allows an admin user to approve a pending order. Only admin users have permission to approve orders.
    """

    @auth.login_required
    @permission_required(RoleType.admin)
    def put(self, order_id):
        """
        Approves the order with the given ID.

        Validates the user’s role, checks if they have permission to approve orders, and updates the order's status
        to 'approved'.

        Args:
            order_id (int): The ID of the order to approve.

        Returns:
            int: HTTP status code 204 indicating that the order was successfully approved.
        """
        OrderManager.approve(order_id)
        return 204


class RejectOrder(Resource):
    """
    Endpoint for rejecting an order.

    This endpoint allows an admin user to reject a pending order. Only admin users have permission to reject orders.
    """

    @auth.login_required
    @permission_required(RoleType.admin)
    def put(self, order_id):
        """
        Rejects the order with the given ID.

        Validates the user’s role, checks if they have permission to reject orders, and updates the order's status
        to 'rejected'.

        Args:
            order_id (int): The ID of the order to reject.

        Returns:
            int: HTTP status code 204 indicating that the order was successfully rejected.
        """
        OrderManager.reject(order_id)
        return 204
