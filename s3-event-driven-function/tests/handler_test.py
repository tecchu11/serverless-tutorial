import json
import os
from unittest import mock

from src.handler import execute


@mock.patch.dict(os.environ, {"ENV_NAME": "DEV"}, clear=True)
def test_parse_event():
    event_json = json.load(open("./event.json", "r"))

