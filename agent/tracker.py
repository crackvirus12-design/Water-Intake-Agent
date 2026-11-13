
"""
Water Intake Agent - Tracking Logic
"""

from config.settings import DEFAULT_GLASS_SIZE_ML
from agent.database import record_intake, get_daily_total


def acknowledge_reminder(reminder_id, consumed=True, amount_ml=None):
    """
    Record the user's response to a water reminder.

    YES = Record consumed water.
    NO = Record zero consumption.
    """

    if amount_ml is None:
        amount_ml = DEFAULT_GLASS_SIZE_ML

    if consumed:
        if not isinstance(amount_ml, int) or amount_ml <= 0:
            raise ValueError("Water quantity must be a positive integer.")

        status = "YES"
        quantity = amount_ml

    else:
        status = "NO"
        quantity = 0

    return record_intake(
        reminder_id,
        quantity,
        status
    )


def mark_missed(reminder_id):
    """Record a reminder that received no response."""

    return record_intake(
        reminder_id,
        0,
        "MISSED"
    )


def get_total_consumption():
    """Return today's confirmed water intake in ml."""

    return get_daily_total()


def get_total_consumption_litres():
    """Return today's confirmed water intake in litres."""

    total_ml = get_total_consumption()

    return round(total_ml / 1000, 2)
