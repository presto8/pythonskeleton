import functools
import os
import toml
from pathlib import PurePath
from src import utils


class Work:
    def __init__(self, appname: str, configdir: os.PathLike):
        self.appname = appname
        self.configdir = self.resolve_configdir(configdir)
        self.datadir = self.resolve_datadir()
        self.status = utils.StatusKeeper(ephemeral_reasons="already-stored ignored")
        self.config = self.load_configfile()

    def print_helper(self, level, *args, **kwargs):
        map = {0: '..', 1: '::', 2: '::', 3: '##', 4: '!!'}
        print(map[level], *args, **kwargs)

    debug = functools.partial(print_helper, level=0)
    info = functools.partial(print_helper, level=1)
    print = functools.partial(print_helper, level=2)
    warn = functools.partial(print_helper, level=3)
    error = functools.partial(print_helper, level=4)

    def resolve_path(self, provided, envvar, default):
        if provided:
            path = provided
        elif envvar in os.environ:
            path = PurePath(os.environ[envvar], self.appname)
        else:
            path = PurePath(default, self.appname)
        os.makedirs(path, exist_ok=True)
        return os.path.abspath(path)

    def resolve_configdir(self, configdir) -> PurePath:
        default = PurePath(os.environ['HOME'], '.config')
        return self.resolve_path(configdir, 'XDG_CONFIG_HOME', default)

    def resolve_datadir(self, datadir=None) -> PurePath:
        default = PurePath(os.environ['HOME'], '.local', '.share')
        return self.resolve_path(datadir, 'XDG_DATA_HOME', default)

    def load_configfile(self) -> object:
        configfile = os.path.join(self.configdir, f"{self.appname}.toml")
        try:
            with open(configfile) as f:
                toml_dict = toml.loads(f.read())
        except FileNotFoundError:
            return {}
        return toml_dict


def hello(work):
    print("hello, world")
