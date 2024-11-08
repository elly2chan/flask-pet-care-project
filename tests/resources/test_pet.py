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
    ('/pets/add_pet', 'post', 201),  # Add pet
    ('/pets', 'get', 200),  # Get pets
    ('/pets/edit_pet/1', 'put', 200),  # Edit pet
    ('/pets/delete_pet/1', 'delete', 200)  # Delete pet
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

    # Test POST (Add pet)
    if method == 'post':
        pet_data = {
            "name": "Buddy",
            "pet_type": PetType.dog.name,
            "breed": "Labrador",
            "gender": Gender.male.name,
            "date_of_birth": "2024-07-28"
        }
        response = client.post(endpoint, json=pet_data, headers=headers)
        print(response)

    # Test GET (Get pets)
    elif method == 'get':
        PetFactory(owner_id=user.id, owner_email=user.email)
        response = client.get(endpoint, headers=headers)
        assert response.status_code == status_code
        assert len(response.json) > 0

    # Test PUT (Edit pet)
    elif method == 'put':
        pet = PetFactory(owner_id=user.id, owner_email=user.email)
        pet_data = {
            "breed": "Bulldog",
        }
        response = client.put(f"/pets/edit_pet/{pet.id}", json=pet_data, headers=headers)
        assert response.status_code == status_code
        assert response.json == {'message': 'Pet is edited successfully.'}
        updated_pet = PetModel.query.get(pet.id)
        assert updated_pet.breed == "Bulldog"

    # Test DELETE (Delete pet)
    elif method == 'delete':
        pet = PetFactory(owner_id=user.id, owner_email=user.email)
        response = client.delete(f"/pets/delete_pet/{pet.id}", headers=headers)
        assert response.status_code == status_code
        assert response.json == {'message': 'Pet is deleted successfully.'}
        deleted_pet = PetModel.query.get(pet.id)
        assert deleted_pet is None
