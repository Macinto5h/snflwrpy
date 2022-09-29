"""
Test suite for the bubble_sorter module.
"""
from snflwrpy.sorters.bogo_sorter import BogoSorter
from chancepy import Chance

def test_bogo_sorter_is_sorted_after_iterating_best_case_scenario():
    """Test bubble sorter is sorted after iterating best case scenario"""

    sorted_array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    sorter = BogoSorter(sorted_array)

    assert sorter.is_sorted()
