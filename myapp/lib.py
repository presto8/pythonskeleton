"""Code in this file should be unit-testable."""

from typing import List, Union
import os
import toml
import sqlitedict


def resolve_configdir(cli_arg=Union[None, str]) -> str:
    if cli_arg:
        path = cli_arg
    elif 'XDG_CONFIG_HOME' in os.environ:
        path = os.path.join(os.environ['XDG_CONFIG_HOME'], 'myapp')
    else:
        path = os.path.join(os.environ['HOME'], '.config', 'myapp')
    return os.path.abspath(path)


def load_config(configpath):
    try:
        cfg = toml.load(configpath)
    except FileNotFoundError:
        print(f'config file "{configpath}" does not exist, using defaults...')
        cfg = dict(a_string="FIXME", a_number=42)
        print(toml.dumps(cfg))
    return cfg


class Db(sqlitedict.SqliteDict):
    def vacuum(self):
        self.conn.execute('vacuum')


def load_db(dbpath):
    return Db(dbpath, autocommit=True)


def do_hello():
    return "hello, world!"
