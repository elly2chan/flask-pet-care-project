"""
Defines the API routes and maps them to their respective resources.

Routes:
- Public: RegisterUser, LoginUser, GetDocumentationPage, GetProducts, GetProduct
- Authenticated: AddPet, GetPets, EditPet, DeletePet, PlaceOrder, BookAppointment
- Admin: AddProduct, EditProduct, DeleteProduct

Each route corresponds to a specific resource handling the logic for that endpoint.
"""
from resources.appointment import BookAppointment
from resources.auth import RegisterUser, LoginUser, ChangePassword
from resources.order import PlaceOrder
from resources.pet import AddPet, GetPets, EditPet, DeletePet, IdentifyDogBreed
from resources.product import AddProduct, GetProducts, EditProduct, DeleteProduct, GetProduct
from resources.public import GetDocumentationPage

routes = (
    (RegisterUser, "/register"),  # everyone can register
    (LoginUser, "/login"),  # everyone can log in
    (ChangePassword, "/users/change_password"),

    (GetDocumentationPage, "/"),  # everyone can see the documentation page (public)

    (AddPet, "/pets/add_pet"),  # only authenticated users can add pets
    (GetPets, "/pets"),  # only authenticated users can see their pets, admins can see all pets
    (EditPet, "/pets/edit_pet/<int:pet_id>"),  # only authenticated users can edit pets, admins can edit all
    (DeletePet, "/pets/delete_pet/<int:pet_id>"),  # only authenticated users can delete pets, admins can delete all

    # if an authenticated user has a registered pet dog, they can identify its breed by providing a picture url
    (IdentifyDogBreed, "/pets/identify_dog_breed/<int:pet_id>"),

    (AddProduct, "/products/add_product"),  # only authenticated admins can add products
    (GetProducts, "/products"),  # everyone can see products (public part)
    (GetProduct, "/products/<int:product_id>"),  # everyone can see products (public part)
    (EditProduct, "/products/edit_product/<int:product_id>"),  # only admins can edit products
    (DeleteProduct, "/products/delete_product/<int:product_id>"),  # only admins can remove products

    (PlaceOrder, "/orders/place_order"),  # only authenticated users can place orders

    # only authenticated users can book an appointment if they have any registered pets
    (BookAppointment, "/appointments/book_appointment"),
)
