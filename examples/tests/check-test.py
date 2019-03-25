#!/usr/bin/env python

import time
import math

from matrix11x7 import Matrix11x7

matrix11x7 = Matrix11x7()

speed_factor = 10

try:
    while True:
        scale = (math.sin(time.time() * speed_factor) + 1) / 2
        offset = 0
        for x in range(matrix11x7.width):
            for y in range(matrix11x7.height):
                offset += 1
                color = 0.25 * scale * (offset % 2)
                matrix11x7.pixel(x, y, color)

        matrix11x7.show()

except KeyboardInterrupt:
    matrix11x7.fill(0)
