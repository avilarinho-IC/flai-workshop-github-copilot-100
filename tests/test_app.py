import pytest
from fastapi.testclient import TestClient
from src.app import app

client = TestClient(app)

def test_signup_for_activity():
    # Register for activity (replace 'activity_name' with a valid one from your app)
    activity_name = "Chess Club"
    email = "student@example.com"
    response = client.post(f"/activities/{activity_name}/signup", params={"email": email})
    assert response.status_code == 200
    # Try to register again for the same activity
    response = client.post(f"/activities/{activity_name}/signup", params={"email": email})
    assert response.status_code == 400
    assert "already signed up" in response.json()["detail"]


def test_invalid_activity():
    email = "student@example.com"
    response = client.post(f"/activities/invalid_activity/signup", params={"email": email})
    assert response.status_code == 404
    assert "not found" in response.json()["detail"]
