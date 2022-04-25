from vogel_sorter.sorters.sorter import Sorter
import math

class RadixLSDSorter(Sorter):
    def sort(self,Application,list):
        maxValue = max(list)
        i = 0
        #10 is the base value since values of the list are in decimal
        while 10 ** i <= maxValue:
            list = self.buckets_to_list(self.list_to_buckets(list,i),Application,list)
            i += 1

    def list_to_buckets(self,array,iteration):
        buckets = [[] for x in range(10)]
        for i in array:
            digit = (i // (10 ** iteration)) % 10
            buckets[digit].append(i)
        return buckets

    def buckets_to_list(self,buckets,Application,list):
        numbers = []
        index = 0
        for bucket in buckets:
            for j in bucket:
                numbers.append(j)
                Application.update_canvas(list[index],j,index)
                index += 1
        return numbers
