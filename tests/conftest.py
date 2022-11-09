import pytest
import functools
import helpers
from src.cli import APPNAME


@pytest.fixture()
def run_myapp(tmp_path):
    ret = functools.partial(helpers.run, APPNAME)
    return ret


@pytest.fixture()
def create_file(tmp_path):
    files_dir = tmp_path / "files"
    return functools.partial(helpers.create_file, files_dir)
