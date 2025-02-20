import pytest
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_create_user():
    response = client.post("/users/", json={
        "username": "testuser",
        "email": "testemail@gmail.com",
        "password": "testpassword"
    })