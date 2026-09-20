# HoneyShield

## Multi-Service Honeypot for Network Threat Detection and Monitoring

HoneyShield is a Python-based cybersecurity project that provides simulated network services for observing and recording suspicious network interactions in a controlled environment.

The system captures connection activity from HTTP, SSH and FTP-like services, analyzes received data using pattern-based detection, stores security events in SQLite and presents captured events through a Flask-based monitoring dashboard.

## Features

- HTTP honeypot service
- SSH-like honeypot service
- FTP-like honeypot service
- Connection monitoring
- Event logging
- Pattern-based suspicious activity detection
- HIGH, MEDIUM and LOW severity classification
- SQLite event storage
- Flask monitoring dashboard
- Service activity statistics
- Controlled cybersecurity testing environment

## Architecture

```text
Network Activity
       |
       v
+-------------------+
| Honeypot Services |
| HTTP / SSH / FTP  |
+-------------------+
       |
       v
+-------------------+
| Detection Engine  |
+-------------------+
       |
       v
+-------------------+
| Event Logger      |
+-------------------+
       |
       v
+-------------------+
| SQLite Database   |
+-------------------+
       |
       v
+-------------------+
| Flask Dashboard   |
+-------------------+
