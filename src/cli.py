import argparse
import inspect
import os
import signal
import sys
from dataclasses import dataclass
from src import lib
from src import work


APPNAME = "paddr"

HELP = f"""
{APPNAME} by Preston Hunt <me@prestonhunt.com>
https://github.com/presto8/pythonskeleton

A starting point for Python scripts.
"""


def parse_args(argv):
    configenv = f'{APPNAME.upper()}_DIR'
    default_command = "hello"

    parser = argparse.ArgumentParser(description=HELP, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument('--configdir', default=os.environ.get(configenv), help=f'location of config files (default: ${configenv}, $XDG_CONFIG_HOME/{APPNAME}, ~/.config/{APPNAME})')
    parser.add_argument('--verbose', default=False, action='store_true', help='show more detailed messages')
    parser.add_argument('--debug', action='store_true', help='print as much information as possible')
    parser.add_argument('--quiet', action='store_true', help='print as little output as possible, only error messages')

    commands = []
    subparsers = parser.add_subparsers(dest='command')

    def add_command(name, *args, **kwargs):
        commands.append(name)
        return subparsers.add_parser(name, *args, **kwargs)

    x = add_command('hello', help='simple command')
    x.add_argument('--esp', action='store_true', help='output in Spanish')

    # check for default command
    if default_command and argv and argv[0] not in commands:
        argv.insert(0, default_command)

    args, unknown_args = parser.parse_known_args(argv)
    args.unknown_args = unknown_args

    if args.command is None:
        parser.print_help()
        raise SystemExit(1)

    return args


def cli_mapper(args):
    func = getattr(work, args.command.replace("-", "_"))
    sig = inspect.signature(func)
    func_args = sig.parameters.keys()
    missing_args = [arg for arg in func_args if arg not in arg]
    if missing_args:
        raise Fail(f"missing arguments for {func}: {missing_args}")  # pragma: no cover
    pass_args = {k: v for k, v in args.__dict__.items() if k in func_args}
    if 'pathspec' in pass_args.keys():
        pass_args['pathspec'] = [Path(path) for path in pass_args['pathspec']]
    return func(**pass_args)


def main(argv):
    args = parse_args(argv)
    args.work = work.Work(appname=APPNAME, configdir=args.configdir)
    cli_mapper(args)


class Fail(Exception):
    pass


class SigtermInterrupt(Exception):
    pass


def register_sigterm():
    def exit_gracefully(*args):
        raise SigtermInterrupt()
    signal.signal(signal.SIGINT, exit_gracefully)
    signal.signal(signal.SIGTERM, exit_gracefully)


def entrypoint():  # pragma: no cover
    try:
        register_sigterm()
        main(sys.argv[1:])
    except Fail as f:
        print(*f.args, file=sys.stderr)
        sys.exit(1)
    except SigtermInterrupt:
        print("received interrrupt or terminate signal")
    except KeyboardInterrupt:
        print("Ctrl+C")
