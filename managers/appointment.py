from sqlalchemy.exc import IntegrityError
from werkzeug.exceptions import NotFound, Conflict

from db import db
from models import AppointmentModel, PetModel


class AppointmentManager:
    @staticmethod
    def book_appointment(user, data):
        """Adds a new appointment to the database."""

        try:
            data["owner_id"] = user.id
            data["owner_name"] = user.first_name + " " + user.last_name
            data["owner_phone"] = user.phone

            pet = db.session.execute(db.select(PetModel).filter_by(owner_id=user.id, name=data["pet_name"])).scalar()
            if not pet:
                raise NotFound(
                    f"Pet with name '{data['pet_name']}' not found for user {user.first_name} {user.last_name}")

            data["pet_id"] = pet.id

            existing_appointment = db.session.execute(
                db.select(AppointmentModel).filter_by(appointment_datetime=data["appointment_datetime"])
            ).scalar()

            if existing_appointment:
                raise Conflict(f"Appointment time '{data['appointment_datetime']}' is already taken.")

            appointment = AppointmentModel(**data)
            db.session.add(appointment)
            db.session.flush()
            return appointment
        except IntegrityError:
            raise ValueError("Error saving the appointment. Please try again.")
