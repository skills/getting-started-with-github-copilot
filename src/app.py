"""
High School Management System API

A super simple FastAPI application that allows students to view and sign up
for extracurricular activities at Mergington High School.
"""

from fastapi import FastAPI, HTTPException
from fastapi.staticfiles import StaticFiles
from fastapi.responses import RedirectResponse
from pymongo import MongoClient
import os
from pathlib import Path

app = FastAPI(title="Mergington High School API",
              description="API for viewing and signing up for extracurricular activities")

# Configuração do MongoDB
client = MongoClient('mongodb://localhost:27017/')
db = client['school_activities']

# Mount the static files directory
current_dir = Path(__file__).parent
app.mount("/static", StaticFiles(directory=os.path.join(Path(__file__).parent,
          "static")), name="static")


@app.get("/")
def root():
    return RedirectResponse(url="/static/index.html")


@app.get("/activities")
def get_activities():
    # Busca todas as atividades do MongoDB e converte para o formato esperado pelo frontend
    activities_list = db.activities.find({}, {'_id': 0})  # Exclui o campo _id
    return {activity['name']: {k: v for k, v in activity.items() if k != 'name'} 
            for activity in activities_list}


@app.post("/activities/{activity_name}/signup")
def signup_for_activity(activity_name: str, email: str):
    """Sign up a student for an activity"""
    # Busca a atividade no MongoDB
    activity = db.activities.find_one({"name": activity_name})
    
    # Valida se a atividade existe
    if not activity:
        raise HTTPException(status_code=404, detail="Activity not found")
    
    # Valida se ainda há vagas
    if len(activity['participants']) >= activity['max_participants']:
        raise HTTPException(status_code=400, detail="Activity is full")
    
    # Valida se o email já está inscrito
    if email in activity['participants']:
        raise HTTPException(status_code=400, detail="Already signed up for this activity")
    
    # Adiciona o participante
    result = db.activities.update_one(
        {"name": activity_name},
        {"$push": {"participants": email}}
    )
    
    if result.modified_count == 1:
        return {"message": "Successfully signed up for the activity"}
    else:
        raise HTTPException(status_code=500, detail="Failed to sign up for activity")
