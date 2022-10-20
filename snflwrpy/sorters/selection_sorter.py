"""Module for the SelectionSorter class"""
from snflwrpy.sorters.abstract_sorter import AbstractSorter

class SelectionSorter(AbstractSorter):
    """Sorter implementation of the selection sort algorithm"""

    def __init__(self, unsorted_array):
        super().__init__(unsorted_array)

        self._outer_sort_index = 0
        self._min_index = 0
        self._inner_sort_index = 1

    def next(self):
        self._change_min_index_if_needed()
        self._update_indices_and_sort_status()

    def _change_min_index_if_needed(self):
        expected_smaller_element = self._unsorted_array[self._min_index]
        expected_larger_element = self._unsorted_array[self._inner_sort_index]

        if expected_smaller_element > expected_larger_element:
            self._min_index = self._inner_sort_index

    def _update_indices_and_sort_status(self):
        if self._outer_sort_index == len(self._unsorted_array) - 2 and self._inner_sort_index == len(self._unsorted_array) - 1:
            self._sorted = True
        elif self._inner_sort_index == len(self._unsorted_array) - 1:
            self._swap_if_needed()
            self._outer_sort_index += 1
            self._inner_sort_index = self._outer_sort_index + 1
            self._min_index = self._outer_sort_index
        else:
            self._inner_sort_index += 1

    def _swap_if_needed(self):
        if self._min_index != self._outer_sort_index:
            minimum = self._unsorted_array[self._min_index]
            self._unsorted_array[self._min_index] = self._unsorted_array[self._outer_sort_index]
            self._unsorted_array[self._outer_sort_index] = minimum
