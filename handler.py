import os

_hello = os.environ['HELLO']
_world = os.environ['WORLD']


def hello(event, context):
    print("{} {}".format(_hello, _world))
