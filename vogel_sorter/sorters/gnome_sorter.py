"""Module for GnomeSorter class"""
from vogel_sorter.sorters.abstract_sorter import AbstractSorter

class GnomeSorter(AbstractSorter):
    """Sorter implementation of the gnome sort algorithm"""

    def __init__(self, unsorted_array):
        super().__init__(unsorted_array)
        self._sort_index = 1
        self._swapped = False

    def next(self):
        changes = self._swap_elements_if_needed()
        self._update_index_and_sorted_status()
        return changes

    def _swap_elements_if_needed(self):
        if self._sort_index == 0:
            return []

        changes = []
        expected_smaller_element = self._unsorted_array[self._sort_index - 1]
        expected_larger_element = self._unsorted_array[self._sort_index]

        if expected_smaller_element > expected_larger_element:
            changes.append(self._apply_change(self._sort_index - 1, expected_larger_element))
            changes.append(self._apply_change(self._sort_index, expected_smaller_element))
            self._swapped = True

        return changes

    def _update_index_and_sorted_status(self):
        if self._sort_index == len(self._unsorted_array) - 1 and self._swapped is False:
            self._sorted = True
            return

        if self._swapped:
            self._sort_index -= 1
            self._swapped = False
        else:
            self._sort_index += 1
