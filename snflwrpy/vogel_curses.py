from curses import wrapper
from snflwrpy.sorter_factory import sorter_factory
from snflwrpy import __name__, __version__
import math
import random
import time

def start_visualizer(algorithm):
    wrapper(main, algorithm)

def main(stdscr, algorithm):
    stdscr.clear()

    florets = 300

    array = []
    for index in range(florets):
        array.append(index)

    random.shuffle(array)

    (mlines, mcols) = stdscr.getmaxyx()
    center_x = mcols / 2
    center_y = mlines / 2

    stdscr.addstr(0,0, __name__ + " " + __version__)
    stdscr.addstr(mlines - 1, 0, f"algorithm: {algorithm} | florets: {florets}")

    for index in range(len(array)):
        r = math.sqrt(array[index])
        angle = index * 137.508
        offset_x = center_x + math.cos(degrees_to_radians(angle)) * (r*2)
        offset_y = center_y + math.sin(degrees_to_radians(angle)) * r

        stdscr.addch(round(offset_y), round(offset_x), '●')

    stdscr.refresh()

    sorter = sorter_factory(algorithm, array)

    start_time = time.time()
    iterations = 0
    while sorter.is_sorted() is False:
        iterations += 1
        changes = sorter.next()

        stdscr.erase()

        stdscr.addstr(0,0, __name__ + " " + __version__)
        stdscr.addstr(mlines - 1, 0, f"algorithm: {algorithm} | florets: {florets} | iterations: {iterations} | time: {round(time.time() - start_time, 2)} seconds")

        for index in range(len(sorter._unsorted_array)):
            r = math.sqrt(sorter._unsorted_array[index])
            angle = index * 137.508
            offset_x = center_x + math.cos(degrees_to_radians(angle)) * (r*2)
            offset_y = center_y + math.sin(degrees_to_radians(angle)) * r

            stdscr.addch(round(offset_y), round(offset_x), '●')

        stdscr.refresh()

    stdscr.refresh()
    stdscr.getkey()

def degrees_to_radians(angle):
    return angle * (math.pi / 180)
