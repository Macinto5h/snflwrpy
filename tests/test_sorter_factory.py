from vogel_sorter.sorter_factory import SorterFactory
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

def test_sorter_factory_returns_default_when_given_invalid_name():
    received_sorter = SorterFactory().get_sorter('')
    assert isinstance(received_sorter, Sorter)

def test_sorter_factory_returns_bubble_sorter_when_requested():
    sorter_name = BUBBLE_SORTER_NAME
    received_sorter = SorterFactory().get_sorter(sorter_name)
    assert isinstance(received_sorter, BubbleSorter)

def test_sorter_factory_returns_cocktail_sorter_when_requested():
    sorter_name = COCKTAIL_SORTER_NAME
    received_sorter = SorterFactory().get_sorter(sorter_name)
    assert isinstance(received_sorter, CocktailSorter)

def test_sorter_factory_returns_gnome_sorter_when_requested():
    sorter_name = GNOME_SORTER_NAME
    received_sorter = SorterFactory().get_sorter(sorter_name)
    assert isinstance(received_sorter, GnomeSorter)

def test_sorter_factory_returns_insertion_sorter_when_requested():
    sorter_name = INSERTION_SORTER_NAME
    received_sorter = SorterFactory().get_sorter(sorter_name)
    assert isinstance(received_sorter, InsertionSorter)

def test_sorter_factory_returns_merge_sorter_when_requested():
    sorter_name = MERGE_SORTER_NAME
    received_sorter = SorterFactory().get_sorter(sorter_name)
    assert isinstance(received_sorter, MergeSorter)

def test_sorter_factory_returns_radix_lsd_sorter_when_requested():
    sorter_name = RADIX_LSD_SORTER_NAME
    received_sorter = SorterFactory().get_sorter(sorter_name)
    assert isinstance(received_sorter, RadixLSDSorter)

def test_sorter_factory_returns_selection_sorter_when_requested():
    sorter_name = SELECTION_SORTER_NAME
    received_sorter = SorterFactory().get_sorter(sorter_name)
    assert isinstance(received_sorter, SelectionSorter)

def test_sorter_factory_returns_shell_sorter_when_requested():
    sorter_name = SHELL_SORTER_NAME
    received_sorter = SorterFactory().get_sorter(sorter_name)
    assert isinstance(received_sorter, ShellSorter)

def test_sorter_factory_returns_stooge_sorter_when_requested():
    sorter_name = STOOGE_SORTER_NAME
    received_sorter = SorterFactory().get_sorter(sorter_name)
    assert isinstance(received_sorter, StoogeSorter)
