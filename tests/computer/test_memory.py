"""
Test for Memory
"""
import pytest
from computer.data_types import Address8, Data16

from computer.memory import SRAM


# pylint: disable=C0116,W0212

@pytest.fixture(name="sram8")
def fixture_memory8():
    return SRAM(size=8)

@pytest.fixture(name="sram16", scope="module")
def fixture_memory16():
    return SRAM(size=16, cheating_optim=True)


def test_read_performance_8bits(sram8: SRAM):
    a = Address8(*[0] * 8)
    sram8.read(a)

def test_write_performance_8bits(sram8: SRAM):
    a = Address8(*[0] * 8)
    d = Data16(1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1)
    sram8.write(a, d)

def test_write_read_8bits(sram8: SRAM):
    sram8.reset()
    sram8.clock_tick(True)

    a = Address8(*[0] * 8)
    d = Data16(1, 1, 1, 1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1)

    bits = sram8.read(a)
    assert bits == (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)

    sram8.write(a, d)
    sram8.clock_tick(True)
    bits = sram8.read(a)
    assert bits == (1, 1, 1, 1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1)

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
