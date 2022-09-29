"""Module for snflwrpy Visualizer that uses the curses library"""
import math
import random
import time
from snflwrpy.sorter_factory import sorter_factory
from snflwrpy import __app_name__, __app_version__

CONSTANT_SCALING_FACTOR = 137.508
TITLE_TEXT = f"{__app_name__} {__app_version__}"

def visualizer_start(stdscr, args):
    array = build_shuffled_array(args.floret_count)
    sorter = sorter_factory(args.algorithm, array)
    start_time = time.time()
    iterations = 0

    while sorter.is_sorted() is False:
        iterations += 1
        sorter.next()

        stats_text = f"algorithm: {args.algorithm} | florets: {args.floret_count} | iterations: {iterations} | time: {round(time.time() - start_time, 2)} seconds"
        draw(stdscr, stats_text, sorter._unsorted_array)

    stdscr.getkey()

def build_shuffled_array(item_count):
    array = []
    for index in range(item_count):
        array.append(index)

    random.shuffle(array)
    return array


def draw(stdscr, stats_text, array):
    stdscr.erase()

    (mlines, mcols) = stdscr.getmaxyx()
    center_x = mcols / 2
    center_y = mlines / 2

    stdscr.addstr(0, 0, TITLE_TEXT)
    stdscr.addstr(mlines - 1, 0, stats_text)

    for index in range(len(array)):
        radius = math.sqrt(array[index])
        angle = index * CONSTANT_SCALING_FACTOR
        offset_x = center_x + math.cos(math.radians(angle)) * (radius * 2)
        offset_y = center_y + math.sin(math.radians(angle)) * radius

        stdscr.addch(round(offset_y), round(offset_x), '●')

    stdscr.refresh()
