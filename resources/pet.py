from flask import request
from flask_restful import Resource

from managers.auth import auth
from managers.pet import PetManager
from schemas.request.pet import PetRequestSchema
from schemas.response.pet import PetResponseSchema
from utils.decorators import validate_schema


class AddPet(Resource):
    @auth.login_required
    @validate_schema(PetRequestSchema)
    def post(self):
        data = request.get_json()
        user = auth.current_user()
        pet = PetManager.add_pet(user, data)
        return PetResponseSchema().dump(pet), 201


class GetPets(Resource):
    @auth.login_required
    @validate_schema(PetRequestSchema)
    def get(self):
        user = auth.current_user()
        pets = PetManager.get_pets(user)
        return PetResponseSchema().dump(pets, many=True), 201


class EditPet(Resource):
    @auth.login_required
    def patch(self, pet_id):
        user = auth.current_user()
        data = request.get_json()
        PetManager.edit_pet(pet_id, user, data)
        return 204


class DeletePet(Resource):
    @auth.login_required
    def delete(self, pet_id):
        user = auth.current_user()
        PetManager.delete_pet(pet_id, user)
        return 204
