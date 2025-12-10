import json
import requests
import socket
from requests.exceptions import Timeout
from requests.packages.urllib3.exceptions import InsecureRequestWarning

requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

def check_dns_tcp(host, port=53, timeout=5):
    try:
        with socket.create_connection((host, port), timeout=timeout) as s:
            print('Connection succesfully established to VPN')
    except socket.timeout:
        raise TimeoutError(f"Connection timed out, Please connect to VPN")
    except Exception as e:
        raise Exception(f"DNS TCP check failed: {e}")

print(check_dns_tcp('172.17.169.41'))

try:
    with open('hosts.json', 'r') as file:
        hosts = json.load(file)
except FileNotFoundError:
    print('File not found') 
except json.JSONDecodeError:
    print('Invalid JSON Format')

for host in hosts:
    url = f'https://{host['ip']}/json/health_summary?'
    username = 'admin'
    password = 'cl4r0vtr'
    print(f'\033[36mAnalyzing host: {host['hostname']}, ilo ip:{host['ip']}\033[0m')
    try:
        response = requests.get(url, auth=(username, password), verify=False, timeout=5).json()
        keys = ['self_test', 'system_health', 'hostpwr_state', 'fans_status', 'fans_redundancy', 'temperature_status', 'power_supplies_status', 'power_supplies_redundancy', 'power_supplies_mismatch', 'storage_status', 'nic_status', 'cpu_status', 'mem_status', 'ext_hlth_status']
        values = ['OP_STATUS_OK', 'ON', 'REDUNDANT', 0]
        for key, value in response.items():
            if key in keys:
                if value in values:
                    print(f'\033[92m{key}: {value} --> PASS\033[0m')
                else:
                    print(f'\033[91m{key}: {value} --> FAILED\033[0m')
    except Timeout:
        print(f'\033[91mHost: {host['hostname']}, ilo ip:{host['ip']} request timed out\033[0m')
