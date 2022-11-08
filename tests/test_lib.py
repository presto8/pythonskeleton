from src import lib


def test_hello():
    output = lib.do_hello()
    assert output == "hello, world!"
