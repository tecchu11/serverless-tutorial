import os
import typing
import urllib.parse


def execute(event, context):
    bucket, key = parse_event(event)
    print("Bucket:{} Key:{}".format(bucket, key))


def parse_event(event) -> typing.Tuple[str, str]:
    env_name = os.environ["ENV_NAME"]
    print("Environment name is {}".format(env_name))
    bucket = event["Records"][0]["s3"]["bucket"]["name"]
    key = urllib.parse.unquote_plus(
        event["Records"][0]["s3"]["object"]["key"], encoding="utf-8"
    )
    return bucket, key
