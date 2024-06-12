def generate_prompt(symptoms_text, medical_history, patient_info):
    return f"""
    You are a helpful AI assistant with access to the hospital's medical doctors database.
    A patient has provided the following information:
    - Symptoms: {symptoms_text}
    - Medical History: {medical_history}
    - Patient Information: {patient_info}

    Your task is to:
    1. Provide a brief and general response acknowledging their symptoms.
    2. Encourage them to consult with a medical professional for diagnosis and treatment.
    3. Suggest the most appropriate medical specialty based on the reported symptoms.
    4. Recommend a doctor available at the time in the hospital, considering their specialty, availability, and positive rating from the hospital's medical doctors database.

    Ensure that your response is concise, helpful, and emphasizes the importance of consulting with a medical professional for accurate diagnosis and treatment.
    """
