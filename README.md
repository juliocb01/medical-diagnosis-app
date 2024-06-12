# Medical Diagnosis and Doctor Appointment App

## Project Overview

This project is a mobile application developed using FlutterFlow that allows patients to chat with an AI assistant for medical diagnosis and doctor appointment scheduling. The AI assistant, powered by Google's Gemini 1.5 Pro, provides a preliminary diagnosis based on the patient's symptoms and medical history. It recommends appropriate doctors based on their specialty, availability, and rating.

## Project Structure

```graphql
project/
├── api/                    # Flask API
│   ├── __init__.py         # Initialize Flask app and extensions
│   ├── app.py              # Main API entry point
│   ├── models.py           # Database models
│   ├── database.py         # Database connection and functions
│   ├── routes/             # Directory for route definitions
│   │   ├── __init__.py     # Initialize routes
│   │   ├── diagnose.py     # Route for diagnosis
│   │   └── doctors.py      # Route for doctor-related operations
│   ├── services/           # Directory for service layers
│   │   ├── __init__.py     # Initialize services
│   │   ├── diagnose_service.py # Service logic for diagnosis
│   │   └── doctor_service.py   # Service logic for doctor operations
│   ├── utils/              # Utility functions
│   │   ├── __init__.py     # Initialize utils
│   │   ├── gemini_client.py # Initialize Gemini client
│   │   ├── time_utils.py   # Utilities for time-related operations
│   │   └── prompt_utils.py # Utilities for prompt generation
│   └── requirements.txt    # Project dependencies
├── flutter_app/            # FlutterFlow project (exported code)
│   └── ...
└── scripts/                # Helper scripts
    └── load_doctors.py     # Script to load doctor data
```

## Getting Started

### Prerequisites

- Python 3.9+
- Flask
- Flask-SQLAlchemy
- Google Cloud AI Platform
- medspacy
- dotenv
- google-cloud-aiplatform

### Installation

1. **Clone the repository:**

    ```bash
    git clone https://github.com/yourusername/medical-diagnosis-app.git
    cd medical-diagnosis-app
    ```

2. **Set up a virtual environment:**

    ```bash
    python3 -m venv venv
    source venv/bin/activate
    ```

3. **Install the dependencies:**

    ```bash
    pip install -r api/requirements.txt
    ```

4. **Set up environment variables:**

    Create a `.env` file in the `api/` directory with the following content:

    ```env
    DATABASE_URL=sqlite:///your_database.db
    GEMINI_ENDPOINT_NAME=your_endpoint_id
    GEMINI_PROJECT_ID=your_project_id
    GEMINI_LOCATION=your_location
    ```

5. **Initialize the database:**

    ```bash
    python api/database.py
    ```

6. **Load doctor data:**

    ```bash
    python scripts/load_doctors.py
    ```

7. **Verify Google Cloud Authentication:**

    Ensure you are authenticated with Google Cloud:

    ```bash
    gcloud auth application-default login
    ```

### Running the Application

1. **Start the Flask API:**

    ```bash
    python api/app.py
    ```

2. **Export the FlutterFlow project code and run the Flutter app.**

## API Endpoints

### Diagnose

- **URL:** `/api/diagnose`
- **Method:** `POST`
- **Description:** Receives patient symptoms and medical history, and returns a preliminary diagnosis along with recommended doctors.
- **Request Body:**

    ```json
    {
        "symptoms": "Chest pain, shortness of breath",
        "medical_history": "History of diabetes",
        "patient_info": "John Doe, 35, Male"
    }
    ```

- **Response:**

    ```json
    {
        "message": "You might be experiencing...",
        "recommended_doctors": [
            {
                "id": 1,
                "name": "Dr. John Doe",
                "specialty": "Cardiologist",
                "availability": "Mon-Fri, 9am-5pm",
                "rating": 4.5
            }
        ],
        "extracted_symptoms": ["Chest pain", "shortness of breath"],
        "patient_info": "John Doe, 35, Male"
    }
    ```

## Contributing

We welcome contributions to enhance the functionality of this project. To contribute:

1. Fork the repository.
2. Create a new branch for your feature or bugfix.
3. Make your changes and commit them with clear messages.
4. Push your changes to your forked repository.
5. Submit a pull request to the main repository.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.
