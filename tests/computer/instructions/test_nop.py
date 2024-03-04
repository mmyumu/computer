"""
Test for flags instructions module
"""


from computer.data_types import Bits
from computer.instructions.nop import Nop
from computer.registers import Registers

# pylint: disable=C0116

def test_clc(registers: Registers):
    registers.cf = False
    registers.zf = False

    operand = Bits([0] * 14)
    nop = Nop()
    nop(operand)

    assert registers.cf is False
    assert registers.zf is False
