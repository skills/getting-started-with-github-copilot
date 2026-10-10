from copy import deepcopy

import pytest
from fastapi.testclient import TestClient

from src.app import app, activities, participant_tokens


@pytest.fixture
def client():
    original_activities = deepcopy(activities)
    original_participant_tokens = participant_tokens.copy()
    with TestClient(app) as test_client:
        yield test_client
    activities.clear()
    activities.update(original_activities)
    participant_tokens.clear()
    participant_tokens.update(original_participant_tokens)


def test_get_activities_returns_activity_details(client):
    response = client.get("/activities")

    assert response.status_code == 200
    assert "Chess Club" in response.json()
    assert response.json()["Chess Club"]["participants"] == [
        "michael@mergington.edu",
        "daniel@mergington.edu",
    ]


def test_signup_rejects_duplicate_participant(client):
    response = client.post(
        "/activities/Chess%20Club/signup",
        params={"email": "michael@mergington.edu"},
    )

    assert response.status_code == 400
    assert response.json()["detail"] == "Student is already signed up"


def test_signup_rejects_full_activity(client):
    activity = activities["Swimming Club"]
    activity["participants"] = [
        f"student{index}@mergington.edu"
        for index in range(activity["max_participants"])
    ]

    response = client.post(
        "/activities/Swimming%20Club/signup",
        params={"email": "new.student@mergington.edu"},
    )

    assert response.status_code == 400
    assert response.json()["detail"] == "Activity is full"


def test_signup_and_unregister_update_participants(client):
    email = "new.student@mergington.edu"
    signup_response = client.post(
        "/activities/Chess%20Club/signup",
        params={"email": email},
    )

    assert signup_response.status_code == 200
    assert email in activities["Chess Club"]["participants"]
    token = signup_response.json()["unregister_token"]

    unregister_response = client.delete(
        "/activities/Chess%20Club/signup",
        params={"email": email},
        headers={"Authorization": f"Bearer {token}"},
    )

    assert unregister_response.status_code == 200
    assert email not in activities["Chess Club"]["participants"]


def test_signup_tokens_are_scoped_to_activity(client):
    email = "new.student@mergington.edu"
    chess_response = client.post(
        "/activities/Chess%20Club/signup",
        params={"email": email},
    )
    art_response = client.post(
        "/activities/Art%20Studio/signup",
        params={"email": email},
    )

    assert chess_response.status_code == 200
    assert art_response.status_code == 200
    assert chess_response.json()["unregister_token"] != art_response.json()["unregister_token"]


def test_unregister_rejects_different_student(client):
    email = "michael@mergington.edu"
    response = client.delete(
        "/activities/Chess%20Club/signup",
        params={"email": email},
        headers={"Authorization": "Bearer invalid-token"},
    )

    assert response.status_code == 403
    assert email in activities["Chess Club"]["participants"]


def test_unregister_requires_bearer_token(client):
    response = client.delete(
        "/activities/Chess%20Club/signup",
        params={"email": "michael@mergington.edu"},
    )

    assert response.status_code == 401


def test_signup_rejects_unknown_activity(client):
    response = client.post(
        "/activities/Unknown/signup",
        params={"email": "student@mergington.edu"},
    )

    assert response.status_code == 404
    assert response.json()["detail"] == "Activity not found"