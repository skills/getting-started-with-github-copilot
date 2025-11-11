from fastapi.testclient import TestClient
from src.app import app, activities


client = TestClient(app)


def test_get_activities():
    resp = client.get("/activities")
    assert resp.status_code == 200
    data = resp.json()
    assert isinstance(data, dict)
    # Ensure a known activity is present
    assert "Chess Club" in data


def test_signup_and_unregister_flow():
    activity = "Chess Club"
    email = "test.student@mergington.edu"

    # Ensure clean state: remove if already present
    if email in activities[activity]["participants"]:
        activities[activity]["participants"].remove(email)

    # Sign up
    resp = client.post(f"/activities/{activity}/signup", params={"email": email})
    assert resp.status_code == 200
    assert email in activities[activity]["participants"]

    # Sign up again -> should fail (already signed up)
    resp2 = client.post(f"/activities/{activity}/signup", params={"email": email})
    assert resp2.status_code == 400

    # Unregister
    resp3 = client.post(f"/activities/{activity}/unregister", params={"email": email})
    assert resp3.status_code == 200
    assert email not in activities[activity]["participants"]


def test_unregister_nonexistent():
    activity = "Chess Club"
    email = "nonexistent@mergington.edu"

    # Ensure not registered
    if email in activities[activity]["participants"]:
        activities[activity]["participants"].remove(email)

    resp = client.post(f"/activities/{activity}/unregister", params={"email": email})
    assert resp.status_code == 400
