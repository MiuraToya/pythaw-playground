"""Sample Lambda with violations for testing pythaw output formats."""
import boto3


def handler(event, context):
    client = boto3.client("s3")       # PW001
    resource = boto3.resource("s3")   # PW002
    session = boto3.Session()         # PW003
    return client.list_buckets()
