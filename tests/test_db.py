import time

from src import lib


def test_hello(tmp_path):
    db_path = tmp_path / "sqlite.db"
    db = lib.load_db(db_path)

    db['hello'] = 'world'
    assert db['hello'] == 'world'

    db['hello'] = 'mundo'
    assert db['hello'] == 'mundo'

    del db['hello']
    try:
        db['hello']
        assert False
    except KeyError:
        pass

    a_list = [1, 2, 3, 4]
    db['list'] = a_list
    a_dict = dict(a=1, b=2, c="hello")
    db['dict'] = a_dict
    del db
    db = lib.load_db(tmp_path / "sqlite.db")
    assert db['list'] == a_list
    assert db['dict'] == a_dict

    bigdata = "hello" * 1_000_000
    db['big'] = bigdata
    del db

    db = lib.load_db(tmp_path / "sqlite.db")
    assert db_path.stat().st_size > len(bigdata)

    del db['big']
    db.vacuum()
    time.sleep(0.1)  # wait for vacuum to finish
    assert db_path.stat().st_size < 100_000
