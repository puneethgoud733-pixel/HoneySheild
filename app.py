from flask import Flask, render_template

from database import initialize_database, get_recent_events, get_statistics


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


if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=5000,
        debug=False
    )
