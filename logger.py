import logging
import os
from datetime import datetime

from config import LOG_PATH
from database import insert_event


os.makedirs(os.path.dirname(LOG_PATH), exist_ok=True)

logging.basicConfig(
    filename=LOG_PATH,
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s"
)


def record_event(
    source_ip,
    source_port,
    destination_port,
    service,
    event_type,
    severity,
    message,
    payload=""
):
    timestamp = datetime.now().isoformat(timespec="seconds")

    logging.info(
        "%s | %s:%s -> %s | %s | %s | %s",
        service,
        source_ip,
        source_port,
        destination_port,
        event_type,
        severity,
        message
    )

    insert_event(
        timestamp,
        source_ip,
        source_port,
        destination_port,
        service,
        event_type,
        severity,
        message,
        payload
    )
