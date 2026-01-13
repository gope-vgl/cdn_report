import os
from logger.logger_setup import setup_logger
from utils.json_utils import json_load
from utils.host_check import check_vpn
from utils.ilo_client import IloClient
from processors.host_processor import process_host
import urllib3
from urllib3.exceptions import InsecureRequestWarning
urllib3.disable_warnings(InsecureRequestWarning)

logger = setup_logger("cdn_report", "cdn_report.log")
config = json_load('config/config.json')
hosts = json_load(config["hosts_file"])
if check_vpn(config["dns_ip"]):
    username = os.environ.get("username", "admin")
    logger.debug(f"Got username: {username}")
    password = os.environ.get("password", "cl4r0vtr")
    logger.debug(f"Got password: {password}")
    client = IloClient()
    logger.debug(f"Succesfully created client: {client}")
    for host in hosts:
        process_host(client, host)
else:
    raise SystemExit(1)
    
