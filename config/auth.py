import os

CONFIG_FILE = os.environ.get("CONFIG_FILE", "config/config.json")
USER = os.environ.get("CDN_USER", "admin")
PASSWD = os.environ.get("CDN_PASS", "cl4r0vtr")
FAILBACK_PASSWD = os.environ.get("CDN_FAILBACK_PASS", "cl4rovtr")
