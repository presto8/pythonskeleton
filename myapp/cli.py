#!/usr/bin/env python3

from dataclasses import dataclass
from myapp import lib
import click


@dataclass
class AppContext:
    data: str
    configdir: str


pass_app = click.make_pass_decorator(AppContext)


@click.group()
@click.option('--verbose/--no-verbose', default=False)
@click.option('--config', type=str, default=None, envvar='MYAPP_CONFIG')
@click.pass_context
def cli(ctx, verbose, config):
    app = AppContext(
        configdir=lib.resolve_configdir(config),
        data="some data",
    )
    ctx.obj = app

    click.echo('I am about to invoke %s' % ctx.invoked_subcommand)


@cli.command()
@pass_app
def hello(app):
    hello = lib.do_hello()
    click.echo(hello)
    click.echo(f'global data = {app.data}')


if __name__ == '__main__':
    cli()
