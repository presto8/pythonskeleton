import pytest
import functools
import helpers


@pytest.fixture()
def run_fig(tmp_path):
    fig_dir = tmp_path / "figdir"
    ret = functools.partial(helpers.run, "fig", "--figdir", str(fig_dir))
    ret("init")
    return ret


@pytest.fixture()
def create_file(tmp_path):
    files_dir = tmp_path / "files"
    return functools.partial(helpers.create_file, files_dir)
