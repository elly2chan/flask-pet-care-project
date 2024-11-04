from werkzeug.exceptions import NotFound, Unauthorized

from db import db
from models.enums import RoleType
from models.pet import PetModel


class PetManager:
    @staticmethod
    def add_pet(user, data):
        data["owner_id"] = user.id
        data["owner_email"] = user.email
        pet = PetModel(**data)
        db.session.add(pet)
        db.session.flush()

    @staticmethod
    def get_pets(user):
        query = db.select(PetModel)
        if user.role.user:
            query = query.filter_by(owner_id=user.id)
        pets = db.session.execute(query).scalars()
        if not pets:
            raise Exception("No pets found.")
        return pets

    @staticmethod
    def edit_pet(pet_id, user, data):
        pet = db.session.execute(db.select(PetModel).filter_by(id=pet_id)).scalar()
        if not pet:
            raise NotFound

        if user.role == RoleType.admin.name:
            for key, value in data.items():
                setattr(pet, key, value)
        else:
            if pet.owner_id != user.id:
                raise Unauthorized

            for key, value in data.items():
                setattr(pet, key, value)

        db.session.add(pet)
        db.session.flush()

    @staticmethod
    def delete_pet(pet_id, user):
        pet = db.session.execute(db.select(PetModel).filter_by(id=pet_id)).scalar()
        if not pet:
            raise NotFound

        if user.role == RoleType.admin.name:
            db.session.delete(pet)
        else:
            if pet.owner_id != user.id:
                raise Unauthorized
            db.session.delete(pet)

        db.session.flush()
