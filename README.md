# S3 event driven function with serverless framework(pyton)

## Get Started

### Installation

- Install node.js and python via asdf: `asdf install`
- After install node, globally install serverless via npm: `npm install -g serverless`

### How to invoke on local env with test event json

- `sls invoke local -f event-handler-function -p test/event.json`
