# Lambda function implemented serverless framework with python

[![CI](https://github.com/tecchu11/s3-event-driven-function/actions/workflows/ci.yml/badge.svg)](https://github.com/tecchu11/s3-event-driven-function/actions/workflows/ci.yml)

This is serverless framework tutorial.

## Get Started

### Installation

Install node.js and python via asdf: `asdf install`.After install node, globally install serverless via
npm: `npm install -g serverless`.

Second, install pipenv via pi: `pip install pipenv`. And then all dependencies: `pipenv sync --dev`.

### How to invoke on local env with test event json

You can invoke lambda function locally, `sls invoke local -f {function_name} -p path/to/test-event.json`.

For instance

```
cd s3-event-driven-function
sls invoke local -f event-driven-function -p tests/event.json
```

For more sls info, run `sls` with `--help` option.
