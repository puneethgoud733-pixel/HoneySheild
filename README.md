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
Writing
🛠️ Technologies Used
Programming Language: Python
Web Framework: Flask
Database: SQLite
Network Services: HTTP, SSH-like and FTP-like honeypot services
Detection Method: Pattern-based suspicious activity detection
Operating System: Kali Linux
Network Analysis: Wireshark
Frontend: HTML, CSS and Flask templates
📂 Project Structure
HoneyShield/
│
├── app.py
├── honeypot.py
├── detection.py
├── logger.py
├── database.py
├── requirements.txt
├── README.md
│
├── templates/
│   └── dashboard.html
│
├── static/
│   └── style.css
│
├── screenshots/
│
└── honeyshield.db

⚙️ Installation and Setup
1. Clone the Repository
git clone <YOUR_GITHUB_REPOSITORY_URL>
cd HoneyShield
2. Create a Virtual Environment
python3 -m venv venv
3. Activate the Environment
source venv/bin/activate
4. Install Dependencies
pip install -r requirements.txt
5. Start the Application
python3 app.py
If your honeypot services run in a separate script, start them using the appropriate command for your implementation.
6. Open the Dashboard
Open your browser and navigate to:
http://127.0.0.1:5000
The dashboard address and port may differ depending on your Flask configuration.
🔍 Detection and Monitoring
HoneyShield uses pattern-based detection to examine activity received by its simulated services.
The monitoring workflow includes:
Receiving a network connection or service interaction.
Extracting relevant connection information.
Checking received data against configured suspicious patterns.
Assigning a severity level of HIGH, MEDIUM or LOW.
Recording security events in an SQLite database.
Displaying recorded events and service statistics on the monitoring dashboard.
Severity levels depend on the rules configured in the detection engine. They are indicators for investigation, not definitive proof of a successful attack.
📊 Security Events Monitored
Depending on the implemented detection rules, the system can record:
Connection timestamps
Source IP addresses
Target service information
Suspicious request patterns
Detected event categories
Severity classifications
Service activity statistics
Only include fields that your application actually captures and stores.
🧪 Testing
Test the application in an isolated lab environment using systems and traffic you are authorized to control.
Verify that each configured honeypot service starts successfully.
Generate harmless test connections to the relevant services.
Check whether connection events are recorded correctly.
Verify suspicious-pattern detection using predefined test inputs.
Confirm that events are stored in SQLite.
Check that the dashboard displays the stored events and statistics.
Review application logs for errors.

 

🚀 Future Enhancements
Real-time dashboard updates.
Email or messaging alerts for high-severity events.
Advanced detection rules and configurable patterns.
Event filtering and searchable security logs.
IP reputation lookups.
Integration with an intrusion detection system (IDS).
Exportable security incident reports.
Improved dashboard authentication and access controls.
🎓 Learning Outcomes
Through HoneyShield, this project explores:
Network security monitoring.
Honeypot architecture and simulated services.
Python-based security automation.
Pattern-based threat detection.
SQLite database management.
Flask web application development.
Security event analysis and incident monitoring.
👨‍💻 Author
Cybersecurity Student : G.Puneeth goud
Areas of Interest: Network Security | Threat Detection | Network Administration | Defensive Security
📄 License
Choose an appropriate open-source license before publishing this project for reuse. If no license has been added, all rights remain reserved by default.
