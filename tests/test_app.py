from fastapi.testclient import TestClient

from src.app import activities, app

client = TestClient(app)


def test_duplicate_signup_is_rejected():
    activity = "Chess Club"
    email = "michael@mergington.edu"

    response = client.post(f"/activities/{activity}/signup?email={email}")

    assert response.status_code == 400
    assert response.json()["detail"] == "Student is already signed up"


def test_activity_capacity_is_enforced():
    activity = "Gym Class"
    email = "newstudent@mergington.edu"
    original = list(activities[activity]["participants"])

    try:
        activities[activity]["participants"] = [
            f"student{i}@mergington.edu" for i in range(activities[activity]["max_participants"])
        ]

        response = client.post(f"/activities/{activity}/signup?email={email}")

        assert response.status_code == 400
        assert response.json()["detail"] == "Activity is full"
    finally:
        activities[activity]["participants"] = original
