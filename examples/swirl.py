#!/usr/bin/env python

import time
import math

from matrix11x7 import Matrix11x7

matrix11x7 = Matrix11x7()

# Avoid retina-searage!
matrix11x7.set_brightness(0.5)

print("""
Matrix 11x7: Swirl

Displays a basic demo-scene style pattern.

Press Ctrl+C to exit!

""")


def swirl(x, y, step):
    x -= (matrix11x7.width / 2.0)
    y -= (matrix11x7.height / 2.0)

    dist = math.sqrt(pow(x, 2) + pow(y, 2))

    angle = (step / 10.0) + dist / 1.5

    s = math.sin(angle)
    c = math.cos(angle)

    xs = x * c - y * s
    ys = x * s + y * c

    r = abs(xs + ys)

    return max(0.0, 0.7 - min(1.0, r / 8.0))


matrix11x7.set_brightness(0.8)

while True:
    timestep = math.sin(time.time() / 18) * 1500

    for x in range(0, matrix11x7.width):
        for y in range(0, matrix11x7.height):
            v = swirl(x, y, timestep)
            matrix11x7.pixel(x, y, v)

    time.sleep(0.001)
    matrix11x7.show()
