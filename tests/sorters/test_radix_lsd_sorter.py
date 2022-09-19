"""Test suite for radix_lsd_sorter module"""
from snflwr.sorters.radix_lsd_sorter import RadixLSDSorter
from snflwr.sorters.sort_change import SortChange
from chancepy import Chance

def test_radix_lsd_sorter_is_sorted_after_iterating_list_length_times_digit_length():
    """Test radix lsd sorter is sorted after iterating next n squared times"""

    unsorted_array = []
    list_length = Chance.integer(2, 20)
    digit_length = 3

    for i in range(list_length):
        unsorted_array.append(Chance.integer(100, 999))

    sorter = RadixLSDSorter(unsorted_array)

    for i in range(list_length ** digit_length):
        sorter.next()

    assert sorter.is_sorted()
