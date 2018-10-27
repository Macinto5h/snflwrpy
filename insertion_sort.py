import time

class InsertionSort:
    def sort(self, Application, list):
        length = len(list)
        for index in range(1, length):
            k = list[index]
            i = index-1
            while(i >= 0 and list[i]>k):
                old_value = list[i+1]
                new_value = list[i]
                list[i+1]=list[i]
                Application.update_canvas(old_value,new_value,i+1)
                #time.sleep(0.001)
                i = i - 1
            old_value = list[i+1]
            list[i+1] = k
            Application.update_canvas(old_value,k,i+1)
            #time.sleep(0.001)

    def __init__(self, Application):
        self.sort(Application, Application.array)
