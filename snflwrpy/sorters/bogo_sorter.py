"""Module for the BogoSorter class"""
import random
from snflwrpy.sorters.abstract_sorter import AbstractSorter

class BogoSorter(AbstractSorter):
    """Sorter implementation of the bogo sort algorithm"""

    def next(self):
        random.shuffle(self._unsorted_array)

    def is_sorted(self):
        for index in range(len(self._unsorted_array) - 1):
            if self._unsorted_array[index] > self._unsorted_array[index + 1]:
                return False
        return True
