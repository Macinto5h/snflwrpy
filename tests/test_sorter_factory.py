"""
Test suite for sorter_factory module.
"""
from vogel_sorter.sorter_factory import sorter_factory
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

def test_sorter_factory_returns_default_when_given_invalid_name():
    """Test sorter factory returns default when given invalid name."""

    received_sorter = sorter_factory('')
    assert isinstance(received_sorter, Sorter)

def test_sorter_factory_returns_bubble_sorter_when_requested():
    """Test sorter factory returns bubble sorter when requested."""

    sorter_name = SortType.BUBBLE.value
    received_sorter = sorter_factory(sorter_name)
    assert isinstance(received_sorter, BubbleSorter)

def test_sorter_factory_returns_cocktail_sorter_when_requested():
    """Test sorter factory returns cocktail sorter when requested."""

    sorter_name = SortType.COCKTAIL.value
    received_sorter = sorter_factory(sorter_name)
    assert isinstance(received_sorter, CocktailSorter)

def test_sorter_factory_returns_gnome_sorter_when_requested():
    """Test sorter factory returns gnome sorter when requested."""

    sorter_name = SortType.GNOME.value
    received_sorter = sorter_factory(sorter_name)
    assert isinstance(received_sorter, GnomeSorter)

def test_sorter_factory_returns_insertion_sorter_when_requested():
    """Test sorter factory returns insertion sorter when requested."""

    sorter_name = SortType.INSERTION.value
    received_sorter = sorter_factory(sorter_name)
    assert isinstance(received_sorter, InsertionSorter)

def test_sorter_factory_returns_merge_sorter_when_requested():
    """Test sorter factory returns merge sorter when requested."""

    sorter_name = SortType.MERGE.value
    received_sorter = sorter_factory(sorter_name)
    assert isinstance(received_sorter, MergeSorter)

def test_sorter_factory_returns_radix_lsd_sorter_when_requested():
    """Test sorter factory returns radix lsd sorter when requested."""

    sorter_name = SortType.RADIX_LSD.value
    received_sorter = sorter_factory(sorter_name)
    assert isinstance(received_sorter, RadixLSDSorter)

def test_sorter_factory_returns_selection_sorter_when_requested():
    """Test sorter factory returns selection sorter when requested."""

    sorter_name = SortType.SELECTION.value
    received_sorter = sorter_factory(sorter_name)
    assert isinstance(received_sorter, SelectionSorter)

def test_sorter_factory_returns_shell_sorter_when_requested():
    """Test sorter factory returns shell sorter when requested."""

    sorter_name = SortType.SHELL.value
    received_sorter = sorter_factory(sorter_name)
    assert isinstance(received_sorter, ShellSorter)

def test_sorter_factory_returns_stooge_sorter_when_requested():
    """Test sorter factory returns stooge sorter when requested."""

    sorter_name = SortType.STOOGE.value
    received_sorter = sorter_factory(sorter_name)
    assert isinstance(received_sorter, StoogeSorter)
