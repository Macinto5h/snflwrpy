from vogel_sorter.sorters.sorter import Sorter
import math

class SelectionSorter(Sorter):
    def sort(self, Application, list):
        length = len(list)
        for i in range(length):
            m = list[i] #smallest value variable
            j = i + 1
            swap_index = i
            while (j < length):
                if (list[j] < m):
                    m = list[j]
                    swap_index = j
                j += 1
            Application.update_canvas(list[swap_index],list[i],swap_index)
            list[swap_index] = list[i]
            Application.update_canvas(list[i], m, i)
            list[i] = m
