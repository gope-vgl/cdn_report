import os
from validators.validators import validate_key
from logger.logger_setup import setup_logger
from utils.ilo_client import IloClient
from config.auth import USER, PASSWD, FAILBACK_PASSWD

logger = setup_logger("cdn_report", "cdn_report.log")

def process_host( host: dict[str, str], client: IloClient) -> bool:
    hostname = host["hostname"]
    ip = host["ip"]
    logger.debug(f'***** Analyzing host: {hostname} ({ip}) *****')
    data = client.get_health_summary(ip, USER, PASSWD,FAILBACK_PASSWD)
    if data is None:
        logger.error(f"Failed to read health summary from {hostname} {ip}")
    else:
        for key, value in data.items():
            result = validate_key(key, value)
            if result is None:
                continue
            if result:
                logger.info(f"{key}: {value} --> PASS")
                success = True
            else:
                logger.error(f"{key}: {value} --> FAILED")
                success = False
        return success
