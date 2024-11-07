from datetime import datetime

import pytest

from db import db
from models import AppointmentModel, UserModel
from tests.base import app, database, client
from tests.factories import UserFactory, PetFactory


def login_data():
    """
    Helper function to generate login data for the first user in the database.
    """
    user = db.session.query(UserModel).first()

    data = {
        "email": user.email,
        "password": "testpassword"
    }

    return user, data


@pytest.mark.parametrize('endpoint, method, status_code', [
    ('/appointments/book_appointment', 'post', 201),  # Book appointment
])
def test_appointments(client, database, endpoint, method, status_code):
    """
    Test booking an appointment.
    """
    # Create a user and login
    user = UserFactory(password="testpassword")
    user_data = login_data()

    # Authenticate the user by obtaining the token
    login_response = client.post("/login", json=user_data[1])
    token = login_response.json["token"]
    headers = {"Authorization": f"Bearer {token}"}

    # Test POST (Book appointment)
    if method == 'post':
        # Create a pet for the user
        pet = PetFactory(owner_id=user.id, owner_email=user.email)

        # Define the appointment data
        appointment_data = {
            "pet_name": pet.name,
            "appointment_datetime": "2024-11-10 10:00:00",  # The date and time for the appointment
            "appointment_reason": "Routine checkup"
        }

        # Book the appointment
        response = client.post(endpoint, json=appointment_data, headers=headers)

        # Assert the status code
        assert response.status_code == status_code

        appointment = AppointmentModel.query.get(response.json["id"])
        assert appointment is not None
        assert appointment.pet_name == pet.name
        assert appointment.appointment_datetime == datetime.fromisoformat("2024-11-10T10:00:00")
        assert appointment.appointment_reason == "Routine checkup"


@pytest.mark.parametrize('endpoint, method, status_code', [
    ('/appointments/book_appointment', 'post', 409),  # Appointment conflict
])
def test_appointment_time_conflict(client, database, endpoint, method, status_code):
    """
    Test booking an appointment when the time is already taken.
    """
    # Create a user and login
    user = UserFactory(password="testpassword")
    user_data = login_data()

    # Authenticate the user by obtaining the token
    login_response = client.post("/login", json=user_data[1])
    token = login_response.json["token"]
    headers = {"Authorization": f"Bearer {token}"}

    # Create a pet for the user
    pet = PetFactory(owner_id=user.id, owner_email=user.email)

    # Define the first appointment data
    appointment_data_1 = {
        "pet_name": pet.name,
        "appointment_datetime": "2024-11-10 10:00:00",  # First appointment time
        "appointment_reason": "Routine checkup"
    }

    # Book the first appointment
    client.post(endpoint, json=appointment_data_1, headers=headers)

    # Define the second appointment data (same time)
    appointment_data_2 = {
        "pet_name": pet.name,
        "appointment_datetime": "2024-11-10 10:00:00",  # Same time as the first one
        "appointment_reason": "Vaccination"
    }

    # Try to book the second appointment (should conflict)
    response = client.post(endpoint, json=appointment_data_2, headers=headers)

    # Assert the status code
    assert response.status_code == status_code

    # Assert the error message
    assert response.json["message"] == "409 Conflict: Appointment time '2024-11-10 10:00:00' is already taken."


@pytest.mark.parametrize('endpoint, method, status_code', [
    ('/appointments/book_appointment', 'post', 404),
])
def test_pet_not_found(client, database, endpoint, method, status_code):
    """
    Test booking an appointment when the pet is not found.
    """
    user = UserFactory(password="testpassword")
    user_data = login_data()

    login_response = client.post("/login", json=user_data[1])
    token = login_response.json["token"]
    headers = {"Authorization": f"Bearer {token}"}

    appointment_data = {
        "pet_name": "NonExistentPet",  # This pet does not exist
        "appointment_datetime": "2024-11-10 10:00:00",
        "appointment_reason": "Routine checkup"
    }

    response = client.post(endpoint, json=appointment_data, headers=headers)

    assert response.status_code == status_code

    assert response.json[
               "message"] == f"Pet with name 'NonExistentPet' not found for user {user.first_name + ' ' + user.last_name}"
