"""
Test for Memory
"""
import pytest
from computer.data_types import Address16, Address8, Data16

from computer.memory import SRAM


# pylint: disable=C0116,W0212

@pytest.fixture(name="sram8_8")
def fixture_memory8_8():
    return SRAM(size=8)

@pytest.fixture(name="sram8_4")
def fixture_memory8_4():
    return SRAM(size=8)

@pytest.fixture(name="sram16_8", scope="module")
def fixture_memory16_8():
    return SRAM(size=16)


def test_read_performance_8_8bits(sram8_8: SRAM):
    a = Address8(*[0] * 8)
    sram8_8.read(a)

def test_write_performance_8_8bits(sram8_8: SRAM):
    a = Address8(*[0] * 8)
    d = Data16(1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1)
    sram8_8.write(a, d)

def test_write_read_8_8bits(sram8_8: SRAM):
    sram8_8.reset()
    sram8_8.clock_tick(True)

    a = Address8(*[0] * 8)
    d = Data16(1, 1, 1, 1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1)

    bits = sram8_8.read(a)
    assert bits == (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)

    sram8_8.write(a, d)
    sram8_8.clock_tick(True)
    bits = sram8_8.read(a)
    assert bits == (1, 1, 1, 1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1)

def test_read_performance_8_4bits(sram8_4: SRAM):
    a = Address8(1, 1, 1, 0, 1, 0, 1, 0)
    sram8_4.read(a)

def test_write_performance_8_4bits(sram8_4: SRAM):
    a = Address8(*[0] * 8)
    d = Data16(1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1)
    sram8_4.write(a, d)

def test_write_read_8_4bits(sram8_4: SRAM):
    sram8_4.reset()
    sram8_4.clock_tick(True)

    a = Address8(0, 1, 1, 0, 1, 0, 0, 1)
    d = Data16(1, 1, 1, 1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1)

    bits = sram8_4.read(a)
    assert bits == (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)

    sram8_4.write(a, d)
    sram8_4.clock_tick(True)
    bits = sram8_4.read(a)
    assert bits == (1, 1, 1, 1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1)

def test_read_performance16_8bits(sram16_8: SRAM):
    a = Address16(*[0] * 16)

    for i in range(16):
        a[i] = 1
        sram16_8.read(a)

def test_write_performance16_8bits(sram16_8: SRAM):
    a = Address16(*[0] * 16)
    d = Data16(1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1)
    sram16_8.write(a, d)

# def test_write_read16_8bits(sram16_8: SRAM):
#     sram16_8.reset()
#     sram16_8.clock_tick(True)

#     a = Address16(*[0] * 16)
#     d = Data16(1, 1, 1, 1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1)

#     bits = sram16_8.read(a)
#     assert bits == (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)

#     sram16_8.write(a, d)
#     sram16_8.clock_tick(True)
#     bits = sram16_8.read(a)
#     assert bits == (1, 1, 1, 1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1)
