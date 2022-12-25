"""Help message for my CLI app. Change this."""


import logging
import random
from pathlib import Path
from typing import Optional

import typer

from my_cli.config import Config

APP_NAME = "my-cli"  # change this


# Persistent user config
config = Config(Path(typer.get_app_dir(APP_NAME)) / "config.json")
config.load()

# App object enclosing the commands.
app = typer.Typer(help=__doc__)

# An option that sync its values to the config file.
# $ my-cli --favorite=hansel  # write 'favorite=value' to config file
# $ my-cli                    # reuse from config file
# $ my-cli --favorite=        # reset favorite
FavoriteOption = config.option("favorite", help="Favorite quote.")


@app.command()
def quote(favorite: Optional[str] = FavoriteOption) -> None:
    """Print a random quote from Zoolander."""
    # Static files will be in site-packages next to this file.
    quotes_path = Path(__file__).parent / "static" / "my_quotes.txt"
    quotes = quotes_path.read_text(encoding="utf-8").strip().split("\n")

    # Filter quotes using the favorite filter.
    if favorite:
        logging.warning("favorite")
        quotes = [x for x in quotes if favorite.lower() in x.lower()]

    # Random number generators in the standard library are not suitable for security.
    # Drop the 'nosec' below and run 'hatch run lint:lint' to see lint checks in action.
    print(random.choice(quotes or ["You've done nothing! NOTHIIIING!"]))  # nosec


if __name__ == "__main__":
    app()
