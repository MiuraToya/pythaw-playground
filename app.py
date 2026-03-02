"""Sample Lambda with violations for testing pythaw output formats."""
import boto3


class S3Service:
    def __init__(self):
        self.client = boto3.client("s3")        # PW001 (nested in class)
        self.resource = boto3.resource("s3")     # PW002 (nested in class)

    def list_buckets(self):
        return self.client.list_buckets()


class DynamoService:
    def __init__(self):
        self.table = boto3.resource("dynamodb").Table("users")  # PW002

    def get_user(self, user_id):
        return self.table.get_item(Key={"id": user_id})


def build_session():
    session = boto3.Session(region_name="ap-northeast-1")  # PW003
    return session


def build_clients(session):
    sqs = session.client("sqs")       # PW001
    sns = session.client("sns")       # PW001
    return sqs, sns


def send_notification(topic_arn, message):
    session = build_session()
    _, sns = build_clients(session)
    sns.publish(TopicArn=topic_arn, Message=message)


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
