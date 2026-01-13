import socket
from logger.logger_setup import setup_logger

logger = setup_logger('cdn_report', 'cdn_report.log')

def check_vpn(host: str, port=53, timeout=5) -> bool:
    try:
        with socket.create_connection((host, port), timeout= timeout):
            logger.info(f'VPN OK - connected to {host}:{port}')
            return True
    except socket.timeout as e:
        logger.error(f'Connection failed, please connect to VPN: {e}')
        return False
    except Exception as e:
        logger.error(f'VPN check failed: {e}')
        return False
