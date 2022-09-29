"""
This module has the command line interface for snflwrpy that allows a user to
run the app with various options.
"""
import argparse
from snflwrpy import __app_version__, __app_description__
from snflwrpy.sort_type import SortType
from snflwrpy.visualizer import start_visualizer

def cli():
    """Command line interface to run the snflwrpy application."""

    parser = argparse.ArgumentParser(description=__app_description__)
    parser.add_argument('-a', '--algorithm', choices=SortType.get_values(), dest='algorithm')
    parser.add_argument('-v', '--version', action='version', version=__app_version__)

    args = parser.parse_args()

    start_visualizer(args.algorithm)

if __name__ == "__main__":
    cli()
