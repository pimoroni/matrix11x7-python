#!/usr/bin/env python

import time

import matrix11x7
from matrix11x7.fonts import font5x5

print("""
Matrix 11x7: Portrait Clock

Displays hours, minutes and seconds in text.

Press Ctrl+C to exit!

""")

matrix11x7.set_brightness(0.3)
matrix11x7.rotate(270)

while True:
    matrix11x7.clear()

    # See https://docs.python.org/2/library/time.html
    # for more information on what the time formats below do.

    # Display the hour as two digits
    matrix11x7.write_string(
        time.strftime("%H"),
        x=0,
        y=0,
        font=font5x5)

    # Display the minute as two digits
    matrix11x7.write_string(
        time.strftime("%M"),
        x=0,
        y=6,
        font=font5x5)

    # Display the second as two digits
    matrix11x7.write_string(
        time.strftime("%S"),
        x=0,
        y=12,
        font=font5x5)

    matrix11x7.show()
    time.sleep(0.1)
