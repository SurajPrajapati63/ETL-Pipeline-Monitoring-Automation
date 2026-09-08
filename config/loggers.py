from loguru import logger
import os

os.makedirs("logs", exist_ok=True)

logger.add(
    "logs/monitor.log",
    rotation="10 MB",
    retention="15 days",
    level="INFO",
    format="{time} | {level} | {message}"
)

def get_logger():
    return logger