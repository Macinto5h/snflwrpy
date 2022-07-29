from vogel_sorter.sorters.sort_change import SortChange

class ImprovedSorter:
    """Sorter interface that applies improved sorter infrastructure"""

    def __init__(self, unsorted_array=[]):
        """Sets up the sorter with an optional unsorted array"""

        self._unsorted_array = unsorted_array
        self._sorted = False

        self._reset_sort_changes()

    def issorted(self):
        """Returns if the array provided to the sorter is sorted"""

        return self._sorted

    def next(self):
        """Returns the next changes that are made to the array when sorted. Must be implemented for all subclasses."""

        return self._sort_changes

    def _record_and_apply_change(self, index, value):
        """Appends sort change to sort changes list and applies the change to the unsorted array"""

        self._sort_changes.append(SortChange(index=index, old_value=self._unsorted_array[index], new_value=value))
        self._unsorted_array[index] = value

    def _reset_sort_changes(self):
        """Resets the internal array for collecting sort changes to be empty"""

        self._sort_changes = []
