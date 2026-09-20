import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

DATABASE_PATH = os.path.join(BASE_DIR, "database", "honeypot.db")
LOG_PATH = os.path.join(BASE_DIR, "logs", "honeypot.log")

HTTP_PORT = 8080
SSH_PORT = 2222
FTP_PORT = 2121

DASHBOARD_PORT = 5000
