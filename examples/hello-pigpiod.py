#!/usr/bin/env python

import time

import pigpio
from matrix11x7 import Matrix11x7

print("""
Matrix 11x7: Hello World

Scrolls "Hello World" across the screen
using the default 5x7 pixel large font.

Press Ctrl+C to exit!

""")

matrix11x7 = Matrix11x7()


class I2C_PIGPIO():
    def __init__(self):
        self.pi = pigpio.pi()
        self.i2c_handle = self.pi.i2c_open(1, 0x74)

    def write_byte_data(self, address, register, value):
        self.pi.i2c_write_byte_data(self.i2c_handle, register, value)

    def read_byte_data(self, address, register):
        return self.pi.i2c_read_byte_data(self.i2c_handle, register)

    def write_i2c_block_data(self, address, register, values):
        self.pi.i2c_write_i2c_block_data(self.i2c_handle, register, values)


matrix11x7.setup(i2c_dev=I2C_PIGPIO())
# Uncomment the below if your display is upside down
# (e.g. if you're using it in a Pimoroni Scroll Bot)
# matrix11x7.rotate(degrees=180)

# Write the "Hello World!" string in the buffer and
# set a more eye-friendly default brightness
matrix11x7.write_string(" Hello World!", brightness=0.5)

# Auto scroll using a while + time mechanism (no thread)
while True:
    # Show the buffer
    matrix11x7.show()
    # Scroll the buffer content
    matrix11x7.scroll()
    # Wait for 0.1s
    time.sleep(0.1)
