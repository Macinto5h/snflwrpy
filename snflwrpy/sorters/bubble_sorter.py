"""Module for the BubbleSorter class"""
from snflwrpy.sorters.abstract_sorter import AbstractSorter

class BubbleSorter(AbstractSorter):
    """Sorter implementation of the bubble sort algorithm"""

    def __init__(self, unsorted_array):
        super().__init__(unsorted_array)
        self._sort_index = 1
        self._swapped = False

    def next(self):
        self._swap_if_needed()
        self._update_index_and_sorted_status()

    def _swap_if_needed(self):
        if self._unsorted_array[self._sort_index - 1] > self._unsorted_array[self._sort_index]:
            self._swap(self._sort_index - 1, self._sort_index)
            self._swapped = True

    def _update_index_and_sorted_status(self):
        if self._sort_index == len(self._unsorted_array) - 1 and self._swapped is False:
            self._sorted = True
        elif self._sort_index == len(self._unsorted_array) - 1:
            self._sort_index = 1
            self._swapped = False
        else:
            self._sort_index += 1
