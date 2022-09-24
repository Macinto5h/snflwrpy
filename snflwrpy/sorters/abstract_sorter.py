from snflwrpy.sorters.sort_change import SortChange
from abc import ABC,abstractmethod

class AbstractSorter(ABC):
    """Sorter interface that applies abstract sorter infrastructure"""

    def __init__(self, unsorted_array):
        """Sets up the sorter with the provided unsorted array and sets other internal values."""

        self._unsorted_array = unsorted_array
        self._sorted = False

    def is_sorted(self):
        """Returns if the array provided to the sorter is sorted"""

        return self._sorted

    @abstractmethod
    def next(self):
        """Returns the next changes that are made to the array when sorted."""

        pass

    def _apply_change(self, index, new_value):
        """Applies the change to the unsorted array and returns a SortChange object."""

        old_value = self._unsorted_array[index]
        self._unsorted_array[index] = new_value

        return SortChange(index, old_value, new_value)
