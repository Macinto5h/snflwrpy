"""Module for CocktailSorter class"""
from vogel_sorter.sorters.bubble_sorter import BubbleSorter

class CocktailSorter(BubbleSorter):
    """Sorter implementation of the cocktail shaker sort algorithm"""

    def __init__(self, unsorted_array):
        super().__init__(unsorted_array)
        self._stepper = 1

    def _update_index_and_sorted_status(self):
        if self._no_swaps_occurred_while_iterating_array():
            self._sorted = True
            return

        self._update_index()

    def _update_index(self):
        if self._has_reached_beginning_or_end_of_array():
            self._swapped = False
            self._stepper *= -1

        self._sort_index += self._stepper

    def _no_swaps_occurred_while_iterating_array(self):
        return self._has_reached_beginning_or_end_of_array() and self._swapped is False

    def _has_reached_beginning_or_end_of_array(self):
        has_reached_beginning = self._sort_index == 1 and self._stepper == -1
        has_reached_end = self._sort_index == len(self._unsorted_array) - 1

        return has_reached_beginning or has_reached_end
