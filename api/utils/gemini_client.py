import os
from google.cloud import aiplatform_v1beta1 as aiplatform

def initialize_gemini_client():
    gemini_endpoint_name = os.getenv("GEMINI_ENDPOINT_NAME")
    gemini_project_id = os.getenv("GEMINI_PROJECT_ID")
    gemini_location = os.getenv("GEMINI_LOCATION")

    client_options = {"api_endpoint": f"{gemini_location}-aiplatform.googleapis.com"}
    client = aiplatform.PredictionServiceClient(client_options=client_options)
    endpoint = client.endpoint_path(gemini_project_id, gemini_location, gemini_endpoint_name)
    return client, endpoint
