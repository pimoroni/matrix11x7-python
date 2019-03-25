#!/usr/bin/env python

import time

from matrix11x7 import Matrix11x7

print("""
Matrix 11x7: Hello World

Scrolls "Hello World" across the screen
using the default 5x7 pixel large font.

Press Ctrl+C to exit!

""")

matrix11x7 = Matrix11x7()

# Uncomment the below if your display is upside down
# (e.g. if you're using it in a Pimoroni Scroll Bot)
# matrix11x7.rotate(degrees=180)

# Write the "Hello World!" string in the buffer and
# set a more eye-friendly default brightness
matrix11x7.write_string(" Hello World!", brightness=0.5)

# Auto scroll using a while + time mechanism (no thread)
while True:
    # Show the buffer
    matrix11x7.show()
    # Scroll the buffer content
    matrix11x7.scroll()
    # Wait for 0.1s
    time.sleep(0.1)
