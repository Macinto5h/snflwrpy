"""Test suite for insertion_sorter module"""
from snflwrpy.sorters.insertion_sorter import InsertionSorter
from chancepy import Chance

def test_insertion_sorter_is_sorted_after_iterating_best_case_scenario():
    """Test insertion sorter is sorted after iterating best case scenario"""

    sorted_array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    list_length = len(sorted_array)
    sorter = InsertionSorter(sorted_array)

    for i in range(list_length):
        sorter.next()

    assert sorter.is_sorted()

def test_insertion_sorter_is_sorted_after_iterating_next_n_squared_times():
    """Test insertion sorter is sorted after iterating next n squared times"""

    unsorted_array = []
    list_length = Chance.integer(2, 20)
    for i in range(list_length):
        unsorted_array.append(Chance.integer(0, 100))

    sorter = InsertionSorter(unsorted_array)

    for i in range(list_length ** 2):
        sorter.next()

    assert sorter.is_sorted()
