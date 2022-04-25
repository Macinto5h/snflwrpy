from vogel_sorter.sorters.sorter import Sorter
import math

class StoogeSorter(Sorter):
    def sort(self, Application, list):
        self.stoogeSortHelper(Application, list, 0, len(list) - 1)

    def stoogeSortHelper(self, Application, list, i, j):
        if (list[i] > list[j]):
            tmp = list[i]
            Application.update_canvas(list[i],list[j],i)
            list[i] = list[j]
            Application.update_canvas(list[j],tmp,j)
            list[j] = tmp

        if ((j - i + 1) > 2):
            # t = -(-(j - i + 1) // 3)
            t = (j - i + 1) // 3
            self.stoogeSortHelper(Application, list, i, j - t)
            self.stoogeSortHelper(Application, list, i + t, j)
            self.stoogeSortHelper(Application, list, i, j - t)
