"""Persistent user configuration."""


import json
import logging
from pathlib import Path
from typing import Any, Dict

import typer


class Config:
    """
    Persistent config in app folder.

    A global object of this class will maintain user preferences to persist across
    invocations. See below for how to read and write to this configuration.
    """

    def __init__(self, path: Path) -> None:
        """Set up a new config for the given config file path."""
        self.path = path
        self.prefs: Dict[str, Any] = {}

    def load(self) -> None:
        """Read config from config file."""
        if self.path.is_file():
            prefs = dict(json.loads(self.path.read_text(encoding="utf-8")))
            self.prefs = {k: prefs[k] for k in prefs if isinstance(k, str)}

    def dump(self) -> None:
        """Write config back to config file."""
        self.path.parent.mkdir(parents=True, exist_ok=True)
        self.path.write_text(json.dumps(self.prefs), encoding="utf-8")

    def option(self, name: str, **kwargs) -> Any:
        """Return an option info for an option that sync with the config file."""

        def callback(ctx: typer.Context, value: Any):
            if ctx.resilient_parsing:
                return None
            if value is not None:
                logging.warning("dumping %s %s", value, name)
                self.prefs[name] = value
                self.dump()
            return value

        return typer.Option(lambda: self.prefs.get(name), callback=callback, **kwargs)
