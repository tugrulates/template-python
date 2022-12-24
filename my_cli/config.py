"""Persistent user configuration."""


import dataclasses
import json
from dataclasses import dataclass
from pathlib import Path

import typer

APP_NAME = "my-cli"  # change this
CONFIG_PATH = Path(typer.get_app_dir(APP_NAME)) / "config.json"


@dataclass
class Config:
    """
    Persistent config in app folder.

    A global object of this class will maintain user preferences to persist across
    invocations. See below for how to read and write to this configuration.
    """

    favorite: str = ""
    # add more serializable config values here

    def load(self):
        """Read config from config file."""
        if CONFIG_PATH.is_file():
            self.__init__(**dict(json.loads(CONFIG_PATH.read_text(encoding="utf-8"))))

    def dump(self, **kwargs):
        """Write config back to config file."""
        self.__init__(**kwargs)
        CONFIG_PATH.parent.mkdir(parents=True, exist_ok=True)
        CONFIG_PATH.write_text(json.dumps(dataclasses.asdict(self)), encoding="utf-8")
