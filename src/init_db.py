from pymongo import MongoClient

# Dados das atividades
activities = {
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
        "description": "Join the school soccer team and participate in local tournaments",
        "schedule": "Wednesdays and Fridays, 4:00 PM - 5:30 PM",
        "max_participants": 22,
        "participants": ["lucas@mergington.edu", "mateo@mergington.edu"]
    },
    "Basketball Club": {
        "description": "Practice basketball and compete in inter-school matches",
        "schedule": "Tuesdays and Thursdays, 5:00 PM - 6:30 PM",
        "max_participants": 15,
        "participants": ["liam@mergington.edu", "noah@mergington.edu"]
    },
    "Drama Club": {
        "description": "Participate in theater productions and acting workshops",
        "schedule": "Mondays, 4:00 PM - 5:30 PM",
        "max_participants": 18,
        "participants": ["ava@mergington.edu", "mia@mergington.edu"]
    },
    "Art Workshop": {
        "description": "Explore painting, drawing, and sculpture techniques",
        "schedule": "Thursdays, 3:30 PM - 5:00 PM",
        "max_participants": 16,
        "participants": ["isabella@mergington.edu", "amelia@mergington.edu"]
    },
    "Math Olympiad": {
        "description": "Prepare for math competitions and solve challenging problems",
        "schedule": "Wednesdays, 3:30 PM - 5:00 PM",
        "max_participants": 10,
        "participants": ["benjamin@mergington.edu", "elijah@mergington.edu"]
    },
    "Debate Club": {
        "description": "Develop public speaking and argumentation skills",
        "schedule": "Fridays, 4:00 PM - 5:30 PM",
        "max_participants": 14,
        "participants": ["charlotte@mergington.edu", "harper@mergington.edu"]
    }
}

# Conecta ao MongoDB local
client = MongoClient('mongodb://localhost:27017/')

# Cria ou acessa o banco de dados
db = client['school_activities']

# Limpa a coleção de atividades se ela existir
db.activities.drop()

# Insere as atividades no MongoDB
for name, details in activities.items():
    # Adiciona o nome da atividade aos detalhes para facilitar as consultas
    activity_doc = {
        "name": name,
        **details
    }
    db.activities.insert_one(activity_doc)

print("Banco de dados inicializado com sucesso!")

# Cria índices para melhor performance
db.activities.create_index("name", unique=True)

print("Atividades inseridas:")
for activity in db.activities.find():
    print(f"- {activity['name']}: {len(activity['participants'])} participantes")
