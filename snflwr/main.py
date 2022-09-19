import tkinter as tk
import math
import random
from snflwr.sorter_factory import sorter_factory
from snflwr.sort_type import SortType
from snflwr import __name__
from snflwr import __version__
import sys
import threading

class Application:
    total_items = 600
    oval_diameter = 10
    oval_distance = 12
    algorithm_list = SortType.get_values()
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

        sorter = sorter_factory(self.selected_algorithm.get(), self.array)

        while sorter.is_sorted() == False:
            changes = sorter.next()
            for change in changes:
                self.update_canvas(change.old_value, change.new_value, change.index)

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
        self.master.title(__name__ + " v" + __version__)
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
