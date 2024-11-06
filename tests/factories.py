from random import randint

import factory
from werkzeug.security import generate_password_hash

from db import db
from models import UserModel, RoleType, ProductModel


class BaseFactory(factory.Factory):
    @classmethod
    def create(cls, **kwargs):
        object = super().create(**kwargs)
        if hasattr(object, "password"):
            plain_pass = object.password
            object.password = generate_password_hash(plain_pass, method="pbkdf2:sha256")
        db.session.add(object)
        db.session.flush()
        return object


class UserFactory(BaseFactory):
    class Meta:
        model = UserModel

    id = factory.Sequence(lambda n: n)
    first_name = factory.Faker("first_name")
    last_name = factory.Faker("last_name")
    email = factory.Faker("email")
    phone = str(randint(100000, 200000))
    password = factory.Faker("password")
    role = RoleType.user
    iban = factory.Faker("iban")


class ProductFactory(BaseFactory):
    class Meta:
        model = ProductModel

    title = factory.Faker("word")  # Random title
    description = factory.Faker("text")  # Random description
    quantity = factory.Faker("random_int", min=1, max=100)  # Random quantity between 1 and 100
    price = factory.Faker("random_number", digits=2)  # Random price between 0 and 99
    photo_url = factory.Faker("image_url")  # Random photo URL (if applicable)
