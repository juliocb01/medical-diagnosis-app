from flask import Blueprint, request, jsonify
from api.services.diagnose_service import diagnose_patient

diagnose_bp = Blueprint('diagnose', __name__)

@diagnose_bp.route('/diagnose', methods=['POST'])
def diagnose():
    data = request.get_json()
    response_data = diagnose_patient(data)
    return jsonify(response_data)