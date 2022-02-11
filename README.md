# S3 event driven function with serverless framework(pyton)

[![CI](https://github.com/tecchu11/s3-event-driven-function/actions/workflows/ci.yml/badge.svg)](https://github.com/tecchu11/s3-event-driven-function/actions/workflows/ci.yml)

## Get Started

### Installation

- Install node.js and python via asdf: `asdf install`
- After install node, globally install serverless via npm: `npm install -g serverless`

### How to invoke on local env with test event json

- `sls invoke local -f event-handler-function -p test/event.json`
