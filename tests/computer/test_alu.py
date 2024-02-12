"""
Test for ALU.
The tests are done with a light memory configuration: 
 - 2**8 bits RAM
 - 2**3 bits registers
 - 2**3 bits for each register
"""
import pytest

from computer.alu import ALU
from computer.data_types import Bits, Opcode8


# pylint: disable=C0116,W0212

@pytest.fixture(name="alu")
def fixture_alu():
    return ALU(memory_size=8, registers_size=3, register_size=3)


def test_alu_nop(alu: ALU):
    opcode = Opcode8(0b0)
    operand = Bits([0] * 14)
    alu.execute(opcode, operand)


def test_alu_load_mem(alu: ALU):
    opcode = Opcode8(0b1)
    operand = Bits([0] * 14)
    alu.execute(opcode, operand)


def test_alu_load_imd(alu: ALU):
    opcode = Opcode8(0b10)
    operand = Bits([0] * 14)
    alu.execute(opcode, operand)
