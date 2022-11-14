"""
Test suite for the abstract_sorter module.
"""
from snflwrpy.sort_type import SortType
from snflwrpy.sorter_factory import sorter_factory
from chancepy import Chance

def test_abstract_sorter_swap_method_swaps_values_in_unsorted_array():
    """Test abstract sorter swap method swaps values in unsorted array"""

    first_number = Chance.integer(51, 100)
    second_number = Chance.integer(0, 50)
    unsorted_array = [first_number, second_number]
    sorter = sorter_factory(Chance.pickone(SortType.get_values()), unsorted_array)

    sorter._swap(0, 1)

    assert sorter.get_array()[0] == second_number
    assert sorter.get_array()[1] == first_number
