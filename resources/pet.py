from flask import request
from flask_restful import Resource

from managers.auth import auth
from managers.pet import PetManager
from schemas.request.pet import PetRequestSchema
from schemas.response.pet import PetResponseSchema
from utils.decorators import validate_schema


class AddPet(Resource):
    """
    Endpoint for adding a new pet.

    This endpoint allows an authenticated user to add a new pet to their account by providing the pet details.
    The pet details are returned in the response.
    """
    @auth.login_required
    @validate_schema(PetRequestSchema)
    def post(self):
        """
        Adds a new pet for the authenticated user.

        Validates the incoming pet request, processes the pet data, and returns the added pet details.

        Args:
            request: The incoming HTTP request containing the pet data.

        Returns:
            dict: A dictionary containing the added pet details.
            int: HTTP status code 201 indicating that the pet was successfully added.
        """
        data = request.get_json()
        user = auth.current_user()
        pet = PetManager.add_pet(user, data)
        return PetResponseSchema().dump(pet), 201


class GetPets(Resource):
    """
    Endpoint for retrieving all pets of the authenticated user.

    This endpoint allows an authenticated user to fetch all their pets from the system.
    The list of pets will be returned in the response.
    """
    @auth.login_required
    def get(self):
        """
        Retrieves all pets for the authenticated user.

        This method fetches all pets associated with the currently authenticated user and returns them.

        Args:
            None

        Returns:
            list: A list of dictionaries containing pet details.
            int: HTTP status code 200 indicating the request was successful.
        """
        user = auth.current_user()
        pets = PetManager.get_pets(user)
        return PetResponseSchema().dump(pets, many=True), 200


class EditPet(Resource):
    """
    Endpoint for editing an existing pet's details.

    This endpoint allows an authenticated user to edit the details of a specific pet, identified by its `pet_id`.
    """
    @auth.login_required
    def put(self, pet_id):
        """
        Edits the details of an existing pet.

        Validates the incoming pet data and updates the pet's details in the system.

        Args:
            pet_id (int): The ID of the pet to be edited.
            request: The incoming HTTP request containing the updated pet data.

        Returns:
            int: HTTP status code 204 indicating the pet was successfully edited.
        """
        user = auth.current_user()
        data = request.get_json()
        PetManager.edit_pet(pet_id, user, data)
        return 204


class DeletePet(Resource):
    """
    Endpoint for deleting a pet.

    This endpoint allows an authenticated user to delete a pet from their account, identified by its `pet_id`.
    """
    @auth.login_required
    def delete(self, pet_id):
        """
        Deletes a specific pet from the authenticated user's account.

        The method removes the pet from the system based on the provided `pet_id`.

        Args:
            pet_id (int): The ID of the pet to be deleted.

        Returns:
            int: HTTP status code 204 indicating the pet was successfully deleted.
        """
        user = auth.current_user()
        PetManager.delete_pet(pet_id, user)
        return 204
