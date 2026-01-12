import json
from logger.logger_setup import logger_setup

logger = logger_setup("cdn_report", "cdn_report.log")

def json_load(path: str):
    try:
        with open(path) as file:
            logger.debug(f"Loading JSON file: {path}")
            return json.load(file)
    except FileNotFoundError:
        logger.error(f"JSON file not found in {path}")
        raise SystemExit(1)
    except json.JSONDecodeError as e:
        logger.error(f"Invalid JSON format in {path}: {e}")
        raise SystemExit(1)
