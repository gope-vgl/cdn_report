import requests
from requests.exceptions import Timeout, RequestException
from logger.logger_setup import logger_setup

logger = logger_setup("cdn_report", "cdn_report.log")

class IloClient:
    def get_health_summary(self, ip, username, password, timeout=5):
        url = f"https://{ip}/json/health_summary"
        try:
            response = requests.get(url, auth=(username, password), verify = False, timeout = timeout)
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
