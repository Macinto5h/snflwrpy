"""Module for AbstractSorter class"""
from abc import ABC, abstractmethod

class AbstractSorter(ABC):
    """Sorter interface that applies abstract sorter infrastructure"""

    def __init__(self, unsorted_array):
        """Sets up the sorter with the provided unsorted array and sets other internal values."""

        self._unsorted_array = unsorted_array
        self._sorted = False

    def is_sorted(self):
        """Returns if the array provided to the sorter is sorted"""

        return self._sorted

    def get_array(self):
        """Returns the array being sorted by the sorter in its current state."""

        return self._unsorted_array

    def _swap(self, index_0, index_1):
        tmp = self._unsorted_array[index_0]

        self._unsorted_array[index_0] = self._unsorted_array[index_1]
        self._unsorted_array[index_1] = tmp

    @abstractmethod
    def next(self):
        """Returns the next changes that are made to the array when sorted."""
