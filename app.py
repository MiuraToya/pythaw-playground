"""Lambda handler that delegates to service classes and utility functions."""
from services.dynamo import DynamoService
from services.notification import send_notification
from services.s3 import S3Service


def handler(event, context):
    s3 = S3Service()
    dynamo = DynamoService()

    user = dynamo.get_user(event["user_id"])
    buckets = s3.list_buckets()

    send_notification(
        topic_arn=event["topic_arn"],
        message=f"User {user} has {len(buckets)} buckets",
    )

    return {"statusCode": 200, "body": "ok"}
