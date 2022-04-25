from vogel_sorter.sorters.sorter import Sorter
import math

class CocktailSorter(Sorter):
    def sort(self, Application, list):
        swapped = True
        while (swapped == True):
            swapped = False
            for i in range(len(list)-2):
                if (list[i] > list[i+1]):
                    temp = list[i]
                    list[i] = list[i+1]
                    Application.update_canvas(temp,list[i],i)
                    list[i+1] = temp
                    Application.update_canvas(list[i],list[i+1],i+1)
                    swapped = True
            if (swapped == False):
                break
            for i in range(len(list)-2,0,-1):
                if (list[i] > list[i+1]):
                    temp = list[i]
                    list[i] = list[i+1]
                    Application.update_canvas(temp,list[i],i)
                    list[i+1] = temp
                    Application.update_canvas(list[i],list[i+1],i+1)
                    swapped = True
