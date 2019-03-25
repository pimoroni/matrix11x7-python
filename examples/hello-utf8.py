#!/usr/bin/env python
# -*- coding: utf-8 -*-

import time

from matrix11x7 import Matrix11x7
from matrix11x7.fonts import font5x7
from six import unichr

print("""
Matrix 11x7: Hello utf-8

Scrolls the 256 characters Matrix 11x7 supports across the screen.

Note: many otherwise useless control characters have been
replaced with symbols you might find useful!

Press Ctrl+C to exit!

""")

# Uncomment to rotate the text
# matrix11x7.rotate(180)

# Set a more eye-friendly default brightness
matrix11x7.set_brightness(0.5)

text = [unichr(x) for x in range(256)]

text = u"{}        ".format(u"".join(text))

matrix11x7.write_string(text, x=0, y=0, font=font5x7, brightness=0.5)

while True:
    matrix11x7.show()
    matrix11x7.scroll()
    time.sleep(0.05)
