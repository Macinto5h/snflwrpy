"""
Test suite for cli module.
"""
from snflwr import __version__
from snflwr.cli import cli
from snflwr.main import Application

def test_vogel_cli_returns_app_with_given_arguments(mocker):
    """Test vogel cli returns app with given arguments"""

    mocker.patch.object(Application, 'start')

    cli()

    Application.start.assert_called_once()
