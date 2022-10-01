#check if file exists in bucket

#upload file to google cloud storage bucket
from google.cloud import storage

class transcript():

    def __init__(self):
        pass






def upload_blob(bucket_name, source_file_name, destination_blob_name):
    """Uploads a file to the bucket."""
    # The ID of your GCS bucket
    # bucket_name = "your-bucket-name"
    # The path to your file to upload
    # source_file_name = "local/path/to/file"
    # The ID of your GCS object
    # destination_blob_name = "storage-object-name"

    storage_client = storage.Client()
    bucket = storage_client.bucket(bucket_name)
    blob = bucket.blob(destination_blob_name)

    blob.upload_from_filename(source_file_name)

    print(
        f"File {source_file_name} uploaded to {destination_blob_name}."
    )


upload_blob("bucket_video_ibrahim" , "D:\music\Marshmello.mp4" , "Marshmello.mp4")


transcript().upload_blob()  # call the function