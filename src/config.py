import os

GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")
NOTIFICATION_EMAIL = os.getenv("NOTIFICATION_EMAIL")
REPORT_SCHEDULE = os.getenv("REPORT_SCHEDULE", "daily")