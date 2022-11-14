"""
Test suite for sort_type module.
"""
from snflwrpy.sort_type import SortType

def test_sort_type_returns_list_of_all_values_when_called():
    """Test sort type returns list of all values when called"""

    expected_list = [
        SortType.BOGO.value,
        SortType.BUBBLE.value,
        SortType.COCKTAIL.value,
        SortType.GNOME.value,
        SortType.INSERTION.value,
        SortType.RADIX_LSD.value,
        SortType.SELECTION.value,
        SortType.STOOGE.value
    ]

    assert SortType.get_values() == expected_list
