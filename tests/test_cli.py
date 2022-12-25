"""Unittests for the CLI."""


from pathlib import Path

import pytest
from typer.testing import CliRunner

from my_cli import cli

runner = CliRunner()


@pytest.fixture
def config(tmp_path: Path) -> cli.Config:
    """Fixture for config."""
    cli.config = cli.Config(tmp_path / "config.json")
    cli.config.dump()
    return cli.config


def test_help(config: cli.Config) -> None:
    """Test help."""
    config.load()
    result = runner.invoke(cli.app, ["--help"])
    assert result.exit_code == 0
    assert "Usage:" in result.stdout


def test_quote(config: cli.Config):
    """Test Zoolander quote."""
    config.load()
    result = runner.invoke(cli.app)
    assert result.exit_code == 0
    assert len(result.stdout.strip().split("\n")) == 1


def test_favorite_quote(config: cli.Config):
    """Test Zoolander quote."""
    config.load()
    print(config.path)
    result = runner.invoke(cli.app, ["--favorite=break-dance"])
    print(config.prefs)
    assert result.exit_code == 0
    assert result.stdout.strip() == "They're break-dance fighting."
    print(config.path)
    print(config.prefs)
    result = runner.invoke(cli.app)
    assert result.exit_code == 0
    assert result.stdout.strip() == "They're break-dance fighting."


def test_favorite_quote_missing(config: cli.Config):
    """Test Zoolander quote."""
    config.load()
    result = runner.invoke(cli.app, ["--favorite=derek"])
    assert result.exit_code == 0
    assert result.stdout.strip() == "You've done nothing! NOTHIIIING!"
