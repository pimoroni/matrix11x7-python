# noqa D100
import sys
import mock
import pytest


def _setup():
    global matrix11x7
    smbus = mock.Mock()
    smbus.SMBus = mock.Mock()
    sys.modules['smbus'] = smbus
    from matrix11x7 import Matrix11x7
    matrix11x7 = Matrix11x7()


def test_set_pixel():
    _setup()
    matrix11x7.set_pixel(0, 0, 1.0)
    with pytest.raises(ValueError):
        matrix11x7.set_pixel(0, 0, 2.0)
