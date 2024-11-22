import click


@click.group()
@click.version_option()
def cli():
    "This is a playground to learn about creating Python application using Click library."


@cli.command(name="command")
@click.argument(
    "example"
)
@click.option(
    "-o",
    "--option",
    help="An example option",
)
def first_command(example, option):
    "Command description goes here"
    click.echo("Here is some output")
