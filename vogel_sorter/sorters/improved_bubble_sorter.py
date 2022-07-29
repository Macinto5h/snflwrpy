from vogel_sorter.sorters.improved_sorter import ImprovedSorter

class ImprovedBubbleSorter(ImprovedSorter):

    def __init__(self, unsorted_array=[]):
        super().__init__(unsorted_array)
        self._sort_index = 1
        self._swapped = False

    def next(self):
        self._reset_sort_changes()

        if self._sorted == False:
            self._swap_elements_if_needed()
            self._update_index_and_sorted_status()

        return super().next()

    def _swap_elements_if_needed(self):
        expected_smaller_element = self._unsorted_array[self._sort_index - 1]
        expected_larger_element = self._unsorted_array[self._sort_index]

        if expected_smaller_element > expected_larger_element:
            self._record_and_apply_change(self._sort_index - 1, expected_larger_element)
            self._record_and_apply_change(self._sort_index, expected_smaller_element)
            self._swapped = True

    def _update_index_and_sorted_status(self):
        if self._sort_index == len(self._unsorted_array) - 1 and self._swapped == False:
            self._sorted = True
        elif self._sort_index == len(self._unsorted_array) - 1:
            self._sort_index = 1
            self._swapped = False
        else:
            self._sort_index += 1