"""
Module provides sorter_factory function used to return a Sorter object
based on the string name provided.
"""
from snflwrpy.sorters.bubble_sorter import BubbleSorter
from snflwrpy.sorters.cocktail_sorter import CocktailSorter
from snflwrpy.sorters.gnome_sorter import GnomeSorter
from snflwrpy.sorters.insertion_sorter import InsertionSorter
from snflwrpy.sorters.radix_lsd_sorter import RadixLSDSorter
from snflwrpy.sort_type import SortType

def sorter_factory(sorter_name, unsorted_array):
    """Returns a sorter based on the name provided."""

    sorter = BubbleSorter(unsorted_array)

    if sorter_name == SortType.COCKTAIL.value:
        sorter = CocktailSorter(unsorted_array)
    elif sorter_name == SortType.GNOME.value:
        sorter = GnomeSorter(unsorted_array)
    elif sorter_name == SortType.INSERTION.value:
        sorter = InsertionSorter(unsorted_array)
    elif sorter_name == SortType.RADIX_LSD.value:
        sorter = RadixLSDSorter(unsorted_array)

    return sorter