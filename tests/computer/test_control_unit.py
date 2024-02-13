"""
Test for ALU.
The tests are done with a light memory configuration: 
 - 2**8 bits RAM
 - 2**3 bits registers
 - 2**3 bits for each register
"""
import pytest

from computer.control_unit import ControlUnit
from computer.data_types import Bits, Opcode8
from computer.memory import Memory
from computer.program_counter import ProgramCounter
from computer.registers import Registers


# pylint: disable=C0116,W0212

@pytest.fixture(name="control_unit")
def fixture_alu(registers: Registers, memory: Memory, program_counter: ProgramCounter):
    return ControlUnit(registers, memory, program_counter)


def test_control_unit_nop(control_unit: ControlUnit):
    opcode = Opcode8(0b0)
    operand = Bits([0] * 14)
    control_unit.execute(opcode, operand)


def test_control_unit_load_mem(control_unit: ControlUnit):
    opcode = Opcode8(0b1)
    operand = Bits([0] * 14)
    control_unit.execute(opcode, operand)


def test_control_unit_load_imd(control_unit: ControlUnit):
    opcode = Opcode8(0b10)
    operand = Bits([0] * 14)
    control_unit.execute(opcode, operand)
