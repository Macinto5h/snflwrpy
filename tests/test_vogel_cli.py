from vogel_sorter import __version__
from vogel_sorter.vogel_cli import VogelCLI
from vogel_sorter.sort_type import SortType
from vogel_sorter.main import Application

def test_vogel_cli_returns_app_version_when_prompted():
    cli = VogelCLI()
    received_version = cli.getAppVersion()
    assert received_version == __version__

def test_vogel_cli_returns_list_of_valid_algorithms_when_prompted():
    cli = VogelCLI()
    received_list = cli.getAvailableAlgorithms()
    assert received_list == SortType.getValues()

def test_vogel_cli_returns_app_with_given_arguments(mocker):
    cli = VogelCLI()
    parsed_args = ParsedArgsObject()
    parsed_args.algorithm = 'insertion'

    mocker.patch.object(Application, 'start')

    cli.startAppWithArgs(parsed_args)

    Application.start.assert_called_once_with(parsed_args.algorithm)

class ParsedArgsObject():
    algorithm = ''
