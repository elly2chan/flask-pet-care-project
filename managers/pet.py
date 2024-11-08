from datetime import datetime

from flask import jsonify
from werkzeug.exceptions import NotFound, Unauthorized, BadRequest

from db import db
from models.enums import RoleType, Gender, PetType
from models.pet import PetModel
from services.nyckel import NyckelService

nyckel_service = NyckelService()


class PetManager:
    @staticmethod
    def add_pet(user, data):
        """Adds a new pet to the database."""
        data["owner_id"] = user.id
        data["owner_email"] = user.email

        if not "date_of_birth" in data:
            raise BadRequest("You must provide a date of birth.")

        if isinstance(data['date_of_birth'], str):
            try:
                data['date_of_birth'] = datetime.strptime(data['date_of_birth'], "%Y-%m-%d").date()
            except ValueError as e:
                raise ValueError(f"Error parsing date_of_birth: {e}")
        elif not isinstance(data['date_of_birth'], datetime):
            raise ValueError("date_of_birth must be a string or a datetime object.")

        try:
            if 'gender' in data:
                data['gender'] = Gender[data['gender'].lower()]
            if 'pet_type' in data:
                data['pet_type'] = PetType[data['pet_type'].lower()]
        except KeyError as e:
            return jsonify({"error": f"Invalid value for {str(e)}."}), 400

        pet = PetModel(**data)
        db.session.add(pet)
        db.session.flush()
        return pet

    @staticmethod
    def get_pets(user):
        """Fetches pets for the given user."""
        query = db.select(PetModel)

        if user.role != RoleType.admin.name:
            query = query.filter_by(owner_id=user.id)

        pets = db.session.execute(query).scalars()
        if not pets:
            raise NotFound("No pets found for the given user.")

        return pets

    @staticmethod
    def edit_pet(pet_id, user, data):
        """Edits a pet."""
        pet = db.session.execute(db.select(PetModel).filter_by(id=pet_id)).scalar()
        if not pet:
            raise NotFound(f"Pet with ID {pet_id} not found.")

        if user.role == RoleType.admin.name or pet.owner_id == user.id:
            valid_fields = {col.name for col in PetModel.__table__.columns}

            for key, value in data.items():
                if key not in valid_fields:
                    raise ValueError(f"Invalid field: {key} is not a valid attribute.")

                setattr(pet, key, value)
        else:
            raise Unauthorized("You do not have permission to edit this pet.")

        db.session.add(pet)
        db.session.flush()

    @staticmethod
    def delete_pet(pet_id, user):
        """Deletes a pet from the database."""
        pet = db.session.execute(db.select(PetModel).filter_by(id=pet_id)).scalar()
        if not pet:
            raise NotFound

        if user.role == RoleType.admin.name or pet.owner_id == user.id:
            db.session.delete(pet)
        else:
            raise Unauthorized("You do not have permission to delete this pet.")

        db.session.flush()

    @staticmethod
    def identify_dog_breed(data):
        """Identify dog breed by provided URL."""

        pet_id, url = data

        pet = db.session.execute(db.select(PetModel).filter_by(id=pet_id)).scalar()
        if not pet:
            raise NotFound("Pet not found.")

        if pet.pet_type != PetType.dog:
            raise BadRequest("Breed identifier is supported only for dogs.")

        result = nyckel_service.identify_dog_breed(url)

        pet_name = pet.name
        breed = result['labelName']
        probability = result['confidence']

        return pet_name, breed, probability
