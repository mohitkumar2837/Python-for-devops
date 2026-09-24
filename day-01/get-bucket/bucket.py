import boto3


def get_buckets():
    s3 = boto3.client("s3")

    response = s3.list_buckets()

    return {
        "buckets": [
            bucket["Name"]
            for bucket in response["Buckets"]
        ]
    }