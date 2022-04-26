from vogel_sorter.sorters.sorter import Sorter
from vogel_sorter.sorters.bubble_sorter import BubbleSorter
from vogel_sorter.sorters.cocktail_sorter import CocktailSorter
from vogel_sorter.sorters.gnome_sorter import GnomeSorter
from vogel_sorter.sorters.insertion_sorter import InsertionSorter
from vogel_sorter.sorters.merge_sorter import MergeSorter
from vogel_sorter.sorters.radix_lsd_sorter import RadixLSDSorter
from vogel_sorter.sorters.selection_sorter import SelectionSorter
from vogel_sorter.sorters.shell_sorter import ShellSorter
from vogel_sorter.sorters.stooge_sorter import StoogeSorter
from vogel_sorter.sorter_names import *

class SorterFactory():
    def get_sorter(self, sorter_name):
        if (sorter_name == BUBBLE_SORTER_NAME):
            return BubbleSorter()
        elif (sorter_name == COCKTAIL_SORTER_NAME):
            return CocktailSorter()
        elif (sorter_name == GNOME_SORTER_NAME):
            return GnomeSorter()
        elif (sorter_name == INSERTION_SORTER_NAME):
            return InsertionSorter()
        elif (sorter_name == MERGE_SORTER_NAME):
            return MergeSorter()
        elif (sorter_name == RADIX_LSD_SORTER_NAME):
            return RadixLSDSorter()
        elif (sorter_name == SELECTION_SORTER_NAME):
            return SelectionSorter()
        elif (sorter_name == SHELL_SORTER_NAME):
            return ShellSorter()
        elif (sorter_name == STOOGE_SORTER_NAME):
            return StoogeSorter()

        return Sorter()
