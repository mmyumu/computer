"""
Test for barrel shifters
"""
import pytest
from computer.data_types import Bits

from computer.electronic.circuits.shifter import BarrelShifter


# pylint: disable=C0116,W0212

@pytest.fixture(name="barrel_shifter_right")
def fixture_barrel_shifter_right():
    return BarrelShifter(3, right=True)

@pytest.fixture(name="barrel_shifter_left")
def fixture_barrel_shifter_left():
    return BarrelShifter(3, right=False)


def test_barrel_shifter(barrel_shifter_right: BarrelShifter, barrel_shifter_left: BarrelShifter):
    for i in range(256):
        i = Bits(i, size=8)

        for s in range(8):
            s = Bits(s, size=3)

            result_right, _ = barrel_shifter_right(i, s)
            assert ((i.to_int() >> s.to_int())|(i.to_int() << (8 - s.to_int())) & 0xFF) % (2 ** 8) == result_right.to_int(), f"Inputs: i={i}, s={s}"

            result_left, _ = barrel_shifter_left(i, s)
            assert ((i.to_int() << s.to_int())|(i.to_int() >> (8 - s.to_int())) & 0xFF) % (2 ** 8) == result_left.to_int(), f"Inputs: i={i}, s={s}"
