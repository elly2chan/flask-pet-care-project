from flask import request
from flask_restful import Resource
from werkzeug.exceptions import NotFound, BadRequest

from managers.auth import auth
from managers.pet import PetManager
from schemas.request.pet import PetRequestSchema
from schemas.response.pet import PetResponseSchema
from utils.decorators import validate_schema


class AddPet(Resource):
    @auth.login_required
    @validate_schema(PetRequestSchema)
    def post(self):
        """
        Add a new pet for the authenticated user.

        :return: dict with added pet details, status code 201
        """
        data = request.get_json()
        user = auth.current_user()
        pet = PetManager.add_pet(user, data)
        return PetResponseSchema().dump(pet), 201


class GetPets(Resource):
    @auth.login_required
    def get(self):
        """
        Retrieve all pets for the authenticated user.

        :return: list of pet details, status code 200
        """
        user = auth.current_user()
        pets = PetManager.get_pets(user)
        return PetResponseSchema().dump(pets, many=True), 200


class EditPet(Resource):
    @auth.login_required
    def put(self, pet_id):
        """
        Edit an existing pet's details.

        :param pet_id: The ID of the pet to edit
        :return: status code 201 for successful edit
        """
        data = request.get_json()
        user = auth.current_user()

        try:
            PetManager.edit_pet(pet_id, user, data)
            return {"message": f"Pet is edited successfully."}, 200
        except ValueError as e:
            return ({"message": str(e)}), 400


class DeletePet(Resource):
    @auth.login_required
    def delete(self, pet_id):
        """
        Delete a specific pet from the authenticated user's account.

        :param pet_id: The ID of the pet to delete
        :return: status code 204 for successful deletion
        """
        user = auth.current_user()
        PetManager.delete_pet(pet_id, user)
        return {"message": f"Pet is deleted successfully."}, 200


class IdentifyDogBreed(Resource):
    @auth.login_required
    def post(self, pet_id):
        """
        Try to identify a dog's breed by a provided URL and pet_id.
        """
        user = auth.current_user()

        data = request.get_json()

        if 'url' not in data:
            raise BadRequest("The 'url' field is required.")

        url = data['url']

        try:
            pet_name, breed, probability = PetManager.identify_dog_breed(user, (pet_id, url))
        except NotFound:
            raise NotFound(f"Pet with id {pet_id} not found.")
        except BadRequest as e:
            raise BadRequest(str(e))

        return {"message": f"Your dog {pet_name}'s breed is {breed}. The probability of that is {probability}."}, 200
