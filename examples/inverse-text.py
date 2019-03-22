#!/usr/bin/env python

import signal

import matrix11x7
from matrix11x7.fonts import font3x5

matrix11x7.set_brightness(0.3)

matrix11x7.fill(1, 0, 0, 17, 7)

matrix11x7.write_string("Ahoy!", y=1, font=font3x5, brightness=0)

matrix11x7.show()

signal.pause()
