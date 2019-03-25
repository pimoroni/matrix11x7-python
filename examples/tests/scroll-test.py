#!/usr/bin/env python

import time

from matrix11x7 import Matrix11x7

matrix11x7 = Matrix11x7()

matrix11x7.pixel(0, 0, 0.5)

try:
    while True:
        matrix11x7.scroll(1, 1)
        matrix11x7.show()
        time.sleep(0.1)

except KeyboardInterrupt:
    matrix11x7.fill(0)
    matrix11x7.show()
