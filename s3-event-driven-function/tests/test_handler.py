import json
import os
from unittest import mock

from src.handler import parse_event


@mock.patch.dict(os.environ, {"ENV_NAME": "DEV"}, clear=True)
def test_parse_event():
    event_json = json.load(open('./event.json', 'r'))
    bucket, key = parse_event(event_json)

    assert bucket == "testEventBucket"
    assert key == "HelloWorld.txt"
