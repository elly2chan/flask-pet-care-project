from random import randint
from uuid import uuid4

import factory
from werkzeug.security import generate_password_hash

from db import db
from models import UserModel, RoleType, ProductModel, PetModel, PetType, Gender


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


class PetFactory(BaseFactory):
    class Meta:
        model = PetModel

    id = factory.Sequence(lambda n: n)
    name = factory.Faker("first_name")  # Random pet name, can adjust as needed
    gender = factory.Faker("random_element", elements=[Gender.male, Gender.female])
    date_of_birth = factory.Faker("date_of_birth", minimum_age=1,
                                  maximum_age=20)  # Pets are usually not younger than 1 and not older than 20 years
    breed = factory.Faker("word")  # Random breed, adjust to your needs
    owner_id = factory.SubFactory(UserFactory)  # A pet belongs to a user
    pet_type = factory.Faker("random_element", elements=[PetType.dog, PetType.cat])  # Random pet type (Dog or Cat)
    is_stray = factory.Faker("boolean", chance_of_getting_true=20)  # 20% chance the pet is stray
    european_passport = factory.Faker("boolean", chance_of_getting_true=50)  # 50% chance the pet has a passport
    microchip = factory.Faker("boolean", chance_of_getting_true=50)  # 50% chance the pet has a microchip
    microchip_id = factory.LazyAttribute(
        lambda _: str(uuid4())[:20])  # Random microchip ID, can be None if not microchipped
    added_on = factory.Faker("date_this_decade")  # Random date from the last 10 years for when the pet was added
