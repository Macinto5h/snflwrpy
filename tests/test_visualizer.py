"""Test suite for the visualizer"""
from chancepy import Chance
from snflwrpy.visualizer import *

def test_build_shuffled_array_returns_array_with_provided_item_count():
    """Test build shuffled array returns array with provided item count"""

    item_count = Chance.integer(0, 100)
    array = build_shuffled_array(item_count)
    assert len(array) == item_count

def test_draw_renders_text_and_sunflower_visual(mocker):
    """Test draw renders text and sunflower visual to terminal"""
    stdscr = mocker.MagicMock()
    max_y = Chance.integer(400,500)
    max_x = Chance.integer(400,500)
    stdscr.getmaxyx.return_value = (max_y, max_x)
    stats_text = Chance.string()
    array = [Chance.integer(0,100) for i in range(Chance.integer(1, 100))]

    draw(stdscr, stats_text, array)

    stdscr.erase.assert_called_once()
    stdscr.addstr.assert_any_call(0, 0, TITLE_TEXT)
    stdscr.addstr.assert_any_call(max_y - 1, 0, stats_text)
    stdscr.addch.assert_called()
    stdscr.refresh.assert_called_once()
