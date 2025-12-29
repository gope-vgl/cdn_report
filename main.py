from utils import dns_check
from .ilo_client import IloClient
from .processors import process_host
from .config import HOSTS_FILE
from .logger_setup import setup_logger
import json

logger = setup_logger("cdn_report", "cdn_report.log")

def load_hosts():
    try:
        with open(HOSTS_FILE) as file:
            return json.load(file)
    except Exception as e:
        logger.error(f"failed to load hosts: {e}")
        raise SystemExit(1)

def main():
    if not check_dns_tcp("172.17.169.41"):
        raise SystemExit("VPN not connected, aborting...")
    hosts = load_hosts()
    client = IloClient()
    for host in hosts:
        process_host(client, host) 
if __name__ == "__main__":
    main()
