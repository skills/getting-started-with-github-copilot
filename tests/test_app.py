"""
Tests for the High School Management System API
"""
import sys
from pathlib import Path

# Add src directory to path
sys.path.insert(0, str(Path(__file__).parent.parent / "src"))

from fastapi.testclient import TestClient
from app import app


client = TestClient(app)


class TestRoot:
    """Test root endpoint"""
    
    def test_root_redirect(self):
        """Test that root redirects to static/index.html"""
        response = client.get("/", follow_redirects=False)
        assert response.status_code == 307
        assert response.headers["location"] == "/static/index.html"


class TestActivities:
    """Test activities endpoints"""
    
    def test_get_activities(self):
        """Test retrieving all activities"""
        response = client.get("/activities")
        assert response.status_code == 200
        
        activities = response.json()
        assert isinstance(activities, dict)
        assert len(activities) > 0
        
        # Check that Chess Club exists and has expected fields
        assert "Chess Club" in activities
        assert "description" in activities["Chess Club"]
        assert "schedule" in activities["Chess Club"]
        assert "max_participants" in activities["Chess Club"]
        assert "participants" in activities["Chess Club"]
    
    def test_get_activities_structure(self):
        """Test the structure of returned activities"""
        response = client.get("/activities")
        activities = response.json()
        
        for activity_name, activity_data in activities.items():
            assert isinstance(activity_name, str)
            assert isinstance(activity_data, dict)
            assert "description" in activity_data
            assert "schedule" in activity_data
            assert "max_participants" in activity_data
            assert "participants" in activity_data
            assert isinstance(activity_data["participants"], list)


class TestSignup:
    """Test signup endpoint"""
    
    def test_signup_new_participant(self, reset_activities):
        """Test signing up a new participant"""
        email = "newstudent@mergington.edu"
        activity = "Chess Club"
        
        response = client.post(
            f"/activities/{activity}/signup",
            params={"email": email}
        )
        
        assert response.status_code == 200
        result = response.json()
        assert "message" in result
        assert email in result["message"]
        assert activity in result["message"]
        
        # Verify participant was added
        activities_response = client.get("/activities")
        activities = activities_response.json()
        assert email in activities["Chess Club"]["participants"]
    
    def test_signup_duplicate_participant(self, reset_activities):
        """Test that duplicate signups return 400 error"""
        email = "michael@mergington.edu"
        activity = "Chess Club"
        
        response = client.post(
            f"/activities/{activity}/signup",
            params={"email": email}
        )
        
        assert response.status_code == 400
        result = response.json()
        assert "Already signed up" in result["detail"]
    
    def test_signup_nonexistent_activity(self, reset_activities):
        """Test signing up for non-existent activity"""
        email = "newstudent@mergington.edu"
        activity = "Nonexistent Activity"
        
        response = client.post(
            f"/activities/{activity}/signup",
            params={"email": email}
        )
        
        assert response.status_code == 404
        result = response.json()
        assert "Activity not found" in result["detail"]
    
    def test_signup_multiple_activities(self, reset_activities):
        """Test that a student can sign up for multiple activities"""
        email = "newstudent@mergington.edu"
        
        # Sign up for Chess Club
        response1 = client.post(
            "/activities/Chess Club/signup",
            params={"email": email}
        )
        assert response1.status_code == 200
        
        # Sign up for Programming Class
        response2 = client.post(
            "/activities/Programming Class/signup",
            params={"email": email}
        )
        assert response2.status_code == 200
        
        # Verify in both activities
        activities_response = client.get("/activities")
        activities = activities_response.json()
        assert email in activities["Chess Club"]["participants"]
        assert email in activities["Programming Class"]["participants"]


class TestUnregister:
    """Test unregister endpoint"""
    
    def test_unregister_participant(self, reset_activities):
        """Test unregistering a participant from an activity"""
        email = "michael@mergington.edu"
        activity = "Chess Club"
        
        # Verify participant is enrolled
        activities_response = client.get("/activities")
        assert email in activities_response.json()["Chess Club"]["participants"]
        
        # Unregister
        response = client.delete(
            f"/activities/{activity}/unregister",
            params={"email": email}
        )
        
        assert response.status_code == 200
        result = response.json()
        assert "message" in result
        assert email in result["message"]
        assert activity in result["message"]
        
        # Verify participant was removed
        activities_response = client.get("/activities")
        assert email not in activities_response.json()["Chess Club"]["participants"]
    
    def test_unregister_nonexistent_participant(self, reset_activities):
        """Test unregistering someone not in the activity"""
        email = "nonexistent@mergington.edu"
        activity = "Chess Club"
        
        response = client.delete(
            f"/activities/{activity}/unregister",
            params={"email": email}
        )
        
        assert response.status_code == 400
        result = response.json()
        assert "Not signed up" in result["detail"]
    
    def test_unregister_from_nonexistent_activity(self, reset_activities):
        """Test unregistering from non-existent activity"""
        email = "michael@mergington.edu"
        activity = "Nonexistent Activity"
        
        response = client.delete(
            f"/activities/{activity}/unregister",
            params={"email": email}
        )
        
        assert response.status_code == 404
        result = response.json()
        assert "Activity not found" in result["detail"]


class TestEdgeCases:
    """Test edge cases and special scenarios"""
    
    def test_special_characters_in_email(self, reset_activities):
        """Test email with special characters"""
        email = "test+special@mergington.edu"
        
        response = client.post(
            "/activities/Chess Club/signup",
            params={"email": email}
        )
        
        assert response.status_code == 200
    
    def test_url_encoded_activity_name(self, reset_activities):
        """Test activity names with spaces are properly handled"""
        email = "newstudent@mergington.edu"
        
        # Chess Club has a space, should be URL encoded
        response = client.post(
            "/activities/Chess%20Club/signup",
            params={"email": email}
        )
        
        assert response.status_code == 200
