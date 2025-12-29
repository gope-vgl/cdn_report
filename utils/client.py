import requests
from requests.exceptions import Timeout, RequestException
from .config import USERNAME, PASSWORDS
from .logger_setup import setup_logger

logger = setup_logger("cdn_report", "cdn_report.log")

class IloClient:
    def get_health_summary(self, ip, timeout=5):
        url = f"https://{ip}/json/health_summary"
        try:
            response = requests.get(url, auth=(USERNAME, PASSWORDS[0]), verify = False, timeout = timeout)
            if not response.ok:
                logger.error(f"{ip} --> HTTP {response.status_code}")
                return None
            return response.json()
        except Timeout:
            logger.error(f"{ip} --> Request timed out")
            return None
        except RequestException as e:
            logger.error(f"{ip} --> Request error: {e}")
            return None
        except ValueError:
            logger.error(f"{ip} --> Invalid JSON response")
            return None
