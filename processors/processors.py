from .validators import validate_key
from .logger_setup import setup_logger

logger = setup_logger("cdn_report", "cdn_report.log")

def process_host(client, host: dict):
    hostname = host["hostname"]
    ip = host["ip"]
    logger.info(f"Analyzing host {hostname} ({ip})")
    data = client.get_health_summary(ip)
    if data is None:
        logger.error(f"Failed to read health summary from {hostname}")
    for key, valuein data.items():
        result = validate_key(key, value)
        if result is None:
            continue
        if result:
            logger.info(f"{key}: {value} --> PASS")
        else:
            logger.error(f"{key}: {value} --> FAILED")
