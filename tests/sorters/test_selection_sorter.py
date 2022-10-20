"""Test suite for selection_sorter module"""
from snflwrpy.sorters.selection_sorter import SelectionSorter
from chancepy import Chance

def test_selection_sorter_is_sorted_after_iterating_best_case_scenario():
    """Test selection sorter is sorted after iterating best case scenario"""

    sorted_array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    list_length = len(sorted_array)
    sorter = SelectionSorter(sorted_array)

    for i in range(list_length ** 2):
        sorter.next()

    assert sorter.is_sorted()

def test_selection_sorter_is_sorted_after_iterating_next_n_squared_times():
    """Test selection sorter is sorted after iterating next n squared times"""

    unsorted_array = []
    list_length = Chance.integer(2, 20)
    for i in range(list_length):
        unsorted_array.append(Chance.integer(0, 100))

    sorter = SelectionSorter(unsorted_array)

    for i in range(list_length ** 2):
        sorter.next()

    assert sorter.is_sorted()