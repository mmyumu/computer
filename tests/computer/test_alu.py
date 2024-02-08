"""
Test for ALU
"""
import pytest

from computer.alu import ALU
from computer.data_types import Opcode8, Operand24


# pylint: disable=C0116,W0212

@pytest.fixture(name="alu")
def fixture_alu():
    return ALU()


def test_alu_nop(alu: ALU):
    opcode = Opcode8(0b0)
    operand = Operand24(0b0)
    alu.execute(opcode, operand)


def test_alu_load_mem(alu: ALU):
    opcode = Opcode8(0b1)
    operand = Operand24(0b0)
    alu.execute(opcode, operand)


def test_alu_load_imd(alu: ALU):
    opcode = Opcode8(0b10)
    operand = Operand24(0b0)
    alu.execute(opcode, operand)
