"""Unittests for the CLI."""


from pathlib import Path

import pytest
from typer.testing import CliRunner

from my_cli import cli

runner = CliRunner()


@pytest.fixture
def test_config(tmp_path: Path) -> cli.Config:
    """Fixture for config."""
    cli.config = cli.Config(tmp_path / "config.json")
    cli.config.dump()
    return cli.config


def test_help(test_config: cli.Config) -> None:
    """Test help."""
    test_config.load()
    result = runner.invoke(cli.app, ["--help"])
    assert result.exit_code == 0
    assert "Usage:" in result.stdout


def test_quote(test_config: cli.Config):
    """Test Zoolander quote."""
    test_config.load()
    result = runner.invoke(cli.app)
    assert result.exit_code == 0
    assert len(result.stdout.strip().split("\n")) == 1


def test_favorite_quote(test_config: cli.Config):
    """Test Zoolander quote."""
    test_config.load()
    print(test_config.path)
    result = runner.invoke(cli.app, ["--favorite=break-dance"])
    print(test_config.prefs)
    assert result.exit_code == 0
    assert result.stdout.strip() == "They're break-dance fighting."
    print(test_config.path)
    print(test_config.prefs)
    result = runner.invoke(cli.app)
    assert result.exit_code == 0
    assert result.stdout.strip() == "They're break-dance fighting."


def test_favorite_quote_missing(test_config: cli.Config):
    """Test Zoolander quote."""
    test_config.load()
    result = runner.invoke(cli.app, ["--favorite=derek"])
    assert result.exit_code == 0
    assert result.stdout.strip() == "You've done nothing! NOTHIIIING!"
