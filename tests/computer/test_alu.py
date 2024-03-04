"""
Test for ALU.
The tests are done with a light memory configuration: 
 - 2**8 bits RAM
 - 2**3 bits registers
 - 2**3 bits for each register
"""
import pytest

from computer.alu import ALU
from computer.data_types import Bits
from computer.registers import Registers


# pylint: disable=C0116,W0212

@pytest.fixture(name="alu")
def fixture_alu(registers: Registers):
    return ALU(registers, memory_size=8)


def test_add(alu: ALU, registers: Registers):
    opcode = Bits(0, 0, 0)

    reg1 = Bits(0, 1, 0)
    reg2 = Bits(1, 0, 0)

    registers.write(reg1, Bits(0, 0, 0, 0, 0, 0, 1, 0))
    registers.write(reg2, Bits(0, 0, 0, 1, 0, 0, 1, 0))

    registers.clock_tick(True)

    operand = Bits(reg1 + reg2 + [0] * 8)
    alu.execute_instruction(opcode, operand)

    registers.clock_tick(True)

    assert registers.read(reg1) == [0, 0, 0, 1, 0, 1, 0, 0]


def test_sub(alu: ALU, registers: Registers):
    opcode = Bits(0, 0, 1)

    reg1 = Bits(0, 1, 0)
    reg2 = Bits(1, 0, 0)

    registers.write(reg1, Bits(0, 0, 0, 1, 0, 0, 1, 0))
    registers.write(reg2, Bits(0, 0, 0, 0, 0, 0, 0, 1))

    registers.clock_tick(True)

    operand = Bits(reg1 + reg2 + [0] * 8)
    alu.execute_instruction(opcode, operand)

    registers.clock_tick(True)

    assert registers.read(reg1) == [0, 0, 0, 1, 0, 0, 0, 1]
