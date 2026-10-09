import sqlite3
from pathlib import Path
from config import DATABASE_PATH

def get_connection():
    db_path = Path(DATABASE_PATH)
    db_path.parent.mkdir(parents=True, exist_ok=True)

    connection = sqlite3.connect(str(db_path))
    connection.row_factory = sqlite3.Row
    return connection

def initialize_database():
    connection = get_connection()

    connection.execute("""
        CREATE TABLE IF NOT EXISTS events (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            timestamp TEXT NOT NULL,
            source_ip TEXT NOT NULL,
            source_port INTEGER,
            destination_port INTEGER,
            service TEXT NOT NULL,
            event_type TEXT NOT NULL,
            severity TEXT NOT NULL,
            message TEXT,
            payload TEXT
        )
    """)

    connection.commit()
    connection.close()


def insert_event(
    timestamp,
    source_ip,
    source_port,
    destination_port,
    service,
    event_type,
    severity,
    message,
    payload
):
    connection = get_connection()

    connection.execute("""
        INSERT INTO events (
            timestamp,
            source_ip,
            source_port,
            destination_port,
            service,
            event_type,
            severity,
            message,
            payload
        )
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
    """, (
        timestamp,
        source_ip,
        source_port,
        destination_port,
        service,
        event_type,
        severity,
        message,
        payload
    ))

    connection.commit()
    connection.close()


def get_recent_events(limit=100):
    connection = get_connection()

    rows = connection.execute("""
        SELECT *
        FROM events
        ORDER BY id DESC
        LIMIT ?
    """, (limit,)).fetchall()

    connection.close()

    return rows


def get_statistics():
    connection = get_connection()

    total = connection.execute(
        "SELECT COUNT(*) FROM events"
    ).fetchone()[0]

    high = connection.execute(
        "SELECT COUNT(*) FROM events WHERE severity = 'HIGH'"
    ).fetchone()[0]

    medium = connection.execute(
        "SELECT COUNT(*) FROM events WHERE severity = 'MEDIUM'"
    ).fetchone()[0]

    low = connection.execute(
        "SELECT COUNT(*) FROM events WHERE severity = 'LOW'"
    ).fetchone()[0]

    services = connection.execute("""
        SELECT service, COUNT(*) AS count
        FROM events
        GROUP BY service
        ORDER BY count DESC
    """).fetchall()

    connection.close()

    return {
        "total": total,
        "high": high,
        "medium": medium,
        "low": low,
        "services": services
    }
