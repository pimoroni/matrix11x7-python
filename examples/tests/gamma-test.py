#!/usr/bin/env python

import time
from matrix11x7 import Matrix11x7

matrix11x7 = Matrix11x7()

DELAY = 0.001

try:
    while True:
        for x in range(20, 48):
            matrix11x7.fill(x / 255.0, 0, 0, 11, 7)
            matrix11x7.show()
            time.sleep(DELAY)
        for x in reversed(range(20, 48)):
            matrix11x7.fill(x / 255.0, 0, 0, 11, 7)
            matrix11x7.show()
            time.sleep(DELAY)

except KeyboardInterrupt:
    matrix11x7.fill(0)
    matrix11x7.show()
