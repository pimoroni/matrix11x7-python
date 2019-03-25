# noqa D100
import sys
import mock


def test_setup():
    """Test against fake device information stored in hardware mock."""
    smbus = mock.Mock()
    smbus.SMBus = mock.Mock()
    sys.modules['smbus'] = smbus
    from matrix11x7 import Matrix11x7

    matrix11x7 = Matrix11x7()

    del matrix11x7
