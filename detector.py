def analyze_payload(payload):
    if not payload:
        return "CONNECTION", "LOW", "Connection received"

    text = payload.lower()

    suspicious_patterns = {
        "admin": "Possible administrative probing",
        "login": "Possible login attempt",
        "password": "Possible credential probing",
        "passwd": "Possible password-file probing",
        "etc/passwd": "Possible Linux file probing",
        "cmd": "Possible command probing",
        "shell": "Possible shell probing",
        "select ": "Possible SQL injection pattern",
        "union ": "Possible SQL injection pattern",
        "script": "Possible script injection pattern",
        "../": "Possible path traversal pattern"
    }

    for pattern, message in suspicious_patterns.items():
        if pattern in text:
            return "SUSPICIOUS_ACTIVITY", "HIGH", message

    return "DATA_RECEIVED", "MEDIUM", "Data received from connection"
