"""Module for the RadixLSDSorter class"""
from snflwrpy.sorters.abstract_sorter import AbstractSorter

class RadixLSDSorter(AbstractSorter):
    """Sorter implementation of the radix lsd sort algorithm"""

    def __init__(self, unsorted_array):
        super().__init__(unsorted_array)
        self._max_value = max(unsorted_array)
        self._digit_power = 0

        self._reset_buckets_and_indices()

    def next(self):
        bucket = self._buckets[self._bucket_list_index]

        while len(bucket) == 0:
            self._bucket_list_index += 1
            bucket = self._buckets[self._bucket_list_index]

        self._unsorted_array[self._array_index] = bucket[self._bucket_index]

        self._update_indices_and_buckets()

    def _update_indices_and_buckets(self):
        reached_end_of_array = self._array_index == len(self._unsorted_array) - 1
        reached_most_significant_digit = (self._max_value // (10 ** self._digit_power)) < 10
        reached_end_of_bucket = self._bucket_index >= len(self._buckets[self._bucket_list_index]) - 1

        if reached_end_of_array and reached_most_significant_digit:
            self._sorted = True
        elif reached_end_of_array:
            self._digit_power += 1
            self._reset_buckets_and_indices()
        elif reached_end_of_bucket:
            self._bucket_list_index += 1
            self._bucket_index = 0
            self._array_index += 1
        else:
            self._bucket_index += 1
            self._array_index += 1


    def _reset_buckets_and_indices(self):
        self._bucket_list_index = 0
        self._bucket_index = 0
        self._array_index = 0
        self._buckets = [[] for x in range(10)]

        for i in self._unsorted_array:
            digit = (i // (10 ** self._digit_power)) % 10
            self._buckets[digit].append(i)
