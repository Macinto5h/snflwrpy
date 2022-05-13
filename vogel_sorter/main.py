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
from vogel_sorter.sorter_factory import SorterFactory
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

        sort = SorterFactory().get_sorter(self.selected_algorithm.get())

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

    def start(self, algorithm):
        self.master = tk.Tk()
        self.master.configure(background="#36454F")
        self.master.title("Sorting Algorithm Visualizer v0.0.1")
        self.master.resizable(width=False, height=False)
        sys.setrecursionlimit(1500)

        self.build_array()
        self.oval_array = []

        self.canvas = tk.Canvas(self.master, bg="#36454F",height=self.canvas_height, width=self.canvas_height, highlightthickness=0)
        self.draw_canvas()
        self.canvas.pack()
        self.selected_algorithm = tk.StringVar(self.master)
        self.selected_algorithm.set(algorithm)
        self.option_menu = tk.OptionMenu(self.master,self.selected_algorithm,*self.algorithm_list)
        self.option_menu.pack()

        self.menubar = tk.Menu(self.master)
        # display the menu
        self.master.config(menu=self.menubar)
        self.menubar.add_command(label="Shuffle", command=self.shuffle_canvas)
        self.menubar.add_command(label="Sort", command=self.sort_canvas)

        self.master.mainloop()

if __name__ == '__main__':
    Application()
