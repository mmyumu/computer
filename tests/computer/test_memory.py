"""
Test for Memory
"""
import pytest
from computer.data_types import Bits

from computer.memory import SRAM


# pylint: disable=C0116,W0212,C2801

@pytest.fixture(name="sram8")
def fixture_memory8():
    return SRAM(size=8)

def test_wrong_size():
    with pytest.raises(ValueError):
        SRAM(size=3)
    with pytest.raises(ValueError):
        SRAM(size=7)
    with pytest.raises(ValueError):
        SRAM(size=23)

def test_write_read_no_cheat():
    sram = SRAM(size=8, cheating_optim=False)

    sram.reset()
    sram.clock_tick(True)

    a = Bits([0] * 8)
    d = Bits(1, 1, 1, 1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1)

    bits = sram.read(a)
    assert bits == [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

    sram.write(a, d)
    sram.clock_tick(True)
    bits = sram.read(a)
    assert bits == [1, 1, 1, 1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1]

def test_str(sram8: SRAM):
    sram8.__str__()

def test_read_performance_8bits(sram8: SRAM):
    a = Bits([0] * 8)
    sram8.read(a)

def test_write_performance_8bits(sram8: SRAM):
    a = Bits([0] * 8)
    d = Bits(1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1)
    sram8.write(a, d)

def test_write_read_8bits(sram8: SRAM):
    sram8.reset()
    sram8.clock_tick(True)

    a = Bits([0] * 8)
    d = Bits(1, 1, 1, 1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1)

    bits = sram8.read(a)
    assert bits == [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

    sram8.write(a, d)
    sram8.clock_tick(True)
    bits = sram8.read(a)
    assert bits == [1, 1, 1, 1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1]

# def test_read_performance_16bits(sram16: SRAM):
#     a = Address16(*[0] * 16)

#     for i in range(16):
#         a[i] = 1
#         sram16.read(a)

# def test_write_performance_16bits(sram16: SRAM):
#     a = Address16(*[0] * 16)
#     d = Data16(1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1)
#     sram16.write(a, d)

# def test_write_read_16bits(sram16: SRAM):
#     sram16.reset()
#     sram16.clock_tick(True)

#     a = Address16(*[0] * 16)
#     d = Data16(1, 1, 1, 1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1)

#     bits = sram16.read(a)
#     assert bits == (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)

#     sram16.write(a, d)
#     sram16.clock_tick(True)
#     bits = sram16.read(a)
#     assert bits == (1, 1, 1, 1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1)
