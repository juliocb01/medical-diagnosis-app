import csv
from api import db
from api.models import Doctor

def load_doctors_from_csv(file_path):
    with open(file_path, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            doctor = Doctor(
                name=row['name'],
                specialty=row['specialty'],
                availability=row['availability'],
                rating=float(row['rating']),
                symptoms=row['symptoms']
            )
            db.session.add(doctor)
        db.session.commit()

if __name__ == '__main__':
    file_path = 'path/to/your/doctors.csv'  # Update this with the path to your CSV file
    load_doctors_from_csv(file_path)
