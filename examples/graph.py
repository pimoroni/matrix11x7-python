#!/usr/bin/env python

import time
import random

import matrix11x7

print("""
Matrix 11x7: Graph

Displays a graph with random values.

Press Ctrl+C to exit!

""")

MIN_VALUE = 0
MAX_VALUE = 50

# Uncomment the below if your display is upside down
#   (e.g. if you're using it in a Pimoroni Scroll Bot)
# matrix11x7.rotate(degrees=180)

# Begin with a list of 17 zeros
values = [0] * matrix11x7.DISPLAY_WIDTH

while True:
    # Insert a random value at the beginning
    values.insert(0, random.randrange(MIN_VALUE, MAX_VALUE))

    # Get rid of the last value, keeping the list at 17 (DISPLAY_WIDTH) items
    values = values[:matrix11x7.DISPLAY_WIDTH]

    # Plot the random values onto Matrix 11x7
    matrix11x7.set_graph(values, low=MIN_VALUE, high=MAX_VALUE, brightness=0.3)

    matrix11x7.show()
    time.sleep(0.05)
