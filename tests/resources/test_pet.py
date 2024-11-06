import pytest

from db import db
from models import UserModel, PetModel, Gender, PetType
from tests.factories import UserFactory, PetFactory

from tests.base import app, database, client


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
    ('/pets/add_pet', 'post', 201),  # Add Pet
    ('/pets', 'get', 200),  # Get Pets
    ('/pets/edit_pet/1', 'put', 204),  # Edit Pet
    ('/pets/delete_pet/1', 'delete', 204)  # Delete Pet
])
def test_pets(client, database, endpoint, method, status_code):
    """
    Test adding, getting, editing, and deleting pets.
    """
    # Create a user and login
    user = UserFactory(password="testpassword")
    user_data = login_data()

    # Authenticate the user by obtaining the token
    login_response = client.post("/login", json=user_data[1])
    token = login_response.json["token"]
    headers = {"Authorization": f"Bearer {token}"}

    # Test POST (Add Pet)
    if method == 'post':
        pet_data = {
            "name": "Buddy",
            "pet_type": PetType.dog.name,  # Pass the enum itself, not the name or value
            "breed": "Labrador",
            "gender": Gender.male.name,  # Pass the enum itself, not the name or value
            "date_of_birth": "2024-07-28"
        }
        response = client.post(endpoint, json=pet_data, headers=headers)
        print(response)

    # Test GET (Get Pets)
    elif method == 'get':
        PetFactory(owner_id=user.id, owner_email=user.email)  # Create a pet for the user
        response = client.get(endpoint, headers=headers)
        assert response.status_code == status_code
        assert len(response.json) > 0

    # Test PUT (Edit Pet)
    elif method == 'put':
        pet = PetFactory(owner_id=user.id, owner_email=user.email)  # Create a pet to edit
        pet_data = {
            "name": "Max",
            "species": "Dog",
            "breed": "Bulldog",
            "age": 4
        }
        response = client.put(f"/pets/edit_pet/{pet.id}", json=pet_data, headers=headers)
        assert response.json == status_code
        updated_pet = PetModel.query.get(pet.id)
        assert updated_pet.name == "Max"

    # Test DELETE (Delete Pet)
    elif method == 'delete':
        pet = PetFactory(owner_id=user.id, owner_email=user.email)  # Create a pet to delete
        response = client.delete(f"/pets/delete_pet/{pet.id}", headers=headers)
        assert response.json == status_code
        deleted_pet = PetModel.query.get(pet.id)
        assert deleted_pet is None
