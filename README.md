## Incident Response System
### Overview
This Incident Response System is a simple, Flask-based web application that logs, manages, and retrieves cybersecurity incidents. It enables cybersecurity professionals or teams to document incidents such as network failures, unauthorized access attempts, system crashes, etc. The system stores incident data in a JSON file for persistence and supports a RESTful API for easy integration with other tools.
### Features
- Log Incidents: Add new cybersecurity incidents with details like type and description.
- View Logs: Retrieve all logged incidents through a RESTful endpoint.
- JSON Storage: Store incidents in a simple JSON file for easy retrieval and management.
### Installation
Follow the steps below to set up and run the project locally.
### Prerequisites
Before running the application, make sure you have the following installed:

- Python 3.6 or higher
- pip (Python package installer)

### Setup
1. Clone the repository:
   
```bash
git clone https://github.com/your-username/incident-response.git
cd incident-response
```

2. Install dependencies: Install the required Python libraries by running:
   
```bash
pip install -r requirements.txt
```
- The requirements.txt file should include:
```bash
Flask==2.2.3
```

3. Run the application: Start the Flask server by running:

```bash
python incident_response.py
```
- By default, the application will run on http://127.0.0.1:5000/.

4. Verify the application:

- Open a web browser or use curl to make a GET request to the / endpoint to verify it's running:
```bash
curl http://127.0.0.1:5000/
```
- You should see a message:
{"message": "Welcome to the Incident Response System!"}

### Endpoints
**1. GET /logs**

Retrieve a list of all logged incidents.

- Response:
Returns a JSON array containing all incidents, or a 404 error if no incidents are logged.

**2. POST /add-incident**

Log a new incident by providing incident details in JSON format.

- Response:
Returns a success message if the incident is logged successfully, or an error if required fields are missing.

File Structure
```bash
incident-response/
│
├── incident_response.py  # Main application code
├── incident_logs.json    # Stores logged incidents (JSON format)
├── requirements.txt      # Project dependencies
└── README.md             # Project documentation
```

### License
This project is licensed under the MIT License.
