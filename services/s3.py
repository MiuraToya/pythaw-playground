"""S3 service wrapper."""
import boto3


class S3Service:
    def __init__(self):
        self.client = boto3.client("s3")      # PW001
        self.resource = boto3.resource("s3")  # PW002

    def list_buckets(self):
        return self.client.list_buckets()

    def upload(self, bucket, key, body):
        self.resource.Bucket(bucket).put_object(Key=key, Body=body)
