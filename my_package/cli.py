"""CLI code for the package can live here."""


import random
from typing import Optional

import typer

from my_package import get_quotes

# App object enclosing the commands.
app = typer.Typer(help=__doc__)


@app.command()
def quote(favorite: Optional[str] = None) -> None:
    """Print a random quote from Zoolander."""
    quotes = get_quotes()

    # Filter quotes using the favorite filter.
    if favorite:
        quotes = [x for x in quotes if favorite.lower() in x.lower()]

    # Random number generators in the standard library are not suitable for security.
    # Drop the 'nosec' below and run 'hatch run lint:lint' to see lint checks in action.
    print(random.choice(quotes or ["You've done nothing! NOTHIIIING!"]))  # nosec


if __name__ == "__main__":
    app()
