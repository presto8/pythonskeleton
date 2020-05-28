import pytest


from myapp import lib


def test_hello():
    output = lib.do_hello()
    assert output == "hello, world!"
