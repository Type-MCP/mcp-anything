"""A fake Click CLI app for testing."""
import click


@click.group()
def cli():
    """A sample CLI tool."""
    pass


@cli.command()
@click.argument("url")
@click.option("--output", "-o", type=str, default="output.json", help="Output file path")
@click.option("--timeout", type=int, default=30, help="Request timeout in seconds")
@click.option("--verbose/--no-verbose", default=False, help="Enable verbose output")
def fetch(url, output, timeout, verbose):
    """Fetch data from a URL."""
    pass


@cli.command()
@click.argument("path")
@click.option(
    "--format",
    "fmt",
    type=click.Choice(["json", "csv", "xml"]),
    default="json",
    help="Output format",
)
def convert(path, fmt):
    """Convert a file to a different format."""
    pass


if __name__ == "__main__":
    cli()
