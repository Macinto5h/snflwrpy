########################################
#GUI for Sorting Algorithm Visualizer  #
#Uses Vogel's Fibonacci Model          #
#to represent a sorted visual sequence #
#                                      #
#Author: Macinto5h                     #
#Last Update: 10/26/2018               #
########################################
import tkinter as tk
import math
import random #needed for shuffle function
from insertion_sort import InsertionSort
#import time delete after testing is done...

class Application:
    def build_array(self):
        self.array = []
        for index in range(self.oval_count):
            self.array.append(index)

    def degrees_to_radians(self, angle):
        return angle * (math.pi / 180)

    def draw_canvas(self):
        for index in range(len(self.oval_array)):
            self.canvas.delete(self.oval_array[index])
        self.oval_array.clear()
        center_x = self.canvas_height/2
        center_y = center_x
        for index in range(self.oval_count):
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
            self.oval_array.append(self.canvas.create_oval(offset_x + self.oval_diameter, offset_y + self.oval_diameter, offset_x, offset_y, fill=oval_fill, outline=oval_fill))
        self.canvas.update_idletasks()

    def shuffle_canvas(self):
        random.shuffle(self.array)
        self.draw_canvas()

    def sort_canvas(self):
        InsertionSort(self)

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
        self.oval_count = 600
        self.oval_diameter = 10;
        self.oval_distance = 12;
        self.build_array()
        self.oval_array = []
        self.canvas_height=750
        self.canvas = tk.Canvas(self.master, bg="white",height=self.canvas_height, width=self.canvas_height)
        self.draw_canvas()
        self.canvas.pack()
        self.shuffle_button = tk.Button(master, text="Shuffle", command=self.shuffle_canvas)
        self.sort_button = tk.Button(master, text="Sort", command=self.sort_canvas)
        self.shuffle_button.pack()
        self.sort_button.pack()

def main():
    root = tk.Tk()
    app = Application(root)
    root.mainloop()
if __name__ == '__main__':
    main()
