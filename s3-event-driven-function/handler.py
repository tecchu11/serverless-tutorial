import boto3
import os
import urllib.parse

hello = os.environ['HELLO']
world = os.environ['WORLD']
s3 = boto3.client('s3')


def execute(event, context):
    bucket = event['Records'][0]['s3']['bucket']['name']
    key = urllib.parse.unquote_plus(event['Records'][0]['s3']['object']['key'], encoding='utf-8')

    print("Bucket:{} Key:{}".format(bucket, key))
    print("Environment variables: {} {}".format(hello, world))
