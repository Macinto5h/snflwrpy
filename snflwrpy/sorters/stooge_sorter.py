"""Module for the StoogeSorter class"""
import math
from snflwrpy.sorters.abstract_sorter import AbstractSorter

class StoogeSorter(AbstractSorter):
    """Sorter implementation of the stooge sort algorithm"""

    def __init__(self, unsorted_array):
        super().__init__(unsorted_array)
        self._stooge_actions = []
        self._add_action(0, len(unsorted_array) - 1)

    def next(self):
        if len(self._stooge_actions) == 0:
            self._sorted = True
            return

        action = self._stooge_actions.pop()
        expected_smallest_element = self._unsorted_array[action.leftmost_index]
        expected_largest_element = self._unsorted_array[action.rightmost_index]
        if expected_smallest_element > expected_largest_element:
            self._swap(action.leftmost_index, action.rightmost_index)

        len_of_subarray = action.rightmost_index - action.leftmost_index + 1
        if len_of_subarray > 2:
            third_of_subarray_len = math.floor(len_of_subarray / 3)
            self._add_action(action.leftmost_index, action.rightmost_index - third_of_subarray_len)
            self._add_action(action.leftmost_index + third_of_subarray_len, action.rightmost_index)
            self._add_action(action.leftmost_index, action.rightmost_index - third_of_subarray_len)

    def _add_action(self, leftmost_index, rightmost_index):
        self._stooge_actions.append(StoogeAction(leftmost_index, rightmost_index))

class StoogeAction():

    def __init__(self, leftmost_index, rightmost_index):
        self._leftmost_index = leftmost_index
        self._rightmost_index = rightmost_index

    @property
    def leftmost_index(self):
        return self._leftmost_index

    @property
    def rightmost_index(self):
        return self._rightmost_index
