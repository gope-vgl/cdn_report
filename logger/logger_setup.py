import logging
from logging.handlers import RotatingFileHandler
from colorlog import ColoredFormatter

def logger_setup(name: str = "app", filename: str = "app.log", level: int = logging.DEBUG, max_bytes: int = 5_000_000, backup_count: int = 3):
    logger = logging.getLogger(name)
    logger.setLevel(level)
    logger.propagate = False

    console_formatter = ColoredFormatter("%(log_color)s[%(asctime)s] [%(levelname)s] %(message)s", datefmt = "%Y-%m-%d %H:%M:%S", log_colors={"DEBUG": "cyan", "INFO": "green", "WARNING": "yellow", "ERROR": "red", "CRITICAL": "red, bold" })
    
    file_formatter = logging.Formatter("[%(asctime)s] [%(levelname)s] %(message)s", datefmt="%Y-%m-%d %H:%M:%S" )

    console_handler = logging.StreamHandler()
    console_handler.setLevel(level)
    console_handler.setFormatter(console_formatter)

    file_handler = RotatingFileHandler(filename, maxBytes = max_bytes, backupCount = backup_count)
    file_handler.setLevel(level)
    file_handler.setFormatter(file_formatter)

    if not logger.handlers:
        logger.addHandler(console_handler)
        logger.addHandler(file_handler)

    return logger
