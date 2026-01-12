import os

user = os.environ.get("ILO_USER", "admin")
password = os.environ.get("ILO_PASS", "cl4r0vtr")
config_path = os.environ.get("CONFIG_PATH,", "config/config.json")
