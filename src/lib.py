"""Code in this file should be unit-testable."""

from typing import Union
import os
import sqlitedict


class Db(sqlitedict.SqliteDict):
    def vacuum(self):
        self.conn.execute('vacuum')


def load_db(dbpath):
    return Db(dbpath, autocommit=True)


def do_hello():
    return "hello, world!"
