########################################
#GUI for Sorting Algorithm Visualizer  #
#Uses Vogel's Fibonacci Model          #
#to represent a sorted visual sequence #
#                                      #
#Author: Macinto5h                     #
#Last Update: 10/19/2018               #
########################################
import tkinter
import math

def degrees_to_radians( angle ):
    return angle * (math.pi / 180)

top = tkinter.Tk()
top.title("Sorting Algorithm Visualizer")
t_canvas = tkinter.Canvas(top, bg="white",height=750, width=750)
center_x = 375
center_y = center_x
for index in range(500):
    r = 10 * math.sqrt(index) #distance from center 
    angle = index * 137.508   #angle
    offset_x = center_x + math.cos(degrees_to_radians(angle))*r
    offset_y = center_y + math.sin(degrees_to_radians(angle))*r
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
    t_canvas.create_oval(offset_x + 6, offset_y + 6, offset_x, offset_y, fill=oval_fill, outline=oval_fill)
#oval = t_canvas.create_oval(40,40,80,80)
t_canvas.pack()
top.mainloop()
