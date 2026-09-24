import boto3


def upload_file(file, bucket_name, file_name):
    s3 = boto3.client("s3")

    s3.upload_fileobj(
        file,
        bucket_name,
        file_name
    )

    return {    
        "message": "File uploaded successfully",
        "bucket": bucket_name,
        "file": file_name
        
    }