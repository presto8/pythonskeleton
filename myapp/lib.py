"""Code in this file should be unit-testable."""

from typing import List, Union
import os


def resolve_configdir(cli_arg=Union[None, str]) -> str:
    if cli_arg:
        path = cli_arg
    elif 'XDG_CONFIG_HOME' in os.environ:
        path = os.path.join(os.environ['XDG_CONFIG_HOME'], 'myapp')
    else:
        path = os.path.join(os.environ['HOME'], '.config', 'myapp')
    return os.path.abspath(path)


def do_hello():
    return "hello, world!"
