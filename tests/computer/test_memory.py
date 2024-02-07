"""
Test for Memory
"""
import pytest
from computer.data_types import Address2, Data4

from computer.memory import Memory


# pylint: disable=C0116,W0212

@pytest.fixture(name="memory")
def fixture_memory():
    return Memory()


def test_write_read(memory: Memory):
    memory.reset()
    memory.clock_tick(True)

    a = Address2(0, 0)
    d = Data4(1, 1, 1, 1)

    bits = memory.read(a)
    assert bits == (0, 0, 0, 0)

    memory.write(a, d)
    memory.clock_tick(True)
    bits = memory.read(a)
    assert bits == (1, 1, 1, 1)
