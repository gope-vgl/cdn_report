import socket
from logger.logger_setup import setup_logger

logger = setup_logger('cdn_report', 'cdn_report.log')

def check_dns(host: str, port=53, timeout=5) -> bool:
    try:
        with socket.create_connection((host, port), timeout= timeout):
            logger.info(f'VPN/TCP DNS OK - connected to {host}:{port}')
            return True
    except socket.timeout:
        logger.error('Connection timed out, please connect to VPN')
        return False
    except Exception as e:
        logger.error(f'DNS TCP check failed: {e}')
        return False
