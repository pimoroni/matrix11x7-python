#!/usr/bin/env python

import matrix11x7

try:
    while True:
        for x in range(18):
            matrix11x7.fill(0.1, 0, 0, x, 7)
            matrix11x7.show()
        for x in range(18):
            matrix11x7.fill(0, 0, 0, x, 7)
            matrix11x7.show()

except KeyboardInterrupt:
    matrix11x7.fill(0)
    matrix11x7.show()
