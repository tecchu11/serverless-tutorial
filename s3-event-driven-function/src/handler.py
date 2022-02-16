import os
import urllib.parse
import typing


def execute(event, context):
    bucket, key = parse_event(event)
    print("Bucket:{} Key:{}".format(bucket, key))


def parse_event(event) -> typing.Tuple[str, str]:
    hello = os.environ['HELLO']
    world = os.environ['WORLD']
    print("Environment variables: {} {}".format(hello, world))
    bucket = event['Records'][0]['s3']['bucket']['name']
    key = urllib.parse.unquote_plus(event['Records'][0]['s3']['object']['key'], encoding='utf-8')
    return bucket, key
