"""
This module has the command line interface for vogel sorter that allows a user to
run the app with various options.
"""
import argparse
from snflwr import __version__
from snflwr import __description__
from snflwr.sort_type import SortType
from snflwr.main import Application

def cli():
    """Command line interface to run the vogel_sorter application."""

    parser = argparse.ArgumentParser(description=__description__)
    parser.add_argument('-a', '--algorithm', choices=SortType.get_values(), dest='algorithm')
    parser.add_argument('-v', '--version', action='version', version=__version__)

    args = parser.parse_args()

    Application().start(args.algorithm)

if __name__ == "__main__":
    cli()
