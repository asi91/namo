import os
from azure.storage.blob import BlobServiceClient

ACCESS_STATS = {}


def read_blob_data_from_azure():
    ACCESS_STATS.clear()
    connect_str = "<ACCESS_KEY_HERE>"

    # Create the BlobServiceClient object which will be used to create a container client
    blob_service_client = BlobServiceClient.from_connection_string(connect_str)

    # Container
    container_name = "hamza"

    # Create a file in local data directory to upload and download
    dir_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    logs_path = os.path.join(dir_path, "logs")

    container_client = blob_service_client.get_container_client(container_name)

    # List the blobs in the container
    blob_list = container_client.list_blobs()

    for blob in blob_list:
        file_name = blob.name
        blob_client = blob_service_client.get_blob_client(container=container_name, blob=file_name)
        for data in blob_client.download_blob().readall().decode("utf8").split("\n"):
            data = data.strip().lower()
            if data:
                ACCESS_STATS.setdefault(data, 0)
                ACCESS_STATS[data] += 1
