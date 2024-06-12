from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from google.cloud import aiplatform
from dotenv import load_dotenv
import os

load_dotenv()

db = SQLAlchemy()
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv("DATABASE_URL")
db.init_app(app)

# Initialize Gemini API client
endpoint = aiplatform.Endpoint(os.getenv("GEMINI_ENDPOINT_NAME"))

from api.routes import register_routes
register_routes(app)

# Initialize medspacy
import medspacy
from medspacy.ner import TargetRule

nlp = medspacy.load()
nlp.get_pipe('target_matcher').add([
    TargetRule('stroke', 'CONDITION'),
    TargetRule('diabetes', 'CONDITION'),
    TargetRule('pna', 'CONDITION'),
    # Add more rules as needed
])
