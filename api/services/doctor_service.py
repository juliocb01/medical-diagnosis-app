from api import db
from api.models import Doctor

def get_all_doctors():
    doctors = Doctor.query.all()
    return [{"id": doctor.id, "name": doctor.name, "specialty": doctor.specialty, "availability": doctor.availability, "rating": doctor.rating, "symptoms": doctor.symptoms} for doctor in doctors]

def get_doctor_by_id(doctor_id):
    doctor = Doctor.query.get(doctor_id)
    if doctor:
        return {"id": doctor.id, "name": doctor.name, "specialty": doctor.specialty, "availability": doctor.availability, "rating": doctor.rating, "symptoms": doctor.symptoms}
    else:
        return None

def create_doctor(data):
    new_doctor = Doctor(
        name=data.get('name'),
        specialty=data.get('specialty'),
        availability=data.get('availability'),
        rating=data.get('rating'),
        symptoms=data.get('symptoms')
    )
    db.session.add(new_doctor)
    db.session.commit()
    return {"id": new_doctor.id, "name": new_doctor.name, "specialty": new_doctor.specialty, "availability": new_doctor.availability, "rating": new_doctor.rating, "symptoms": new_doctor.symptoms}

def update_doctor(doctor_id, data):
    doctor = Doctor.query.get(doctor_id)
    if doctor:
        doctor.name = data.get('name', doctor.name)
        doctor.specialty = data.get('specialty', doctor.specialty)
        doctor.availability = data.get('availability', doctor.availability)
        doctor.rating = data.get('rating', doctor.rating)
        doctor.symptoms = data.get('symptoms', doctor.symptoms)
        db.session.commit()
        return {"id": doctor.id, "name": doctor.name, "specialty": doctor.specialty, "availability": doctor.availability, "rating": doctor.rating, "symptoms": doctor.symptoms}
    else:
        return None

def delete_doctor(doctor_id):
    doctor = Doctor.query.get(doctor_id)
    if doctor:
        db.session.delete(doctor)
        db.session.commit()
        return True
    else:
        return False
