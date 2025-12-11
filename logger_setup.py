import logging
from logging.handlers import RotatingFileHandler

def setup_logger(name: str = "app", log_file: str = "app.log", level: int = logging.INFO, max_bytes: int = 5_000_000, backup_count: int = 3):
    logger = logging.getLogger(name)
    logger.setLevel(level)
    logger.propagate = False

    formatter = logging.Formatter("[%(asctime)s] [%(levelname)s] %(message)s", datefmt="%Y-%m-%d %H:%M:%S" )

    ch = logging.StreamHandler()
    ch.setLevel(level)
    ch.setFormatter(formatter)

    fh = RotatingFileHandler(log_file, maxBytes = max_bytes, backupCount = backup_count)
    fh.setLevel(level)
    fh.setFormatter(formatter)

    if not logger.handlers:
        logger.addHandler(ch)
        logger.addHandler(fh)

    return logger
