class BlobMetadata:

    @staticmethod
    def build(blob):

        return {

            "file_name": blob.name,

            "blob_arrival_time": blob.last_modified,

            "size": blob.size,

            "etag": blob.etag,

            "content_type": getattr(
                blob.content_settings,
                "content_type",
                None
            )

        }