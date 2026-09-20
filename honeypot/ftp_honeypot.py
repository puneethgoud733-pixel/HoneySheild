import socket

from config import FTP_PORT
from detector import analyze_payload
from logger import record_event


def start_ftp_honeypot():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    server.bind(("0.0.0.0", FTP_PORT))
    server.listen(20)

    print(f"[FTP] Honeypot listening on port {FTP_PORT}")

    while True:
        client, address = server.accept()

        source_ip, source_port = address

        try:
            banner = (
                b"220 FTP Service Ready\r\n"
            )

            client.sendall(banner)

            data = client.recv(2048)

            payload = data.decode(
                "utf-8",
                errors="replace"
            )

            event_type, severity, message = analyze_payload(payload)

            record_event(
                source_ip,
                source_port,
                FTP_PORT,
                "FTP",
                event_type,
                severity,
                message,
                payload[:2000]
            )

        except Exception as error:
            record_event(
                source_ip,
                source_port,
                FTP_PORT,
                "FTP",
                "ERROR",
                "MEDIUM",
                str(error),
                ""
            )

        finally:
            client.close()
