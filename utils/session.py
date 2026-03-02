"""Session and client factory helpers."""
import boto3


def build_session():
    return boto3.Session(region_name="ap-northeast-1")  # PW003


def build_clients(session):
    sqs = session.client("sqs")  # PW001
    sns = session.client("sns")  # PW001
    return sqs, sns
