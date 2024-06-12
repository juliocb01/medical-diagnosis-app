from api import db, endpoint, nlp
from api.models import Doctor, Patient
from api.utils.time_utils import get_current_time, get_current_day
from api.utils.prompt_utils import generate_prompt
import medspacy

def diagnose_patient(data):
    symptoms_text = data.get('symptoms')
    medical_history = data.get('medical_history', '')
    patient_info = data.get('patient_info', '')

    # Extract Symptoms using medspacy
    doc = nlp(symptoms_text)
    extracted_symptoms = [ent.text for ent in doc.ents]

    # Generate Prompt
    prompt = generate_prompt(symptoms_text, medical_history, patient_info)

    # Call Gemini API
    response = endpoint.predict(prompt)
    diagnosis_text = response.text

    # Find Matching Doctors
    recommended_doctors = find_doctors_by_symptoms(extracted_symptoms)

    return {
        "message": diagnosis_text,
        "recommended_doctors": recommended_doctors,
        "extracted_symptoms": extracted_symptoms,
        "patient_info": patient_info
    }

def find_doctors_by_symptoms(symptoms):
    matching_doctors = []
    for symptom in symptoms:
        doctors = Doctor.query.filter(Doctor.symptoms.ilike(f"%{symptom}%")).all()
        matching_doctors.extend(doctors)

    matching_doctors = list(set(matching_doctors))
    available_doctors = [doctor for doctor in matching_doctors if is_doctor_available(doctor)]
    available_doctors.sort(key=lambda x: x.rating, reverse=True)

    return [{"id": doctor.id, "name": doctor.name, "specialty": doctor.specialty, "availability": doctor.availability, "rating": doctor.rating} 
            for doctor in available_doctors]

def is_doctor_available(doctor):
    current_time = get_current_time()
    current_day = get_current_day()
    availability = parse_availability(doctor.availability)

    if current_day in availability:
        for time_slot in availability[current_day]:
            if is_time_within_slot(current_time, time_slot):
                return True
    return False

def parse_availability(availability_str):
    availability = {}
    days_slots = availability_str.split(',')
    for day_slot in days_slots:
        day, slots = day_slot.split(':')
        availability[day.strip()] = [slot.strip() for slot in slots.split('|')]
    return availability

def is_time_within_slot(current_time, time_slot):
    start_time, end_time = time_slot.split('-')
    return start_time <= current_time <= end_time
