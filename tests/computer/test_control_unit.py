"""
Test for ALU.
The tests are done with a light memory configuration: 
 - 2**8 bits RAM
 - 2**3 bits registers
 - 2**3 bits for each register
"""
import pytest

from computer.control_unit import ControlUnit
from computer.data_types import Bits
from computer.memory import Memory
from computer.program_counter import ProgramCounter
from computer.registers import Registers


# pylint: disable=C0116,W0212

@pytest.fixture(name="control_unit")
def fixture_control_unit(registers: Registers, memory: Memory, program_counter: ProgramCounter):
    return ControlUnit(registers, memory, program_counter)


def test_nop(control_unit: ControlUnit, registers: Registers):
    opcode = Bits(0, 0, 0, 0, 0, 0, 0)

    reg1 = Bits(0, 1, 0)
    reg2 = Bits(1, 0, 0)

    registers.write(reg1, Bits(0, 0, 0, 0, 0, 0, 1, 0))
    registers.write(reg2, Bits(0, 0, 0, 1, 0, 0, 1, 0))

    registers.clock_tick(True)

    operand = Bits(reg1 + reg2 + [0] * 8)
    control_unit.execute_instruction(opcode, operand)

    registers.clock_tick(True)

    assert registers.read(reg1) == [0, 0, 0, 0, 0, 0, 1, 0]
    assert registers.read(reg2) == [0, 0, 0, 1, 0, 0, 1, 0]
    assert registers.cf is False
    assert registers.zf is False


def test_jump(control_unit: ControlUnit, program_counter: ProgramCounter):
    opcode = Bits(0, 0, 0, 0, 0, 0, 1)

    operand = Bits([0] * 3 + [0] * 3 +  [1, 0, 0, 1, 0, 0, 1, 0])
    control_unit.execute_instruction(opcode, operand)

    program_counter.clock_tick(True)

    assert program_counter.value == [1, 0, 0, 1, 0, 0, 1, 0]


def test_jeq(control_unit: ControlUnit, registers: Registers, program_counter: ProgramCounter):
    opcode = Bits(0, 0, 0, 0, 0, 1, 0)

    registers.zf = True

    operand = Bits([0] * 3 + [0] * 3 +  [1, 0, 0, 1, 0, 0, 1, 0])
    control_unit.execute_instruction(opcode, operand)

    program_counter.clock_tick(True)

    assert program_counter.value == [1, 0, 0, 1, 0, 0, 1, 0]
