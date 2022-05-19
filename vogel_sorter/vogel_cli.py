"""
This module has the command line interface for vogel sorter that allows a user to
run the app with various options.
"""
import argparse
from vogel_sorter import __version__
from vogel_sorter import __description__
from vogel_sorter.sort_type import SortType
from vogel_sorter.main import Application

def cli():
    """Command line interface to run the vogel_sorter application."""

    parser = argparse.ArgumentParser(description=__description__)
    parser.add_argument('-a', '--algorithm', choices=SortType.get_values(), dest='algorithm')
    parser.add_argument('-v', '--version', action='version', version=__version__)

    args = parser.parse_args()

    Application().start(args.algorithm)

if __name__ == "__main__":
    cli()
