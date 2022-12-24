"""Unittests for the CLI."""


from pathlib import Path

import pytest
from typer.testing import CliRunner

from my_cli import cli

runner = CliRunner()


@pytest.fixture
def config(tmp_path: Path) -> cli.Config:
    """Fixture for config."""
    cli.config.PATH = tmp_path / "config.json"
    return cli.config


def test_bare(config: cli.Config) -> None:
    """Test invocation with no arguments."""
    config.dump()
    result = runner.invoke(cli.app)
    assert result.exit_code != 0
    assert "Usage:" in result.stdout


def test_help(config: cli.Config) -> None:
    """Test help."""
    config.dump()
    result = runner.invoke(cli.app, ["--help"])
    assert result.exit_code == 0
    assert "Usage:" in result.stdout


def test_zoo(config: cli.Config):
    """Test Zoolander quote."""
    config.dump()
    result = runner.invoke(cli.app, ["zoo"])
    assert result.exit_code == 0
    assert len(result.stdout.strip().split("\n")) == 1


def test_zoo_favorite(config: cli.Config):
    """Test Zoolander quote."""
    config.dump()
    result = runner.invoke(cli.app, ["zoo", "--favorite=break-dance"])
    assert result.exit_code == 0
    assert result.stdout.strip() == "They're break-dance fighting."
    result = runner.invoke(cli.app, ["zoo"])
    assert result.exit_code == 0
    assert result.stdout.strip() == "They're break-dance fighting."
