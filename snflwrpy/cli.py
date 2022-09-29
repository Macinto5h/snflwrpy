"""
This module has the command line interface for snflwrpy that allows a user to
run the app with various options.
"""
import argparse
from curses import wrapper
from snflwrpy import __app_version__, __app_description__
from snflwrpy.sort_type import SortType
from snflwrpy.visualizer import visualizer_start

def cli():
    """Command line interface to run the snflwrpy application."""

    parser = argparse.ArgumentParser(description=__app_description__)
    parser.add_argument('-a', '--algorithm', choices=SortType.get_values(), dest='algorithm', default=SortType.INSERTION.value)
    parser.add_argument('-f', '--floret-count', type=int, dest='floret_count', default=50)
    parser.add_argument('-v', '--version', action='version', version=__app_version__)

    args = parser.parse_args()

    wrapper(visualizer_start, args)

if __name__ == "__main__":
    cli()
