import os
import json
import datetime
from flask import Flask, jsonify, request, abort

app = Flask(__name__)
LOG_FILE = "incident_logs.json"  # File to store incident logs

# API Key for authentication
API_KEY = "myownapi"

# Helper function to log incidents
def log_incident(incident_type, description):
    incident = {
        "timestamp": datetime.datetime.now().isoformat(),
        "type": incident_type,
        "description": description
    }

    # Creates the file if it doesn't exist
    if not os.path.exists(LOG_FILE):
        with open(LOG_FILE, "w") as f:
            json.dump([], f)

    # Loads existing logs
    with open(LOG_FILE, "r") as f:
        logs = json.load(f)

    # Appends the new incident to the logs
    logs.append(incident)

    # Write back to the file
    with open(LOG_FILE, "w") as f:
        json.dump(logs, f)


# To check the API key
@app.before_request
def check_api_key():
    if request.endpoint not in ('index', 'invalid_key'): 
        api_key = request.headers.get("x-api-key")
        if api_key != API_KEY:
            abort(401, description="Unauthorized: Invalid API Key")


# Route to log a new incident
@app.route('/add-incident', methods=['POST'])
def add_incident():
    try:
        data = request.json
        if not data or 'type' not in data or 'description' not in data:
            return jsonify({"error": "Invalid data"}), 400

        log_incident(data['type'], data['description'])
        return jsonify({"status": "success", "message": "Incident logged"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500


# Route to retrieve all logged incidents
@app.route('/logs', methods=['GET'])
def get_logs():
    if not os.path.exists(LOG_FILE):
        return jsonify({"error": "No incidents logged yet"}), 404

    with open(LOG_FILE, "r") as f:
        logs = json.load(f)

    return jsonify(logs)


@app.errorhandler(401)
def invalid_key(error):
    return jsonify({"error": str(error)}), 401


@app.route('/')
def index():
    return jsonify({"message": "Welcome to the Incident Response System!"})


if __name__ == '__main__':
    app.run(debug=True)
