"""Notification service using SNS."""
from utils.session import build_clients, build_session


def send_notification(topic_arn, message):
    session = build_session()
    _, sns = build_clients(session)
    sns.publish(TopicArn=topic_arn, Message=message)
