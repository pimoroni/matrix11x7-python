#!/usr/bin/env python

import sys
import time

try:
    import psutil
except ImportError:
    sys.exit("This script requires the psutil module\nInstall with: sudo pip install psutil")

from matrix11x7 import Matrix11x7

print("""
Matrix 11x7: CPU

Displays a graph with CPU values.

Press Ctrl+C to exit!

""")

matrix11x7 = Matrix11x7()

# Avoid retina-searage!
matrix11x7.set_brightness(0.5)

i = 0

cpu_values = [0] * matrix11x7.width

# Uncomment the below if your display is upside down
# (e.g. if you're using it in a Pimoroni Scroll Bot)
# matrix11x7.rotate(degrees=180)

while True:
    try:
        cpu_values.pop(0)
        cpu_values.append(psutil.cpu_percent())

        matrix11x7.set_graph(cpu_values, low=0, high=25)

        matrix11x7.show()
        time.sleep(0.2)
    except KeyboardInterrupt:
        matrix11x7.clear()
        sys.exit(-1)
