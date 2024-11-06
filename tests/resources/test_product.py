# (AddProduct, "/products/add_product"),  # only authenticated admins can add products
# (GetProducts, "/products"),  # everyone can see products (public part)
# (GetProduct, "/products/<int:product_id>"),  # everyone can see products (public part)
# (EditProduct, "/products/edit_product/<int:product_id>"),  # only admins can edit products
# (DeleteProduct, "/products/delete_product/<int:product_id>"),  # only admins can remove products