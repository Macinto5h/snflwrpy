"""
Test suite for improved_sorter module.
"""
from vogel_sorter.sorters.improved_sorter import ImprovedSorter
from vogel_sorter.sorters.sort_change import SortChange
from chancepy import Chance

def test_improved_sorter_has_empty_unsorted_list_when_constructed_with_no_args():
    """Test improved sorter has empty unsorted list when constructed with no args"""

    sorter = ImprovedSorter()
    assert sorter._unsorted_array == []

def test_improved_sorter_has_unsorted_list_when_constructed_with_list_arg():
    """Test improved sorter has unsorted list when constructed with list arg"""

    unsorted_array = []

    list_length = Chance.integer(1, 20)
    for i in range(0, list_length):
        unsorted_array.append(Chance.integer(0, 100))

    sorter = ImprovedSorter(unsorted_array)
    assert sorter._unsorted_array == unsorted_array


def test_improved_sorter_has_unsorted_status_when_list_is_unsorted():
    """Test improved sorter always has unsorted status"""

    unsorted_array = [Chance.integer(21, 40), Chance.integer(1,20)]
    sorter = ImprovedSorter(unsorted_array)
    assert sorter.issorted() == False

def test_improved_sorter_next_returns_changes_made_to_unsorted_list():
    """Test improved sorter next returns changes made to unsorted list"""

    unsorted_array = unsorted_array = [Chance.integer(21, 40), Chance.integer(1,20)]
    sorter = ImprovedSorter(unsorted_array)
    next_results = sorter.next()
    assert next_results == sorter._sort_changes

def test_improved_sorter_applies_and_records_change_made_by_sorting():
    """Test improved sorter applies and records change made by sorting"""

    unsorted_array = []

    list_length = Chance.integer(2, 20)
    for i in range(0, list_length):
        unsorted_array.append(Chance.integer(0, 100))

    sorter = ImprovedSorter(unsorted_array)

    random_index = Chance.integer(0, list_length - 1)
    random_value = Chance.integer(0, 100)
    expected_sort_change = SortChange(index=random_index, old_value=sorter._unsorted_array[random_index], new_value=random_value)
    sorter._record_and_apply_change(random_index, random_value)

    assert sorter._unsorted_array[random_index] == random_value
    assert sorter._sort_changes[0] == expected_sort_change