"""
Module provides sorter_factory function used to return a Sorter object
based on the string name provided.
"""
from vogel_sorter.sorters.improved_sorter import ImprovedSorter
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

def sorter_factory(sorter_name):
    """Returns a sorter based on the name provided."""

    sorter = Sorter()

    if sorter_name == SortType.COCKTAIL.value:
        sorter = CocktailSorter()
    elif sorter_name == SortType.GNOME.value:
        sorter = GnomeSorter()
    elif sorter_name == SortType.INSERTION.value:
        sorter = InsertionSorter()
    elif sorter_name == SortType.MERGE.value:
        sorter = MergeSorter()
    elif sorter_name == SortType.RADIX_LSD.value:
        sorter = RadixLSDSorter()
    elif sorter_name == SortType.SELECTION.value:
        sorter = SelectionSorter()
    elif sorter_name == SortType.SHELL.value:
        sorter = ShellSorter()
    elif sorter_name == SortType.STOOGE.value:
        sorter = StoogeSorter()

    return sorter

def improved_sorter_factory(sorter_name, unsorted_array):
    return BubbleSorter(unsorted_array)
