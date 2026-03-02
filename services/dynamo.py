"""DynamoDB service wrapper."""
import boto3


class DynamoService:
    def __init__(self):
        self.table = boto3.resource("dynamodb").Table("users")  # PW002

    def get_user(self, user_id):
        return self.table.get_item(Key={"id": user_id})

    def put_user(self, user):
        self.table.put_item(Item=user)
