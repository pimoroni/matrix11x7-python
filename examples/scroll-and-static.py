#!/usr/bin/env python

import time

from matrix11x7 import Matrix11x7
matrix11x7 = Matrix11x7()
from matrix11x7.fonts import font3x5

print("""
Matrix 11x7: Hello World

Scrolls "Hello World" across the screen
in a 3x5 pixel condensed font.

Press Ctrl+C to exit!

""")

# Uncomment the below if your display is upside down
#   (e.g. if you're using it in a Pimoroni Scroll Bot)
# matrix11x7.rotate(degrees=180)

# Set a more eye-friendly default brightness
matrix11x7.set_brightness(0.5)

# Write the string to scroll
matrix11x7.write_string(" Hello World! ", x=0, y=1, font=font3x5, brightness=1.0)


def draw_static_elements(buf):
    # Buf is given as a two dimensional array of elements buf[x][y]
    # This method will blink a frame of alternating lights around
    # our scrolling text twice a second.

    if int(time.time() * 2) % 2 == 0:
        for x in range(matrix11x7.width):
            if x % 2 == 0:
                buf[x][0] = 1.0
                buf[x][matrix11x7.height - 1] = 1.0

        for y in range(matrix11x7.height):
            if y % 2 == 0:
                buf[0][y] = 1.0
                buf[matrix11x7.width - 1][y] = 1.0

    return buf


try:
    while True:
        matrix11x7.show(before_display=draw_static_elements)
        matrix11x7.scroll()
        time.sleep(0.05)
except KeyboardInterrupt:
    pass
