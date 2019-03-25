#!/usr/bin/env python

import time

from matrix11x7 import Matrix11x7
matrix11x7 = Matrix11x7()
from matrix11x7.fonts import font5x7unicode

matrix11x7.set_font(font5x7unicode)

print("""
Matrix 11x7: Simple Scrolling

A simple example showing a basic scrolling loop for scrolling
single messages across the display.

Press Ctrl+C to exit.
""")


def scroll_message(message):
    matrix11x7.clear()                         # Clear the display and reset scrolling to (0, 0)
    length = matrix11x7.write_string(message)  # Write out your message
    matrix11x7.show()                          # Show the result
    time.sleep(0.5)                              # Initial delay before scrolling

    length -= matrix11x7.width

    # Now for the scrolling loop...
    while length > 0:
        matrix11x7.scroll(1)                   # Scroll the buffer one place to the left
        matrix11x7.show()                      # Show the result
        length -= 1
        time.sleep(0.02)                         # Delay for each scrolling step

    time.sleep(0.5)                              # Delay at the end of scrolling


message = "".join([unichr(x) for x in range(256)])

scroll_message(message)
