"""
Test for Registers
"""
from computer.data_types import Bits
from computer.registers import Registers


# pylint: disable=C0116,C2801

def test_registers_read(registers: Registers):
    a = Bits(0, 0, 0)
    registers.read(a)


def test_registers_write(registers: Registers):
    a = Bits(0, 0, 0)
    d = Bits([1] * 8)
    registers.write(a, d)

def test_registers_str(registers: Registers):
    registers.__str__()
