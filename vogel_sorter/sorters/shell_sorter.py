from vogel_sorter.sorters.sorter import Sorter
import math

class ShellSorter(Sorter):
    def sort(self, Application, list):
        gap = len(list)//2
        while (gap > 0):
            for i in range(gap,len(list)):
                temp = list[i]
                j = i
                while j >= gap and list[j-gap] > temp:
                    Application.update_canvas(list[j],list[j-gap],j)
                    list[j] = list[j-gap]
                    j -= gap
                Application.update_canvas(list[j],temp,j)
                list[j] = temp
            gap //= 2
