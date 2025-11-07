"""
File: draw_line.py
Name: Zoe Lai
-------------------------
This script indefinitely draw lines on canvas.
"""

from campy.graphics.gobjects import GOval, GLine
from campy.graphics.gwindow import GWindow
from campy.gui.events.mouse import onmouseclicked

window = GWindow(600, 800)
SIZE = 10
circle = GOval(SIZE, SIZE)
click_counter = 0  # to track even/odd clicks


def main():
    """
    This program creates lines on an instance of GWindow class.
    There is a circle indicating the user’s first click. A line appears
    at the condition where the circle disappears as the user clicks
    on the canvas for the second time.
    """
    onmouseclicked(click)


def click(event):
    global click_counter
    click_counter += 1
    if click_counter % 2 != 0: # odd clicks (circle appears)
        window.add(circle, x=event.x - SIZE/2, y=event.y - SIZE/2)
    else: # even number clicks (draws line)
        window.remove(circle)
        line = GLine(circle.x + SIZE/2, circle.y + SIZE/2, event.x, event.y)
        window.add(line)


if __name__ == "__main__":
    main()
