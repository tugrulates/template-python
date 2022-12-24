"""Help message for my CLI app. Change this."""


import random
from pathlib import Path
from typing import Optional

import typer

from my_cli.config import Config

# Persistent user config
config = Config()
config.load()

# Commands.
app = typer.Typer(help=__doc__)


@app.command(name="zoo")
def zoo(favorite: Optional[str] = None) -> None:
    """Print a random quote from Zoolander."""
    if favorite is not None:
        # If an option is passed, write to the config file.
        config.dump(favorite=favorite)

    quotes = [
        "It's that damn Hansel! He's so hot right now!",
        "Hansel... so hot right now... Hansel.",
        "Mugatu is so hot right now",
        "What is this? A center for ants?",
        "They're *in* the computer?",
        "They're break-dance fighting.",
    ]
    # We can read persistent options from the config file directly.
    quotes = [x for x in quotes if config.favorite.lower() in x.lower()]

    if quotes:
        print(random.choice(quotes))
    else:
        print("You've done nothing! NOTHIIIING!")


# Sub commands under 'my-cli static' invocation.
static = typer.Typer()
app.add_typer(static, name="static", help="Subcommand example.")


@static.command("list")
def static_files() -> None:
    """List static files."""
    # Static files will be in site-packages next to this file.
    static_file_folder = Path(__file__).parent / "static"
    for path in static_file_folder.iterdir():
        print(path)


@static.command("print")
def static_print() -> None:
    """List static files."""
    static_file_folder = Path(__file__).parent / "static" / "my_static_file.txt"
    print(static_file_folder.read_text(encoding="utf-8").strip())


if __name__ == "__main__":
    app()
