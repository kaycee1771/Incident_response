## Incident Response System
### Overview
This application is an update from its old version and now features an added authentication functionality. As previously stated in the initial commit it uses a simple REST API for logging and retrieving cybersecurity incidents. The application is built using Flask and stores incident logs in a JSON file. It now includes API key-based authentication to ensure secure access to the API endpoints.
### Features
- Log Incidents: Add new cybersecurity incidents with details like type and description.
- View Logs: Retrieve  all logged incidents through a RESTful endpoint.
- JSON Storage: Store incidents in a simple JSON file for easy retrieval and management.
- API key authentication for secure access.
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

### API Usage
**Authentication**

All API requests require the inclusion of an API key in the request header. Use the header **x-API-key** with the value set to **myownapi** (default API key).

### Endpoints

**1. Add an Incident (POST /add-incident)**

Logs a new incident by providing incident details in JSON format.

**Request Headers:**
```bash
x-api-key: <your-api-key>
```
```bash
Content-Type: application/json
```
**Request Body:**
```bash
{
  "type": "<incident type>",
  "description": "<incident description>"
}
```
- Linux/Mac:
```bash
curl -X POST http://127.0.0.1:5000/add-incident \
-H "x-api-key: myownapi" \
-H "Content-Type: application/json" \
-d '{"type": "Unauthorized Access", "description": "Failed login attempt detected"}'
```
- Windows:
```bash
curl -X POST http://127.0.0.1:5000/add-incident ^
-H "x-api-key: myownapi" ^
-H "Content-Type: application/json" ^
-d "{\"type\": \"Unauthorized Access\", \"description\": \"Failed login attempt detected\"}"
```
**Response:**
```bash
{
  "status": "success",
  "message": "Incident logged"
}
```

**2. Retrieve Incident Logs (GET /logs)**

Retrieves a list of all logged incidents.

**Request Headers:**
```bash
x-api-key: <myownapi>
```

- Linux/Mac:
```bash
curl -X GET http://127.0.0.1:5000/logs -H "x-api-key: myownapi"
```
- Windows:
```bash
curl -X GET http://127.0.0.1:5000/logs -H "x-api-key: myownapi"
```
- Response:
```bash
[
  {
    "timestamp": "2025-01-03T14:00:00.000000",
    "type": "Network Issue",
    "description": "Internet connection is down"
  },
  {
    "timestamp": "2025-01-03T15:00:00.000000",
    "type": "System Crash",
    "description": "Mainframe unexpectedly rebooted."
  }
]
```

File Structure
```bash
incident-response/
│
├── incident_response.py  # Main application code
├── incident_logs.json    # Stores logged incidents (JSON format)
├── requirements.txt      # Project dependencies
└── README.md             # Project documentation
```
### Notes
1. **Customizing the API Key:** You can change the default API key and customize it to any value you want, to change the default API key,  update the **API_KEY** variable in the **incident_response.py** file.
### License
This project is licensed under the MIT License.
