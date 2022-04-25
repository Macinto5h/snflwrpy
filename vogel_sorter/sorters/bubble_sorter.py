from vogel_sorter.sorters.sorter import Sorter
import math

class BubbleSorter(Sorter):
    def sort(self, Application, list):
        length = len(list)
        for index_0 in range(length):
            for index_1 in range(length-1,index_0,-1):
                if (list[index_1-1] > list[index_1]):
                    temp = list[index_1]
                    list[index_1] = list[index_1-1]
                    Application.update_canvas(temp,list[index_1],index_1)
                    list[index_1-1] = temp
                    Application.update_canvas(list[index_1],list[index_1-1],index_1-1)
