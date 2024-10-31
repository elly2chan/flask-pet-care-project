from resources.auth import RegisterUser, LoginUser, ChangePassword

routes = (
    (RegisterUser, "/register"),  # everyone can register
    (LoginUser, "/login"),  # everyone can log in
    (ChangePassword, "/users/change_password"),
    # ('', "/about"),  # everyone can see about page (public)
    # ('', "/pets/add_pet"),  # only authenticated users can add pets
    # ('', "/pets"),  # only authenticated users can see their pets, admins can see all pets
    # ('', "/pets/edit_pet/<int:pet_id>"),  # only authenticated users can edit pets, admins can edit all
    # ('', "/pets/delete_pet/<int:pet_id>"),  # only authenticated users can delete pets, admins can delete all
    # ('', "/products/add_product"),  # only authenticated admins can add products
    # ('', "/products"),
    # ('', "/products/<int:product_id>"),# everyone can see products (public part)
    # ('', "/products/edit_product/<int:product_id>"),  # only admins can edit products
    # ('', "/products/delete_product<int:product_id>"),  # only admins can remove products
    # ('', "/orders/place_order"),  # only authenticated users can place orders
    # ('', "/orders/approve_order/<int:order_id>"),  # only admins can approve orders
    # ('', "/orders/deny_order/<int:order_id>"),  # only admins can deny orders
)
