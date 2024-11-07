import enum


class RoleType(enum.Enum):
    """Enum for user roles."""
    user = "user"
    admin = "admin"


class Status(enum.Enum):
    """Enum for order statuses."""
    pending = "Pending"
    approved = "Approved"
    rejected = "Rejected"


class PetType(enum.Enum):
    """Enum for pet types."""
    dog = "dog"
    cat = "cat"


class Gender(enum.Enum):
    """Enum for gender types."""
    female = "female"
    male = "male"
