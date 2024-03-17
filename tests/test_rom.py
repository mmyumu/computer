"""
Test for ROM
"""
import pytest
from computer.data_types import Bits
from computer.rom import ROM
from program.program import BinaryProgram


# pylint: disable=C0116,W0212,C2801

@pytest.fixture(name="rom")
def fixture_rom():
    return ROM(size=8, register_size=8)

def test_set(rom: ROM):
    program = BinaryProgram()
    program.append(Bits(0, 0, 0, 0, 0, 0, 0, 1))
    program.append(Bits(0, 0, 0, 0, 0, 0, 1, 0))
    program.append(Bits(0, 0, 0, 0, 0, 0, 1, 1))
    program.append(Bits(0, 0, 0, 0, 0, 1, 0, 0))
    program.append(Bits(0, 0, 0, 0, 0, 1, 0, 1))
    program.append(Bits(0, 0, 0, 0, 0, 1, 1, 0))
    program.append(Bits(0, 0, 0, 0, 0, 1, 1, 1))

    rom.set(program)

def test_read(rom: ROM):
    program = BinaryProgram()
    program.append(Bits(0, 0, 0, 0, 0, 0, 0, 1))
    program.append(Bits(0, 0, 0, 0, 0, 0, 1, 0))
    program.append(Bits(0, 0, 0, 0, 0, 0, 1, 1))
    program.append(Bits(0, 0, 0, 0, 0, 1, 0, 0))
    program.append(Bits(0, 0, 0, 0, 0, 1, 0, 1))
    program.append(Bits(0, 0, 0, 0, 0, 1, 1, 0))
    program.append(Bits(0, 0, 0, 0, 0, 1, 1, 1))

    rom.set(program)
    rom.clock_tick(True)

    assert rom.read(Bits(3, size=3)) == [0, 0, 0, 0, 0, 1, 0, 0]
