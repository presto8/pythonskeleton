#!/usr/bin/env python3

from dataclasses import dataclass
from myapp import lib
import click


@dataclass
class AppContext:
    data: str


pass_app = click.make_pass_decorator(AppContext)


@click.group()
@click.option('--verbose/--no-verbose', default=False)
@click.pass_context
def cli(ctx, verbose):
    click.echo('I am about to invoke %s' % ctx.invoked_subcommand)
    ctx.obj = AppContext(data="some data")


@cli.command()
@pass_app
def hello(app):
    click.echo(lib.do_hello())
    click.echo(f'global data = {app.data}')


if __name__ == '__main__':
    cli()
