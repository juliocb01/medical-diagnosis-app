from flask import Blueprint, request, jsonify
from api.services.doctor_service import get_all_doctors, get_doctor_by_id, create_doctor, update_doctor, delete_doctor

doctors_bp = Blueprint('doctors', __name__)

@doctors_bp.route('/doctors', methods=['GET'])
def get_doctors():
    doctors = get_all_doctors()
    return jsonify(doctors)

@doctors_bp.route('/doctors/<int:doctor_id>', methods=['GET'])
def get_doctor(doctor_id):
    doctor = get_doctor_by_id(doctor_id)
    if doctor:
        return jsonify(doctor)
    else:
        return jsonify({"error": "Doctor not found"}), 404

@doctors_bp.route('/doctors', methods=['POST'])
def add_doctor():
    data = request.get_json()
    new_doctor = create_doctor(data)
    return jsonify(new_doctor), 201

@doctors_bp.route('/doctors/<int:doctor_id>', methods=['PUT'])
def modify_doctor(doctor_id):
    data = request.get_json()
    updated_doctor = update_doctor(doctor_id, data)
    if updated_doctor:
        return jsonify(updated_doctor)
    else:
        return jsonify({"error": "Doctor not found"}), 404

@doctors_bp.route('/doctors/<int:doctor_id>', methods=['DELETE'])
def remove_doctor(doctor_id):
    result = delete_doctor(doctor_id)
    if result:
        return jsonify({"message": "Doctor deleted"})
    else:
        return jsonify({"error": "Doctor not found"}), 404
