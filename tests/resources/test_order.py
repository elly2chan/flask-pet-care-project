import pytest
from unittest.mock import patch
from models import OrderModel
from models.enums import Status
from tests.base import app, client, database
from tests.factories import UserFactory, ProductFactory

USER_PASSWORD = 'test'


@pytest.fixture
def user(database):
    """Fixture to create a user for the tests."""
    user = UserFactory(password=USER_PASSWORD)
    return user


@pytest.fixture
def auth_token(client, user):
    """Fixture to log in a user and return an authentication token."""
    login_data = {"email": user.email, "password": USER_PASSWORD}
    response = client.post("/login", json=login_data)
    return response.json["token"]


def test_place_order_success(client, database, user, auth_token):
    """Test successful order placement."""
    product = ProductFactory(quantity=100, price=10.0)

    order_data = {
        "product_id": product.id,
        "quantity": 1,
        "address": "test address"
    }
    headers = {"Authorization": f"Bearer {auth_token}"}

    with patch('managers.order.OrderManager.issue_transaction') as mock_transaction:
        # Simulate a successful transaction by returning mock transaction and transfer
        mock_transaction.return_value = ("mock_transaction", {"status": "incoming_payment_waiting"})

    response = client.post("/orders/place_order", json=order_data, headers=headers)

    assert response.status_code == 201
    order = OrderModel.query.filter_by(customer_id=user.id).first()
    assert order
    assert order.status == Status.approved
    assert order.total_price == 10.0
    assert product.quantity == 99


def test_place_order_product_not_found(client, database, user, auth_token):
    """Test placing an order with a non-existent product."""
    order_data = {
        "product_id": 99999,  # Non-existent product_id
        "quantity": 1
    }
    headers = {"Authorization": f"Bearer {auth_token}"}

    response = client.post("/orders/place_order", json=order_data, headers=headers)

    assert response.status_code == 400
    assert response.json == {'message': "Invalid fields {'address': ['Missing data for required field.']}"}


def test_place_order_transaction_failed(client, database, user, auth_token):
    """Test order placement when the transaction fails."""
    product = ProductFactory(quantity=100, price=10.0)

    order_data = {
        "product_id": product.id,
        "quantity": 1,
        "address": "test address"
    }
    headers = {"Authorization": f"Bearer {auth_token}"}

    with patch('managers.order.OrderManager.issue_transaction') as mock_transaction:
        mock_transaction.side_effect = Exception("Transaction failed")

        response = client.post("/orders/place_order", json=order_data, headers=headers)

        assert response.status_code == 500
        assert "Order processing failed" in response.json["message"]
        order = OrderModel.query.filter_by(customer_id=user.id).first()
        assert order
        assert order.status == Status.rejected


def test_place_order_missing_fields(client, database, user, auth_token):
    """Test placing an order with missing fields (e.g., quantity)."""
    product = ProductFactory(quantity=100, price=10.0)

    order_data = {
        "product_id": product.id,
        "address": "test address"
    }
    headers = {"Authorization": f"Bearer {auth_token}"}

    response = client.post("/orders/place_order", json=order_data, headers=headers)

    assert response.status_code == 400
    assert "quantity" in response.json["message"]
