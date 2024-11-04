import enum


class RoleType(enum.Enum):
    user = "user"
    admin = "admin"


class Status(enum.Enum):
    pending = "Pending"
    approved = "Approved"
    rejected = "Rejected"


class PetType(enum.Enum):
    dog = "dog"
    cat = "cat"


class Gender(enum.Enum):
    female = "female"
    male = "male"
