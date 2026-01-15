import os
import urllib3
from urllib3.exceptions import InsecureRequestWarning

from logger.logger_setup import setup_logger
from utils.json_utils import json_load
from utils.host_check import check_vpn
from utils.ilo_client import IloClient
from processors.host_processor import process_host
from config.auth import CONFIG_FILE


# Disable SSL warnings (iLO uses self-signed certs)
urllib3.disable_warnings(InsecureRequestWarning)

logger = setup_logger("cdn_report", "cdn_report.log")

def main() -> None:
    logger.debug("Starting CDN Report")
    
    config_file = os.environ.get("CONFIG_FILE", "config/config.json")

    try:
        config = json_load(config_file)
    except Exception:
        logger.critical("Failed to load configuration file")
        raise SystemExit(1)

    try:
        hosts = json_load(config["hosts_file"])
    except KeyError:
        logger.critical("Missing 'hosts_file' key in config file")
        raise SystemExit()
    except Exception:
        logger.critical("Failed to load hosts file")
        raise SystemExit(1)

    if not check_vpn(config["dns_ip"]):
        logger.critical("VPN not connected - exiting")
        raise SystemExit(1)

    client = IloClient()
    for host in hosts:
        process_host(host, client)

    logger.debug("CDN Report Finished")

if __name__ == "__main__":
    main()
