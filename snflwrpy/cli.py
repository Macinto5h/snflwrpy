"""
This module has the command line interface for snflwrpy that allows a user to
run the app with various options.
"""
import argparse
from snflwrpy import __version__
from snflwrpy import __description__
from snflwrpy.sort_type import SortType
from snflwrpy.main import Application

def cli():
    """Command line interface to run the snflwrpy application."""

    parser = argparse.ArgumentParser(description=__description__)
    parser.add_argument('-a', '--algorithm', choices=SortType.get_values(), dest='algorithm')
    parser.add_argument('-v', '--version', action='version', version=__version__)

    args = parser.parse_args()

    Application().start(args.algorithm)

if __name__ == "__main__":
    cli()
