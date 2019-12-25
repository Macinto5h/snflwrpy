########################################
#GUI for Sorting Algorithm Visualizer  #
#Uses Vogel's Fibonacci Model          #
#to represent a sorted visual sequence #
#                                      #
#Author: Macinto5h                     #
########################################
import tkinter as tk
import math
import random #needed for shuffle function
import sorting_algorithms as sa #stores all the algorithm classes
import sys
import threading

class Application:
    #Constants for Application are defined here....
    total_items = 600
    oval_diameter = 10
    oval_distance = 12
    algorithm_list = [
        "Insertion Sort",
        "Bubble Sort",
        "Merge Sort",
        "Selection Sort",
        "Cocktail Sort",
        "Gnome Sort",
        "Shell Sort",
        "Radix Sort LSD",
        "Stooge Sort"
    ]
    canvas_height = 700

    def build_array(self):
        self.array = []
        for index in range(self.total_items):
            self.array.append(index)

    def degrees_to_radians(self, angle):
        return angle * (math.pi / 180)

    def draw_canvas(self):
        for index in range(len(self.oval_array)):
            self.canvas.delete(self.oval_array[index])
        self.oval_array.clear()
        center_x = self.canvas_height/2
        center_y = center_x
        for index in range(self.total_items):
            r = self.oval_distance * math.sqrt(self.array[index]) #distance from center
            angle = index * 137.508   #angle
            offset_x = center_x + math.cos(self.degrees_to_radians(angle))*r
            offset_y = center_y + math.sin(self.degrees_to_radians(angle))*r
            oval_fill = "white"
            if (index+1)%5 == 1:
                oval_fill = "red"
            elif (index+1)%5 == 2:
                oval_fill = "orange"
            elif (index+1)%5 == 3:
                oval_fill = "green"
            elif (index+1)%5 == 4:
                oval_fill = "blue"
            else:
                oval_fill = "purple"
            self.oval_array.append(self.canvas.create_oval(offset_x + self.oval_diameter,
            offset_y + self.oval_diameter, offset_x, offset_y, fill=oval_fill, outline=oval_fill))
        self.canvas.update_idletasks()

    def shuffle_canvas(self):
        random.shuffle(self.array)
        self.draw_canvas()

    def sort_canvas(self):

        app = self

        sort = sa.Sort()

        if (self.selected_algorithm.get() == "Bubble Sort"):
            sort = sa.BubbleSort()
            
        elif (self.selected_algorithm.get() == "Merge Sort"):
            sort = sa.MergeSort()
        elif (self.selected_algorithm.get() == "Selection Sort"):
            sort = sa.SelectionSort()
        elif (self.selected_algorithm.get() == "Cocktail Sort"):
            sort = sa.CocktailSort()
        elif (self.selected_algorithm.get() == "Gnome Sort"):
            sort = sa.GnomeSort()
        elif (self.selected_algorithm.get() == "Shell Sort"):
            sort = sa.ShellSort()
        elif (self.selected_algorithm.get() == "Radix Sort LSD"):
            sort = sa.RadixSortLSD()
        elif (self.selected_algorithm.get() == "Stooge Sort"):
            sort = sa.StoogeSort()
        else:
            sort = sa.InsertionSort()
        threading.Thread(target=sort.sort(app, app.array)).start()

    def update_canvas(self, old_value, new_value, index):
        center_x = self.canvas_height/2
        center_y = center_x
        angle = index * 137.508
        old_distance = self.oval_distance * math.sqrt(old_value)
        new_distance = self.oval_distance * math.sqrt(new_value)
        offset_x = center_x + math.cos(self.degrees_to_radians(angle))*new_distance
        offset_x -= center_x + math.cos(self.degrees_to_radians(angle))*old_distance
        offset_y = center_y + math.sin(self.degrees_to_radians(angle))*new_distance
        offset_y -= center_y + math.sin(self.degrees_to_radians(angle))*old_distance
        self.canvas.move(self.oval_array[index], offset_x, offset_y)
        self.canvas.update_idletasks()

    def __init__(self, master):
        self.master = master
        self.build_array()
        self.oval_array = []

        self.canvas = tk.Canvas(self.master, bg="#36454F",height=self.canvas_height, width=self.canvas_height, highlightthickness=0)
        self.draw_canvas()
        self.canvas.pack()
        self.selected_algorithm = tk.StringVar(self.master)
        self.selected_algorithm.set(self.algorithm_list[0])
        self.option_menu = tk.OptionMenu(self.master,self.selected_algorithm,*self.algorithm_list)
        self.option_menu.pack()

        self.menubar = tk.Menu(self.master)
        # display the menu
        self.master.config(menu=self.menubar)
        self.menubar.add_command(label="Shuffle", command=self.shuffle_canvas)
        self.menubar.add_command(label="Sort", command=self.sort_canvas)

def main():
    root = tk.Tk()
    root.configure(background="#36454F")
    root.title("Sorting Algorithm Visualizer v0.0.1")
    root.resizable(width=False, height=False)
    sys.setrecursionlimit(1500)
    app = Application(root)
    root.mainloop()
if __name__ == '__main__':
    main()
