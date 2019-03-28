#!/usr/bin/env python

import time

from matrix11x7 import Matrix11x7
from matrix11x7.fonts import font5x7

print("""
Matrix 11x7: Hello World

Scrolls "Hello World" across the screen
in a 5x7 pixel large font.

Press Ctrl+C to exit!

""")

matrix11x7 = Matrix11x7()
matrix11x7.rotate(degrees=90)

# Avoid retina-searage!
matrix11x7.set_brightness(0.5)

matrix11x7.write_string("Hello World! ", x=0, y=2, font=font5x7)
matrix11x7.show()

time.sleep(0.5)

while True:
    matrix11x7.show()
    matrix11x7.scroll()
    time.sleep(0.05)
