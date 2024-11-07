from flask import request
from flask_restful import Resource

from managers.appointment import AppointmentManager
from managers.auth import auth
from schemas.request.appointment import AppointmentRequestSchema
from schemas.response.appointment import AppointmentResponseSchema
from utils.decorators import validate_schema


class BookAppointment(Resource):
    @auth.login_required
    @validate_schema(AppointmentRequestSchema)
    def post(self):
        """
        Book an appointment for the authenticated user's pet.

        :return: dict with order details, status code 201
        """
        user = auth.current_user()
        data = request.get_json()
        appointment = AppointmentManager.book_appointment(user, data)
        return AppointmentResponseSchema().dump(appointment), 201
