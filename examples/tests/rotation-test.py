#!/usr/bin/env python

import time

from matrix11x7 import Matrix11x7

matrix11x7 = Matrix11x7()

# Avoid retina-searage!
matrix11x7.set_brightness(0.5)

matrix11x7.set_pixel(0, 0, 1)
matrix11x7.set_pixel(1, 1, 1)

try:
    while True:
        for x in [0, 90, 180, 270]:
            matrix11x7.rotate(x)
            matrix11x7.show()
            time.sleep(0.1)

except KeyboardInterrupt:
    matrix11x7.fill(0)
    matrix11x7.show()
