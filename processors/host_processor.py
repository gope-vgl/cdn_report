import os
from validators.validators import validate_key
from logger.logger_setup import logger_setup

logger = logger_setup("cdn_report", "cdn_report.log")

def process_host(client, host: dict):
    hostname = host["hostname"]
    ip = host["ip"]
    logger.info(f'''------------------------------------------------------
                            | Analyzing host: {hostname} with ip: {ip} |
                            -------------------------------------------------------''')
    username = os.environ.get("username", "admin")
    password = os.environ.get("password", "cl4r0vtr")
    data = client.get_health_summary(ip, username, password)
    if data is None:
        logger.error(f"Failed to read health summary from {hostname}")
    else:
        for key, value in data.items():
            result = validate_key(key, value)
            if result is None:
                continue
            if result:
                logger.info(f"{key}: {value} --> PASS")
            else:
                logger.error(f"{key}: {value} --> FAILED")
