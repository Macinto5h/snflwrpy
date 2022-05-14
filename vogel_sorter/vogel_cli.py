import argparse
from vogel_sorter import __version__
from vogel_sorter import __description__
from vogel_sorter.sort_type import SortType
from vogel_sorter.main import Application

class VogelCLI():
    def parseArguments(self):
        parser = argparse.ArgumentParser(description=__description__)
        parser.add_argument('-a', '--algorithm', choices=self.getAvailableAlgorithms(), dest='algorithm')
        parser.add_argument('-v', '--version', action='version', version=self.getAppVersion())

        args = parser.parse_args()

        self.startAppWithArgs(args)

    def getAppVersion(self):
        return __version__

    def getAvailableAlgorithms(self):
        return SortType.getValues()

    def startAppWithArgs(self, args):
        app = Application()
        app.start(args.algorithm)

if __name__ == "__main__":
    VogelCLI().parseArguments()
