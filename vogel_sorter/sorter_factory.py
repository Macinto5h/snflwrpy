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
from vogel_sorter.sort_type import SortType

class SorterFactory():
    def get_sorter(self, sorter_name):
        if (sorter_name == SortType.BUBBLE.value):
            return BubbleSorter()
        elif (sorter_name == SortType.COCKTAIL.value):
            return CocktailSorter()
        elif (sorter_name == SortType.GNOME.value):
            return GnomeSorter()
        elif (sorter_name == SortType.INSERTION.value):
            return InsertionSorter()
        elif (sorter_name == SortType.MERGE.value):
            return MergeSorter()
        elif (sorter_name == SortType.RADIX_LSD.value):
            return RadixLSDSorter()
        elif (sorter_name == SortType.SELECTION.value):
            return SelectionSorter()
        elif (sorter_name == SortType.SHELL.value):
            return ShellSorter()
        elif (sorter_name == SortType.STOOGE.value):
            return StoogeSorter()

        return Sorter()
