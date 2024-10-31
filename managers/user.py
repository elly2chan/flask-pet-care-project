from werkzeug.exceptions import BadRequest, NotFound, Unauthorized
from werkzeug.security import generate_password_hash, check_password_hash

from db import db
from managers.auth import AuthManager
from models.enums import RoleType
from models.order import OrderModel
from models.pet import PetModel
from models.user import UserModel


class UserManager:
    @staticmethod
    def register(user_data):
        user_data["password"] = generate_password_hash(
            user_data["password"], method="pbkdf2:sha256"
        )
        user_data["role"] = RoleType.user.name
        user = UserModel(**user_data)
        try:
            db.session.add(user)
            db.session.flush()
            return AuthManager.encode_token(user)
        except Exception as ex:
            raise BadRequest(str(ex))

    @staticmethod
    def login(data):
        user = db.session.execute(db.select(UserModel).filter_by(email=data["email"])).scalar()
        if not user or not check_password_hash(user.password, data["password"]):
            raise BadRequest("Invalid username or password.")
        return AuthManager.encode_token(user)

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

    @staticmethod
    def place_order(user, product, data):
        data["customer_id"] = user.id
        data["product_id"] = product.id
        data["product_title"] = product.title
        data["product_description"] = product.description
        order = OrderModel(**data)
        db.session.add(order)
        db.session.flush()
