"""
Test for Memory
"""
import pytest
from computer.data_types import Address10, Data4

from computer.memory import SRAM


# pylint: disable=C0116,W0212

@pytest.fixture(name="sram")
def fixture_memory():
    return SRAM()


def test_write_read(sram: SRAM):
    sram.reset()
    sram.clock_tick(True)

    a = Address10(*[0] * 10)
    d = Data4(1, 1, 1, 1)

    bits = sram.read(a)
    assert bits == (0, 0, 0, 0)

    sram.write(a, d)
    sram.clock_tick(True)
    bits = sram.read(a)
    assert bits == (1, 1, 1, 1)
