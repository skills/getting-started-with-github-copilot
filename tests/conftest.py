import sys
from pathlib import Path

# Add src directory to path so we can import app
sys.path.insert(0, str(Path(__file__).parent.parent / "src"))

import pytest
from fastapi.testclient import TestClient
from app import app


@pytest.fixture
def client():
    """Create a test client for the FastAPI app"""
    return TestClient(app)


@pytest.fixture
def reset_activities():
    """Reset activities to initial state before each test"""
    from app import activities
    
    initial_state = {
        "Chess Club": {
            "description": "Learn strategies and compete in chess tournaments",
            "schedule": "Fridays, 3:30 PM - 5:00 PM",
            "max_participants": 12,
            "participants": ["michael@mergington.edu", "daniel@mergington.edu"]
        },
        "Programming Class": {
            "description": "Learn programming fundamentals and build software projects",
            "schedule": "Tuesdays and Thursdays, 3:30 PM - 4:30 PM",
            "max_participants": 20,
            "participants": ["emma@mergington.edu", "sophia@mergington.edu"]
        },
        "Gym Class": {
            "description": "Physical education and sports activities",
            "schedule": "Mondays, Wednesdays, Fridays, 2:00 PM - 3:00 PM",
            "max_participants": 30,
            "participants": ["john@mergington.edu", "olivia@mergington.edu"]
        },
        "Soccer Team": {
            "description": "Competitive soccer team with regular matches and tournaments",
            "schedule": "Tuesdays and Thursdays, 4:00 PM - 6:00 PM",
            "max_participants": 25,
            "participants": ["james@mergington.edu", "liam@mergington.edu"]
        },
        "Swimming Club": {
            "description": "Swim training and competitive meets",
            "schedule": "Mondays and Wednesdays, 3:30 PM - 5:00 PM",
            "max_participants": 20,
            "participants": ["ava@mergington.edu", "noah@mergington.edu"]
        },
        "Art Studio": {
            "description": "Painting, drawing, and mixed media art projects",
            "schedule": "Thursdays, 3:30 PM - 5:30 PM",
            "max_participants": 15,
            "participants": ["isabella@mergington.edu", "mia@mergington.edu"]
        },
        "Drama Club": {
            "description": "Theater performances, acting workshops, and stage production",
            "schedule": "Tuesdays and Fridays, 3:30 PM - 5:00 PM",
            "max_participants": 30,
            "participants": ["ethan@mergington.edu", "charlotte@mergington.edu"]
        },
        "Robotics Team": {
            "description": "Build and program robots for regional competitions",
            "schedule": "Wednesdays, 3:30 PM - 6:00 PM",
            "max_participants": 18,
            "participants": ["william@mergington.edu", "benjamin@mergington.edu"]
        },
        "Debate Club": {
            "description": "Develop critical thinking and public speaking through competitive debates",
            "schedule": "Mondays, 3:30 PM - 5:00 PM",
            "max_participants": 16,
            "participants": ["amelia@mergington.edu", "lucas@mergington.edu"]
        }
    }
    
    # Clear and reset
    activities.clear()
    activities.update(initial_state)
    yield
    # Reset after test
    activities.clear()
    activities.update(initial_state)
