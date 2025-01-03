import os
import json
import datetime
from flask import Flask, jsonify, request

app = Flask(__name__)
LOG_FILE = "incident_logs.json"  # File to store incident logs


# Helper function to log incidents
def log_incident(incident_type, description):
    incident = {
        "timestamp": datetime.datetime.now().isoformat(),
        "type": incident_type,
        "description": description
    }

    # Create the file if it doesn't exist
    if not os.path.exists(LOG_FILE):
        with open(LOG_FILE, "w") as f:
            json.dump([], f)

    # Load existing logs
    with open(LOG_FILE, "r") as f:
        logs = json.load(f)

    # Append the new incident to the logs
    logs.append(incident)

    # Write back to the file
    with open(LOG_FILE, "w") as f:
        json.dump(logs, f)


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


if __name__ == '__main__':
    app.run(debug=True)
