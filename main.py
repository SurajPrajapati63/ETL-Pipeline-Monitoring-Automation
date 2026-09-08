from config.loggers import get_logger
from database.repository import MonitoringRepository
from scheduler.scheduler import *
from blob_monitor.blob_listener import BlobListener
logger = get_logger()

logger.info("Application Started")

repo = MonitoringRepository()

print("Database Connected Successfully")

logger.info("Database Ready")


listener = BlobListener()

listener.monitor()

print("Blob Monitoring Completed")