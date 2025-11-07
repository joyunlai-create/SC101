"""
File: bouncing_ball.py
Name: Zoe Lai
------------------------
This script simulates bouncing a ball against the ground. Three attempts maximum.
"""

from campy.graphics.gobjects import GOval
from campy.graphics.gwindow import GWindow
from campy.gui.events.timer import pause
from campy.gui.events.mouse import onmouseclicked

VX = 5
vy = 5
DELAY = 10
GRAVITY = 1
SIZE = 20
REDUCE = 0.8
START_X = 30
START_Y = 40

window = GWindow(800, 500, title='bouncing ball')
ball = GOval(SIZE, SIZE)
counter = 0  # count number of times ball goes out of the window
running = False


def main():
    """
    This program simulates a bouncing ball at (START_X, START_Y) that has VX as x velocity
    and 0 as y velocity initially. Each bounce against the ground reduces y velocity to reduce*vy.
    """
    window.add(ball, x=START_X, y=START_Y)
    ball.filled = True
    onmouseclicked(animation)


def animation(event):
    global vy, counter, running
    if running or counter >= 3:
        return  # if ball is dropped or balls goes beyond window for >= 3 times, mouse clicks will not effect animation
    else:
        running = True
        while True:
            # update
            ball.move(VX, vy)
            vy = vy + GRAVITY # gravity applies whenever, falling down or bouncing up

            # evaluate
            if ball.y + SIZE > window.height:  # when the ball goes beyond the ground
                ball.y = window.height-SIZE  # relocate the ball onto the ground
                vy = -vy * REDUCE
            if ball.x + SIZE >= window.width:  # when ball goes out of the window
                counter += 1
                window.add(ball, x=START_X, y=START_Y)  # relocate ball to initial position
                vy = 5  # reset to original vy
                running = False
                break

            # pause
            pause(DELAY)


if __name__ == "__main__":
    main()
