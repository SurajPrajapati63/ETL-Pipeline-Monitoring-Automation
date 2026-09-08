from azure.storage.blob import BlobServiceClient
from config.config import Config


class BlobClient:

    def __init__(self):

        self.client = BlobServiceClient.from_connection_string(
            Config.AZURE_CONNECTION_STRING
        )

        self.container = self.client.get_container_client(
            Config.CONTAINER_NAME
        )

    def list_blobs(self):
        return self.container.list_blobs()

    def get_blob_client(self, blob_name):
        return self.container.get_blob_client(blob_name)