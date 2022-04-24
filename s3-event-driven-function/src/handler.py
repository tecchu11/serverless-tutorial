import os

from aws_lambda_powertools.logging import Logger
from aws_lambda_powertools.utilities.data_classes import S3Event
from aws_lambda_powertools.utilities.typing import LambdaContext

env_name = os.environ["ENV_NAME"]
logger = Logger(service="s3-event-driven-function")


def execute(event: S3Event, context: LambdaContext) -> None:
    bucket_name = event.bucket_name
    key_name = event.record.s3.get_object.key
    logger.info(
        f"Bucket name {bucket_name} and Object key name {key_name} are parsed by event."
    )
    logger.info(f"Env is  {env_name}")
