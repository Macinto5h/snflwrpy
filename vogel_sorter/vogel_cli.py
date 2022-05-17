import argparse
from vogel_sorter import __version__
from vogel_sorter import __description__
from vogel_sorter.sort_type import SortType
from vogel_sorter.main import Application

class VogelCLI():
    def parse_arguments(self):
        parser = argparse.ArgumentParser(description=__description__)
        parser.add_argument('-a', '--algorithm', choices=self.get_available_algorithms(), dest='algorithm')
        parser.add_argument('-v', '--version', action='version', version=self.get_app_version())

        args = parser.parse_args()

        self.start_app_with_args(args)

    def get_app_version(self):
        return __version__

    def get_available_algorithms(self):
        return SortType.get_values()

    def start_app_with_args(self, args):
        app = Application()
        app.start(args.algorithm)

if __name__ == "__main__":
    VogelCLI().parse_arguments()
