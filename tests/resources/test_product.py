import pytest

from db import db
from models import UserModel, ProductModel
from models.enums import RoleType
from tests.factories import UserFactory, ProductFactory

from tests.base import app, database, client


def login_data():
    """
    Helper function to generate login data for the first user in the database.
    """
    user = db.session.query(UserModel).first()

    data = {
        "email": user.email,
        "password": "testpassword"
    }

    return user, data


@pytest.mark.parametrize('endpoint, method, status_code', [
    ('/products/add_product', 'post', 201),  # Add product
    ('/products', 'get', 200),  # Get all products
    ('/products/1', 'get', 200),  # Get specific product
    ('/products/edit_product/1', 'put', 204),  # Edit product
    ('/products/delete_product/1', 'delete', 204)  # Delete product
])
def test_products(client, database, endpoint, method, status_code):
    """
    Test adding, getting, editing, and deleting products.
    """
    # Create a user and login
    UserFactory(password="testpassword", role=RoleType.admin)
    user_data = login_data()

    # Authenticate the user by obtaining the token
    login_response = client.post("/login", json=user_data[1])
    token = login_response.json["token"]
    headers = {"Authorization": f"Bearer {token}"}

    # Test POST (Add product)
    if method == 'post':
        products_data = {
            "title": "Dog bandanna",
            "description": "A cool bandanna for dogs, size S (for medium sized dogs)",
            "quantity": 50,
            "price": 3.50,
            "photo_url": "https://bunny-wp-pullzone-htpc131rqm.b-cdn.net/wp-content/uploads/2021/03/Moms-Best-Pal"
                         "-Pink-Bandana.jpg"
        }
        response = client.post(endpoint, json=products_data, headers=headers)
        assert response.json["title"] == "Dog bandanna"
        assert response.status_code == status_code

    # Test GET (Get product/s)
    elif method == 'get':
        ProductFactory()  # Add a product to the database
        response = client.get(endpoint, headers=headers)
        assert response.status_code == status_code
        assert len(response.json) > 0

    # Test PUT (Edit product)
    elif method == 'put':
        product = ProductFactory()
        product_title = product.title
        product_data = {
            "title": "Dog T-Shirt",
        }
        response = client.put(f"/products/edit_product/{product.id}", json=product_data, headers=headers)
        assert response.json == status_code
        updated_product = db.session.execute(db.select(ProductModel).filter_by(id=product.id)).scalar()
        assert updated_product.title == product_data["title"]
        assert updated_product.title != product_title

    # Test DELETE (Delete Pet)
    elif method == 'delete':
        product = ProductFactory()
        response = client.delete(f"/products/delete_product/{product.id}", headers=headers)
        assert response.json == status_code
        deleted_product = db.session.execute(db.select(ProductModel).filter_by(id=product.id)).scalar()
        assert deleted_product is None
