"""
Test suite for the bubble_sorter module.
"""
from snflwrpy.sorters.bubble_sorter import BubbleSorter
from snflwrpy.sorters.sort_change import SortChange
from chancepy import Chance

def test_bubble_sorter_next_returns_expected_sort_change():
    """Test bubble sorter next returns expected sort changes"""

    unsorted_array = [Chance.integer(21, 40), Chance.integer(1,20)]
    sorter = BubbleSorter(unsorted_array)
    first_expected_sort_change = SortChange(index=0, old_value=unsorted_array[0], new_value=unsorted_array[1])
    second_expected_sort_change = SortChange(index=1, old_value=unsorted_array[1], new_value=unsorted_array[0])

    next_results = sorter.next()

    assert next_results[0] == first_expected_sort_change
    assert next_results[1] == second_expected_sort_change

def test_bubble_sorter_is_sorted_after_iterating_next_n_squared_times():
    """Test bubble sorter is sorted after iterating next n squared times"""

    unsorted_array = []
    list_length = Chance.integer(2, 20)
    for i in range(list_length):
        unsorted_array.append(Chance.integer(0, 100))

    sorter = BubbleSorter(unsorted_array)

    for i in range(list_length ** 2):
        sorter.next()

    assert sorter.is_sorted()

def test_bubble_sorter_is_sorted_after_iterating_best_case_scenario():
    """Test bubble sorter is sorted after iterating best case scenario"""

    sorted_array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    list_length = len(sorted_array)
    sorter = BubbleSorter(sorted_array)

    for i in range(list_length):
        sorter.next()

    assert sorter.is_sorted()
