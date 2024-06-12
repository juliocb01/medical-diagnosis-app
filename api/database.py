from flask_sqlalchemy import SQLAlchemy
from flask import Flask

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///your_database.db'  # Choose SQLite or another database
db = SQLAlchemy(app)

from api.models import Doctor, Patient  # Import your models here

db.create_all()  # Create tables if they don't exist

# Add sample data (if needed)
def add_sample_data():
    doctor1 = Doctor(name='Dr. John Doe', specialty='Cardiologist', availability='Mon-Fri, 9am-5pm', rating=4.5, symptoms='Chest pain, Shortness of breath, Palpitations, Dizziness')
    db.session.add(doctor1)
    db.session.commit()

if __name__ == '__main__':
    add_sample_data()
