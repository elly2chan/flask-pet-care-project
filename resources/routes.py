from resources.auth import RegisterUser, LoginUser, ChangePassword
from resources.pet import AddPet, GetPets, EditPet, DeletePet
from resources.order import PlaceOrder, ApproveOrder, RejectOrder
from resources.product import AddProduct, GetProducts, EditProduct, DeleteProduct, GetProduct
from resources.public import GetAboutPage

routes = (
    (RegisterUser, "/register"),  # everyone can register
    (LoginUser, "/login"),  # everyone can log in
    (ChangePassword, "/users/change_password"),
    (GetAboutPage, "/about"),  # everyone can see about page (public)
    (AddPet, "/pets/add_pet"),  # only authenticated users can add pets
    (GetPets, "/pets"),  # only authenticated users can see their pets, admins can see all pets
    (EditPet, "/pets/edit_pet/<int:pet_id>"),  # only authenticated users can edit pets, admins can edit all
    (DeletePet, "/pets/delete_pet/<int:pet_id>"),  # only authenticated users can delete pets, admins can delete all
    (AddProduct, "/products/add_product"),  # only authenticated admins can add products
    (GetProducts, "/products"), # everyone can see products (public part)
    (GetProduct, "/products/<int:product_id>"),  # everyone can see products (public part)
    (EditProduct, "/products/edit_product/<int:product_id>"),  # only admins can edit products
    (DeleteProduct, "/products/delete_product/<int:product_id>"),  # only admins can remove products
    (PlaceOrder, "/orders/place_order"),  # only authenticated users can place orders
    (ApproveOrder, "/orders/approve_order/<int:order_id>"),  # only admins can approve orders
    (RejectOrder, "/orders/reject_order/<int:order_id>"),  # only admins can deny orders
)
