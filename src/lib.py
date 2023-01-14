"""Code in this file should be unit-testable."""

from typing import Union
import os
import json
import sqlite3
import sqlitedict
import zlib


class Db(sqlitedict.SqliteDict):
    dbpath: str
    compress: bool = False

    def __post_init__(self):
        self.dict = sqlitedict.SqliteDict(self.dbpath, encode=self._my_encode, decode=self._my_decode)

    def _my_encode(self, obj):
        result = json.dumps(obj)
        if self.compress:
            result = sqlite3.Binary(zlib.compress(result))
        return result

    def _my_decode(self, obj):
        if self.compress:
            result = zlib.decompress(bytes(obj))
        else:
            result = obj
        return json.loads(result)

    def vacuum(self):
        self.conn.execute('vacuum')


def load_db(dbpath):
    return Db(dbpath, autocommit=True)


def do_hello():
    return "hello, world!"
