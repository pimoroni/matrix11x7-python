#!/usr/bin/env python

import time
import matrix11x7

DELAY = 0.0001

try:
    while True:
        for x in range(255):
            matrix11x7.fill(x / 255.0, 0, 0, 17, 7)
            matrix11x7.show()
            time.sleep(DELAY)
        for x in reversed(range(255)):
            matrix11x7.fill(x / 255.0, 0, 0, 17, 7)
            matrix11x7.show()
            time.sleep(DELAY)

except KeyboardInterrupt:
    matrix11x7.fill(0)
    matrix11x7.show()
