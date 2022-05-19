"""
Test suite for vogel_cli module.
"""
from vogel_sorter import __version__
from vogel_sorter.vogel_cli import cli
from vogel_sorter.main import Application

def test_vogel_cli_returns_app_with_given_arguments(mocker):
    """Test vogel cli returns app with given arguments"""

    mocker.patch.object(Application, 'start')

    cli()

    Application.start.assert_called_once()
