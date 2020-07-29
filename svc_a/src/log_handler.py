import logging
from logging.handlers import TimedRotatingFileHandler


def rotate_log_by_minute(path="logs/user_agent.log"):
    logger = logging.getLogger("Rotate Log")
    logger.setLevel(logging.INFO)

    handler = TimedRotatingFileHandler(
        path,
        when="s",
        interval=6,
        backupCount=1
    )

    logger.addHandler(handler)

    return logger
