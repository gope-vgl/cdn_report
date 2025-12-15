import os

#Paths
HOSTS_FILE = os.environ.get("HOSTS_FILE", "data/hosts.json")

#Credentials

USERNAME = os.environ.get("USERNAME", "admin")
PASSWORDS = os.environ.get("PASSWORDS", ["cl4r0vtr", "cl4rovtr"])

print(f'{HOSTS_FILE}')
print(f'{USERNAME}')
print(f'{PASSWORDS}')
