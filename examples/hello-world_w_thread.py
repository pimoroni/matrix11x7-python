#!/usr/bin/env python

import threading

import matrix11x7


def autoscroll(interval=0.1):
    """Autoscroll with a thread (recursive function).

    Automatically show and scroll the buffer according to the interval value.

    :param interval: Amount of seconds (or fractions thereof), not zero

    """

    # Start a timer
    threading.Timer(interval, autoscroll, [interval]).start()
    # Show the buffer
    matrix11x7.show()
    # Scroll the buffer content
    matrix11x7.scroll()


print("""
Matrix 11x7: Hello World

Scrolls "Hello World" across the screen
using the default 5x7 pixel large font.

Press Ctrl+C to exit!

""")

# Uncomment the below if your display is upside down
#   (e.g. if you're using it in a Pimoroni Scroll Bot)
# matrix11x7.rotate(degrees=180)

# Write the "Hello World!" string in the buffer and
#   set a more eye-friendly default brightness
matrix11x7.write_string(" Hello World!", brightness=0.5)

# Auto scroll using a thread
autoscroll()
