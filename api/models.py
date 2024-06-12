from api import db

class Doctor(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    specialty = db.Column(db.String(100), nullable=False)
    availability = db.Column(db.String, nullable=False)  # Example: "Mon-Fri, 9am-5pm"
    rating = db.Column(db.Float, nullable=False)
    symptoms = db.Column(db.String, nullable=False)  # Example: "Chest pain, Shortness of breath, Palpitations, Dizziness"

class Patient(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    medical_history = db.Column(db.Text)
    # ... other relevant fields
