import requests
from requests.exceptions import Timeout, RequestException
from logger.logger_setup import setup_logger

logger = setup_logger("cdn_report", "cdn_report.log")

class IloClient:
    def get_health_summary(self, ip, username, password, failback_password,  timeout=5):
        url = f"https://{ip}/json/health_summary"
        try:
            response = requests.get(url, auth=(username, password), verify = False, timeout = timeout)
            if not response.ok:
                if response.status_code == 403:
                    logger.warning(f'403 Forbidden, re-trying using failback password')
                    response = requests.get(url, auth=(username, failback_password), verify = False, timeout = timeout)
                else:
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
