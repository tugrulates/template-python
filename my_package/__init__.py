"""
My app.

Non-CLI code for the package can live here.
"""


from pathlib import Path
from typing import List


def get_quotes() -> List[str]:
    """Return the list of quotes from the static quotes file."""
    # Static files will be in site-packages next to this file.
    quotes_path = Path(__file__).parent / "static" / "my_quotes.txt"
    return quotes_path.read_text(encoding="utf-8").strip().split("\n")
