
"""
Water Intake Agent - Database Module
"""

import sqlite3

from datetime import datetime
from zoneinfo import ZoneInfo

from config.settings import DATABASE_PATH, TIMEZONE


def get_connection():
    """Create a connection to the SQLite database."""

    DATABASE_PATH.parent.mkdir(parents=True, exist_ok=True)

    connection = sqlite3.connect(DATABASE_PATH)
    connection.row_factory = sqlite3.Row

    return connection


def initialize_database():
    """Create the water intake table if it does not exist."""

    connection = get_connection()

    try:
        cursor = connection.cursor()

        cursor.execute("""
            CREATE TABLE IF NOT EXISTS water_intake (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                reminder_id TEXT UNIQUE,
                consumed_ml INTEGER NOT NULL DEFAULT 0,
                status TEXT NOT NULL,
                recorded_at TEXT NOT NULL
            )
        """)

        connection.commit()

    finally:
        connection.close()


def record_intake(reminder_id, consumed_ml, status):
    """Record a water consumption acknowledgement."""

    timestamp = datetime.now(TIMEZONE).isoformat()

    connection = get_connection()

    try:
        cursor = connection.cursor()

        cursor.execute("""
            INSERT INTO water_intake
            (reminder_id, consumed_ml, status, recorded_at)
            VALUES (?, ?, ?, ?)
        """, (
            reminder_id,
            consumed_ml,
            status,
            timestamp
        ))

        connection.commit()

        return True

    except sqlite3.IntegrityError:
        return False

    finally:
        connection.close()


def get_daily_total():
    """Calculate today's confirmed water consumption."""

    today = datetime.now(TIMEZONE).date().isoformat()

    connection = get_connection()

    try:
        cursor = connection.cursor()

        cursor.execute("""
            SELECT COALESCE(SUM(consumed_ml), 0)
            FROM water_intake
            WHERE status = 'YES'
            AND substr(recorded_at, 1, 10) = ?
        """, (today,))

        return cursor.fetchone()[0]

    finally:
        connection.close()
