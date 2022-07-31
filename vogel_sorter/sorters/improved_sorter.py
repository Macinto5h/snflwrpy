from vogel_sorter.sorters.sort_change import SortChange
from abc import ABC,abstractmethod

class ImprovedSorter(ABC):
    """Sorter interface that applies improved sorter infrastructure"""

    def __init__(self, unsorted_array):
        """Sets up the sorter with the provided unsorted array and sets other internal values."""

        self._unsorted_array = unsorted_array
        self._sorted = False

        self._reset_sort_changes()

    def issorted(self):
        """Returns if the array provided to the sorter is sorted"""

        return self._sorted

    def next(self):
        """Returns the next changes that are made to the array when sorted."""

        self._reset_sort_changes()

        if self._sorted == False:
            self._find_next_changes()

        return self._sort_changes

    @abstractmethod
    def _find_next_changes(self):
        """Finds the next changes the sorting algorithm will apply, and adds them to the sort changes variable if any."""

        pass

    def _record_and_apply_change(self, index, value):
        """Appends sort change to sort changes list and applies the change to the unsorted array."""

        self._sort_changes.append(SortChange(index=index, old_value=self._unsorted_array[index], new_value=value))
        self._unsorted_array[index] = value

    def _reset_sort_changes(self):
        """Resets the internal array for collecting sort changes to be empty"""

        self._sort_changes = []
