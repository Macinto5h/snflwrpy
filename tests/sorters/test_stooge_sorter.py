"""Test suite for stooge_sorter module"""
from chancepy import Chance
from snflwrpy.sorters.stooge_sorter import StoogeSorter
import math

def test_stooge_sorter_is_sorted_after_iterating_worst_case_scenario():
    """Test stooge sorter is sorted after iterating worst case scenario"""

    unsorted_array = []
    list_length = Chance.integer(2, 20)
    for i in range(list_length):
        unsorted_array.append(Chance.integer(0, 100))

    sorter = StoogeSorter(unsorted_array)
    stooge_sort_worst_case_time_complexity = (list_length ** 2.7095) + 1
    for i in range(math.ceil(stooge_sort_worst_case_time_complexity)):
        sorter.next()

    assert sorter.is_sorted()
