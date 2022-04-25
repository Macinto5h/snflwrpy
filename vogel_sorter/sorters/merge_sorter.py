from vogel_sorter.sorters.sorter import Sorter
import math

class MergeSorter(Sorter):
    def merge(self, Application, list, p, q, r):
        left_length = q-p+1
        right_length = r-q
        l = 0
        ri = 0
        left_list = []
        right_list = []
        for index in range(p, q+1, 1):
            left_list.append(list[index])
        for index in range(q+1, r+1, 1):
            right_list.append(list[index])
        for index in range(p, r+1, 1):
            old_value = list[index]
            if (l == left_length):
                list[index] = right_list[ri]
                ri += 1
            elif (ri == right_length or left_list[l]<=right_list[ri]):
                list[index] = left_list[l]
                l += 1
            else:
                list[index] = right_list[ri]
                ri += 1
            Application.update_canvas(old_value,list[index],index)
    def merge_sort(self, Application, list, p, r):
        if (p < r):
            q = (p+r)//2
            self.merge_sort(Application, list, p, q)
            self.merge_sort(Application, list, q+1, r)
            self.merge(Application,list,p,q,r)

    def sort(self, Application, list):
        self.merge_sort(Application, list, 0, len(list)-1)
