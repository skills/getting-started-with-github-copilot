"""
High School Management System API

A simple FastAPI application that allows students to view and sign up
for extracurricular activities at Mergington High School.
"""

from fastapi import FastAPI, HTTPException, Query
from fastapi.staticfiles import StaticFiles
from fastapi.responses import RedirectResponse
from pydantic import BaseModel, EmailStr
from typing import Dict
import os
from pathlib import Path

app = FastAPI(
    title="Mergington High School API",
    description="API for viewing and signing up for extracurricular activities"
)

# Mount the static files directory
static_dir = os.path.join(Path(__file__).parent, "static")
app.mount("/static", StaticFiles(directory=static_dir), name="static")


# In-memory activity database
activities: Dict[str, dict] = {
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
    }
}


class SignupRequest(BaseModel):
    email: EmailStr


@app.get("/", include_in_schema=False)
def root():
    return RedirectResponse(url="/static/index.html")


@app.get("/activities")
def get_activities():
    """Get all activities and their details"""
    return activities


@app.post("/activities/{activity_name}/signup")
def signup_for_activity(activity_name: str, signup: SignupRequest):
    """Sign up a student for an activity"""
    email = signup.email

    # Validate activity exists
    if activity_name not in activities:
        raise HTTPException(status_code=404, detail="Activity not found")

    activity = activities[activity_name]

    # Check if already signed up
    if email in activity["participants"]:
        raise HTTPException(status_code=400, detail="Already signed up for this activity")

    # Check if activity is full
    if len(activity["participants"]) >= activity["max_participants"]:
        raise HTTPException(status_code=400, detail="Activity is full")

    # Add participant
    activity["participants"].append(email)
    return {"message": f"Successfully signed up {email} for {activity_name}"}
