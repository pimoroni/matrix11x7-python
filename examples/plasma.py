#!/usr/bin/env python

import time
import math

from matrix11x7 import Matrix11x7
matrix11x7 = Matrix11x7()

print("""
Matrix 11x7: Plasma

Displays a basic demo-scene style pattern.

Press Ctrl+C to exit!

""")

i = 0

while True:
    i += 2
    s = math.sin(i / 50.0) * 2.0 + 6.0

    for x in range(0, 17):
        for y in range(0, 7):
            v = 0.3 + (0.3 * math.sin((x * s) + i / 4.0) * math.cos((y * s) + i / 4.0))

            matrix11x7.pixel(x, y, v)

    time.sleep(0.01)
    matrix11x7.show()
