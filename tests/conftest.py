import pytest
import functools
import helpers


@pytest.fixture()
def run_myapp(tmp_path):
    ret = functools.partial(helpers.run, "myapp")
    return ret


@pytest.fixture()
def create_file(tmp_path):
    files_dir = tmp_path / "files"
    return functools.partial(helpers.create_file, files_dir)
