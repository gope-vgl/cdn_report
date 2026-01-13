import json
from typing import Any
from logger.logger_setup import setup_logger

logger = setup_logger("cdn_report", "cdn_report.log")

def json_load(path: str) -> Any:
    try:
        with open(path, encoding="utf-8") as file:
            logger.info(f"Loading JSON file from {path}")
            json_file = json.load(file)
            logger.debug(f"JSON loaded succesfully")
            return json_file
    except FileNotFoundError as e:
        logger.error(f"JSON file not found in {path}: {e}")
        raise e
    except json.JSONDecodeError as e:
        logger.error(f"Invalid JSON format in {path}: {e}")
        raise e

def json_out(path: str, data: Any) -> None:
    try:
        with open(path, 'w') as jsonfile:
            logger.info(f"Writing JSON file to {path}")
            json.dump(data, jsonfile)
    except OSError as e:
        logger.error(f"Failed to write JSON file {path}: {e}")
        raise e
