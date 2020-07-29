import os
from azure.storage.blob import BlobServiceClient
from azure.core.exceptions import ResourceExistsError

def backup_file_to_azure():
    connect_str = "<ACCESS_KEY_HERE>"

    # Create the BlobServiceClient object which will be used to create a container client
    blob_service_client = BlobServiceClient.from_connection_string(connect_str)

    # Create a unique name for the container
    container_name = "hamza"

    # Create a file in local data directory to upload and download
    # file_name = "user_agent.log"
    dir_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    logs_path = os.path.join(dir_path, "logs")

    _, _, f_names = next(os.walk(logs_path))
    file_name = max(f_names)

    upload_file_path = os.path.join(logs_path, file_name)

    # Create a blob client using the local file name as the name for the blob
    blob_client = blob_service_client.get_blob_client(container=container_name, blob=file_name)

    print("\nUploading to Azure Storage as blob:\n\t" + file_name)

    # Upload the created file
    with open(upload_file_path, "rb") as data:
        try:
            blob_client.upload_blob(data)
        except ResourceExistsError as e:
            print("No new logs. Ignoring..")
