import socket
from datetime import datetime

from config import HTTP_PORT
from detector import analyze_payload
from logger import record_event


def start_http_honeypot():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    server.bind(("0.0.0.0", HTTP_PORT))
    server.listen(20)

    print(f"[HTTP] Honeypot listening on port {HTTP_PORT}")

    while True:
        client, address = server.accept()

        source_ip, source_port = address

        try:
            data = client.recv(4096)

            payload = data.decode(
                "utf-8",
                errors="replace"
            )

            event_type, severity, message = analyze_payload(payload)

            record_event(
                source_ip,
                source_port,
                HTTP_PORT,
                "HTTP",
                event_type,
                severity,
                message,
                payload[:2000]
            )

            response = (
                "HTTP/1.1 200 OK\r\n"
                "Content-Type: text/html\r\n"
                "Connection: close\r\n"
                "\r\n"
                "<html>"
                "<head><title>HoneyShield</title></head>"
                "<body>"
                "<h1>Server Online</h1>"
                "<p>HoneyShield monitoring service.</p>"
                "</body>"
                "</html>"
            )

            client.sendall(response.encode())

        except Exception as error:
            record_event(
                source_ip,
                source_port,
                HTTP_PORT,
                "HTTP",
                "ERROR",
                "MEDIUM",
                str(error),
                ""
            )

        finally:
            client.close()
