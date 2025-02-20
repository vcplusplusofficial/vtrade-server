import pytest
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_create_user():
    response = client.post("/users/", json={
        "username": "testuser",
        "email": "testemail@gmail.com",
        "password": "testpassword",
        "first_name": "Johnny",
        "last_name": "Test"
    })
    assert response.status_code == 200
    data = response.json()
    assert data["username"] == "testuser"
    assert data["email"] == "testemail@gmail.com"
    assert data["first_name"] == "Johnny"
    assert data["last_name"] == "Test"
