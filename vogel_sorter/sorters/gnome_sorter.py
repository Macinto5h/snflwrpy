from vogel_sorter.sorters.sorter import Sorter
import math

class GnomeSorter(Sorter):
    def sort(self, Application, list):
        index = 0
        while (index < len(list)):
            if (index == 0 or list[index] >= list[index-1]):
                index += 1
            else:
                temp = list[index]
                list[index] = list[index-1]
                Application.update_canvas(temp,list[index],index)
                list[index-1] = temp
                Application.update_canvas(list[index],list[index-1],index-1)
                index -= 1
