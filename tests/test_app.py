import pytest
from fastapi.testclient import TestClient
from src import app as app_module

client = TestClient(app_module.app)


def test_get_activities():
    """GET /activities should return the activities dictionary."""
    response = client.get("/activities")
    assert response.status_code == 200
    data = response.json()
    # Basic sanity checks
    assert isinstance(data, dict)
    assert "Chess Club" in data
    assert isinstance(data["Chess Club"].get("participants"), list)


def test_signup_for_activity():
    """POST signup should add the email to the activity participants."""
    activity = "Chess Club"
    test_email = "test.user@example.com"

    # Ensure clean state before test
    participants = app_module.activities[activity]["participants"]
    if test_email in participants:
        participants.remove(test_email)

    try:
        response = client.post(f"/activities/{activity}/signup", params={"email": test_email})
        assert response.status_code == 200
        assert response.json() == {"message": f"Signed up {test_email} for {activity}"}
        assert test_email in app_module.activities[activity]["participants"]
    finally:
        # Cleanup added test email
        if test_email in app_module.activities[activity]["participants"]:
            app_module.activities[activity]["participants"].remove(test_email)
