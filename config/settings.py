
"""
Water Intake Agent - Application Settings
"""

import os
from zoneinfo import ZoneInfo
from pathlib import Path

# Project root directory
BASE_DIR = Path(__file__).resolve().parent.parent

# Timezone
TIMEZONE = ZoneInfo("Asia/Kolkata")

# Daily tracking configuration
START_HOUR = 6
END_HOUR = 19

# Water intake configuration
DEFAULT_GLASS_SIZE_ML = 250
DAILY_WATER_TARGET_ML = 2500

# Database configuration
DATA_DIR = BASE_DIR / "data"
DATABASE_PATH = Path(
    os.getenv(
        "DATABASE_PATH",
        str(DATA_DIR / "water_intake.db")
    )
)

# Scheduler configuration
REMINDER_INTERVAL_MINUTES = 60

# Application configuration
APP_NAME = "Water Intake Agent"
APP_VERSION = "1.0.0"

def display_settings():
    """Display application configuration."""

    print("=" * 40)
    print(APP_NAME)
    print("=" * 40)

    print(f"Version: {APP_VERSION}")
    print(f"Timezone: {TIMEZONE}")
    print(f"Tracking starts: {START_HOUR}:00")
    print(f"Tracking ends: {END_HOUR}:00")
    print(f"Glass size: {DEFAULT_GLASS_SIZE_ML} ml")
    print(f"Daily target: {DAILY_WATER_TARGET_ML} ml")
    print(f"Database: {DATABASE_PATH}")

    print("=" * 40)
