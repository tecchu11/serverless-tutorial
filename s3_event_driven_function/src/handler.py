import os

import boto3
from aws_lambda_powertools.logging import Logger
from aws_lambda_powertools.utilities.data_classes import S3Event, event_source
from aws_lambda_powertools.utilities.typing import LambdaContext

s3_resource = boto3.resource(service_name="s3", endpoint_url="http://localhost:4566/")
env_name = os.environ["ENV_NAME"]
logger = Logger()


@event_source(data_class=S3Event)
@logger.inject_lambda_context(log_event=True)
def execute(event: S3Event, context: LambdaContext) -> None:
    bucket_name = event.bucket_name
    key_name = event.record.s3.get_object.key
    logger.info(
        f"Bucket name {bucket_name} and Object key name {key_name} are parsed by event."
    )
    logger.info(f"Env is  {env_name}")


def print_object_content(bucket_name: str, object_key_name: str) -> None:
    object_content = (
        s3_resource.Bucket(bucket_name)
        .Object(object_key_name)
        .get()["Body"]
        .read()
        .decode("utf-8")
    )
    logger.info(f"s3://{bucket_name}//{object_key_name} content is {object_content}")
