import pytest
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

@pytest.fixture
def user_payload():
    return {
        "username": "testuser",
        "email": "testemail@gmail.com",
        "password": "testpassword",
        "first_name": "Johnny",
        "last_name": "Test"
    }

@pytest.fixture
def create_user(user_payload):
    response = client.post("/users/", json=user_payload)
    assert response.status_code == 200
    data = response.json()

    yield data
    client.delete(f"/users/{data["id"]}")

def test_create_user(create_user):
    assert create_user["username"] == "testuser"
    assert create_user["email"] == "testemail@gmail.com"
    assert create_user["first_name"] == "Johnny"
    assert create_user["last_name"] == "Test"

def test_read_user(create_user):
    user_id = create_user["id"]
    response = client.get(f"/users/{user_id}")
    assert response.status_code == 200
    data = response.json()

    assert data["username"] == "testuser"
    assert data["email"] == "testemail@gmail.com"
    assert data["first_name"] == "Johnny"
    assert data["last_name"] == "Test"

def test_update_user(create_user):
    user_id = create_user["id"]
    update_payload = {
        "username": "new_testuser",
        "first_name": "New_John",
        "last_name": "New_Test",
        "email": "New_testemail@gmail.com"
    }

    client.put(f"/users/{user_id}", json=update_payload)
    updated_response = client.get(f"/users/{user_id}")
    data = updated_response.json()
    assert data["username"] == "new_testuser"
    assert data["first_name"] == "New_John"
    assert data["last_name"] == "New_Test"
    assert data["email"] == "New_testemail@gmail.com"






