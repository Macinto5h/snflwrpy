"""Module for the InsertionSorter class"""
from snflwrpy.sorters.abstract_sorter import AbstractSorter

class InsertionSorter(AbstractSorter):
    """Sorter implementation of the insertion sort algorithm"""

    def __init__(self, unsorted_array):
        super().__init__(unsorted_array)

        if len(unsorted_array) > 1:
            self._outer_sort_index = 1
            self._set_outer_sort_value_and_inner_sort_index()

    def next(self):
        changes = []

        if (self._inner_sort_index >= 0
            and self._unsorted_array[self._inner_sort_index] > self._outer_sort_value):
            new_value = self._unsorted_array[self._inner_sort_index]
            changes.append(self._apply_change(self._inner_sort_index + 1, new_value))
            self._inner_sort_index -= 1
        else:
            changes.append(self._apply_change(self._inner_sort_index + 1, self._outer_sort_value))
            self._update_sort_status_and_indices()

        return changes

    def _update_sort_status_and_indices(self):
        self._outer_sort_index += 1

        if self._outer_sort_index >= len(self._unsorted_array):
            self._sorted = True
            return

        self._set_outer_sort_value_and_inner_sort_index()

    def _set_outer_sort_value_and_inner_sort_index(self):
        self._outer_sort_value = self._unsorted_array[self._outer_sort_index]
        self._inner_sort_index = self._outer_sort_index - 1
