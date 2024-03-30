import sys
from fastapi.testclient import TestClient

sys.path.append("..")

from auth import auth_router

client = TestClient(auth_router, base_url="http://localhost:8000")

def test_signin_success():
    user_credentials = {
        "email": "john.doe@example.com",
        "password": "password123"
    }
    response = client.post("/signin", json=user_credentials)
    assert response.status_code == 200
    assert "access_token" in response.json()
    assert response.json()["token_type"] == "bearer"
