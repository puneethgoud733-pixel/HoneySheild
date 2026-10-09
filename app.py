
import os
import hmac
from flask import Flask, render_template, request, jsonify
from database import initialize_database, get_recent_events, get_statistics
from logger import record_event

app = Flask(__name__)
initialize_database()


@app.route("/")
def dashboard():
    events = get_recent_events(100)
    statistics = get_statistics()
    return render_template(
        "dashboard.html",
        events=events,
        statistics=statistics
    )


@app.route("/test-event", methods=["POST"])
def test_event():
    expected = os.environ.get("HONEYPOT_TEST_TOKEN", "")
    supplied = request.headers.get("X-Test-Token", "")

    if not expected or not hmac.compare_digest(supplied, expected):
        return jsonify({"error": "Unauthorized"}), 401

    record_event(
        "127.0.0.1", 0, 5000, "TEST",
        "SUSPICIOUS_ACTIVITY", "HIGH",
        "HoneyShield dashboard test event", "admin test"
    )
    return jsonify({"message": "Test event recorded"}), 201


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=False)
