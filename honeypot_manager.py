import threading

from database import initialize_database
from honeypot.http_honeypot import start_http_honeypot
from honeypot.ssh_honeypot import start_ssh_honeypot
from honeypot.ftp_honeypot import start_ftp_honeypot


def main():
    initialize_database()

    services = [
        start_http_honeypot,
        start_ssh_honeypot,
        start_ftp_honeypot
    ]

    threads = []

    for service in services:
        thread = threading.Thread(
            target=service,
            daemon=True
        )

        thread.start()
        threads.append(thread)

    print()
    print("=" * 50)
    print("       HONEYSHIELD HONEYPOT")
    print("=" * 50)
    print("HTTP : 8080")
    print("SSH  : 2222")
    print("FTP  : 2121")
    print("=" * 50)
    print("Honeypot is running...")
    print("Press CTRL+C to stop.")
    print()

    try:
        while True:
            pass

    except KeyboardInterrupt:
        print("\nHoneyShield stopped.")


if __name__ == "__main__":
    main()
