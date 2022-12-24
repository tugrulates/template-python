"""Unittests for the CLI."""


from pathlib import Path

import pytest
from typer.testing import CliRunner

from my_cli import cli

runner = CliRunner()


@pytest.fixture
def config(tmp_path: Path) -> cli.Config:
    """Fixture for config."""
    return cli.config


def test_bare() -> None:
    """Test invocation with no arguments."""
    result = runner.invoke(cli.app)
    assert result.exit_code != 0
    assert "Usage:" in result.stdout


def test_help() -> None:
    """Test help."""
    result = runner.invoke(cli.app, ["--help"])
    assert result.exit_code == 0
    assert "Usage:" in result.stdout


def test_zoo():
    """Test Zoolander quote."""
    result = runner.invoke(cli.app, ["zoo"])
    assert result.exit_code == 0
    assert len(result.stdout.strip().split("\n")) == 1


def test_zoo_favorite():
    """Test Zoolander quote."""
    result = runner.invoke(cli.app, ["zoo", "--favorite=break-dance"])
    assert result.exit_code == 0
    assert result.stdout.strip() == "They're break-dance fighting."
