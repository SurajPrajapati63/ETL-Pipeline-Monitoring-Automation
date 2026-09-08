from blob_monitor.blob_client import BlobClient
from blob_monitor.blob_metadata import BlobMetadata
from blob_monitor.blob_utils import (
    get_profile_name,
    get_procedure_name
)

from database.repository import MonitoringRepository

from config.loggers import get_logger

logger = get_logger()


class BlobListener:

    def __init__(self):

        self.client = BlobClient()

        self.repo = MonitoringRepository()

    def monitor(self):

        blobs = self.client.list_blobs()

        for blob in blobs:

            metadata = BlobMetadata.build(blob)

            file_name = metadata["file_name"]

            if self.repo.file_exists(file_name):
                continue

            serial = self.repo.get_next_serial()

            values = (

                serial,

                file_name,

                get_profile_name(file_name),

                get_procedure_name(file_name),

                "WAITING",

                metadata["blob_arrival_time"].strftime("%b %d, %Y, %I:%M %p"),

                None,

                None,

                None,

                None,

                None,

                metadata["size"],

                None,

                "Blob detected"

            )

            self.repo.insert(values)

            logger.info(f"New File Detected : {file_name}")