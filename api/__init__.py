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
gemini_endpoint_name = os.getenv("GEMINI_ENDPOINT_NAME")
gemini_project_id = os.getenv("GEMINI_PROJECT_ID")
gemini_location = os.getenv("GEMINI_LOCATION")

client_options = {"api_endpoint": f"{gemini_location}-aiplatform.googleapis.com"}
endpoint = aiplatform.Endpoint(
    endpoint_name=gemini_endpoint_name,
    project=gemini_project_id,
    location=gemini_location,
    client_options=client_options
)

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
