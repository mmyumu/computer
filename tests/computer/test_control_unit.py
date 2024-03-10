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


# pylint: disable=C0116,W0212,R0801

@pytest.fixture(name="control_unit")
def fixture_control_unit(registers: Registers, memory: Memory, program_counter: ProgramCounter):
    return ControlUnit(registers, memory, program_counter)


def test_nop(control_unit: ControlUnit, registers: Registers):
    opcode = Bits(0, 0, 0, 0, 0, 0, 0, 0)

    reg1 = Bits(0, 1, 0)
    reg2 = Bits(1, 0, 0)

    registers.write(reg1, Bits(0, 0, 0, 0, 0, 0, 1, 0))
    registers.write(reg2, Bits(0, 0, 0, 1, 0, 0, 1, 0))

    registers.clock_tick(True)

    operand = Bits(reg1 + reg2 + [0] * 8)
    control_unit.execute(opcode, operand)

    registers.clock_tick(True)

    assert registers.read(reg1) == [0, 0, 0, 0, 0, 0, 1, 0]
    assert registers.read(reg2) == [0, 0, 0, 1, 0, 0, 1, 0]
    assert registers.cf is False
    assert registers.zf is False


def test_jump(control_unit: ControlUnit, program_counter: ProgramCounter):
    program_counter.set(Bits([0] * 8))
    program_counter.clock_tick(True)

    opcode = Bits(0, 0, 0, 0, 0, 0, 0, 1)

    operand = Bits([0] * 3 + [0] * 3 +  [1, 0, 0, 1, 0, 0, 1, 0])
    control_unit.execute(opcode, operand)

    program_counter.clock_tick(True)

    assert program_counter.value == [1, 0, 0, 1, 0, 0, 1, 0]

def test_jeq_zf_false(control_unit: ControlUnit, registers: Registers, program_counter: ProgramCounter):
    program_counter.set(Bits([0] * 8))
    program_counter.clock_tick(True)

    opcode = Bits(0, 0, 0, 0, 0, 0, 1, 0)

    registers.zf = False

    operand = Bits([0] * 3 + [0] * 3 +  [1, 0, 0, 1, 0, 0, 1, 0])
    control_unit.execute(opcode, operand)

    program_counter.clock_tick(True)

    assert program_counter.value == [0, 0, 0, 0, 0, 0, 0, 0]

def test_jeq_zf_true(control_unit: ControlUnit, registers: Registers, program_counter: ProgramCounter):
    program_counter.set(Bits([0] * 8))
    program_counter.clock_tick(True)

    opcode = Bits(0, 0, 0, 0, 0, 0, 1, 0)

    registers.zf = True

    operand = Bits([0] * 3 + [0] * 3 +  [1, 0, 0, 1, 0, 0, 1, 0])
    control_unit.execute(opcode, operand)

    program_counter.clock_tick(True)

    assert program_counter.value == [1, 0, 0, 1, 0, 0, 1, 0]

def test_jlt_cf_false(control_unit: ControlUnit, registers: Registers, program_counter: ProgramCounter):
    program_counter.set(Bits([0] * 8))
    program_counter.clock_tick(True)

    opcode = Bits(0, 0, 0, 0, 0, 0, 1, 1)

    registers.cf = False

    operand = Bits([0] * 3 + [0] * 3 +  [1, 0, 0, 1, 0, 0, 1, 0])
    control_unit.execute(opcode, operand)

    program_counter.clock_tick(True)

    assert program_counter.value == [1, 0, 0, 1, 0, 0, 1, 0]

def test_jlt_cf_true(control_unit: ControlUnit, registers: Registers, program_counter: ProgramCounter):
    program_counter.set(Bits([0] * 8))
    program_counter.clock_tick(True)

    opcode = Bits(0, 0, 0, 0, 0, 0, 1, 1)

    registers.cf = True

    operand = Bits([0] * 3 + [0] * 3 +  [1, 0, 0, 1, 0, 0, 1, 0])
    control_unit.execute(opcode, operand)

    program_counter.clock_tick(True)

    assert program_counter.value == [0, 0, 0, 0, 0, 0, 0, 0]

def test_jge_cf_false_zf_false(control_unit: ControlUnit, registers: Registers, program_counter: ProgramCounter):
    program_counter.set(Bits([0] * 8))
    program_counter.clock_tick(True)

    opcode = Bits(0, 0, 0, 0, 0, 1, 0, 0)

    registers.cf = False
    registers.zf = False

    operand = Bits([0] * 3 + [0] * 3 +  [1, 0, 0, 1, 0, 0, 1, 0])
    control_unit.execute(opcode, operand)

    program_counter.clock_tick(True)

    assert program_counter.value == [0, 0, 0, 0, 0, 0, 0, 0]

def test_jge_cf_false_zf_true(control_unit: ControlUnit, registers: Registers, program_counter: ProgramCounter):
    program_counter.set(Bits([0] * 8))
    program_counter.clock_tick(True)

    opcode = Bits(0, 0, 0, 0, 0, 1, 0, 0)

    registers.cf = False
    registers.zf = True

    operand = Bits([0] * 3 + [0] * 3 +  [1, 0, 0, 1, 0, 0, 1, 0])
    control_unit.execute(opcode, operand)

    program_counter.clock_tick(True)

    assert program_counter.value == [1, 0, 0, 1, 0, 0, 1, 0]

def test_jge_cf_true_zf_false(control_unit: ControlUnit, registers: Registers, program_counter: ProgramCounter):
    program_counter.set(Bits([0] * 8))
    program_counter.clock_tick(True)

    opcode = Bits(0, 0, 0, 0, 0, 1, 0, 0)

    registers.cf = True
    registers.zf = False

    operand = Bits([0] * 3 + [0] * 3 +  [1, 0, 0, 1, 0, 0, 1, 0])
    control_unit.execute(opcode, operand)

    program_counter.clock_tick(True)

    assert program_counter.value == [1, 0, 0, 1, 0, 0, 1, 0]

def test_jge_cf_true_zf_true(control_unit: ControlUnit, registers: Registers, program_counter: ProgramCounter):
    program_counter.set(Bits([0] * 8))
    program_counter.clock_tick(True)

    opcode = Bits(0, 0, 0, 0, 0, 1, 0, 0)

    registers.cf = True
    registers.zf = True

    operand = Bits([0] * 3 + [0] * 3 +  [1, 0, 0, 1, 0, 0, 1, 0])
    control_unit.execute(opcode, operand)

    program_counter.clock_tick(True)

    assert program_counter.value == [1, 0, 0, 1, 0, 0, 1, 0]

def test_load_mem(control_unit: ControlUnit, registers: Registers, memory: Memory):
    memory_address = Bits(1, 1, 0, 0, 1, 1, 0, 0)
    memory_value = Bits(1, 1, 1, 0, 0, 0, 1, 1)
    memory.write(memory_address, memory_value)
    memory.clock_tick(True)

    opcode = Bits(0, 0, 0, 0, 0, 1, 0, 1)

    operand = Bits([1, 0, 1] + [0] * 3 +  memory_address)
    control_unit.execute(opcode, operand)

    registers.clock_tick(True)

    assert registers.read(Bits(1, 0, 1)) == memory_value

def test_load_imd(control_unit: ControlUnit, registers: Registers):
    opcode = Bits(0, 0, 0, 0, 0, 1, 1, 0)

    operand = Bits([1, 0, 1] + [0] * 3 +  [1, 0, 1, 1, 1, 1, 0, 1])
    control_unit.execute(opcode, operand)

    registers.clock_tick(True)

    assert registers.read(Bits(1, 0, 1)) == [1, 0, 1, 1, 1, 1, 0, 1]

def test_load_reg(control_unit: ControlUnit, registers: Registers, memory: Memory):
    memory_address = Bits(0, 0, 1, 1, 0, 0, 1, 1)
    memory_value = Bits(1, 0, 0, 1, 0, 0, 1, 0)
    memory.write(memory_address, memory_value)
    memory.clock_tick(True)

    reg_address = Bits(0, 1, 0)
    reg_value = memory_address
    registers.write(reg_address, reg_value)

    registers.clock_tick(True)

    opcode = Bits(0, 0, 0, 0, 0, 1, 1, 1)

    operand = Bits([1, 0, 1] + reg_address +  [0] * 8)
    control_unit.execute(opcode, operand)

    registers.clock_tick(True)

    assert registers.read(Bits(1, 0, 1)) == memory_value

def test_store_mem(control_unit: ControlUnit, registers: Registers, memory: Memory):
    reg_address = Bits(1, 0, 1)
    reg_value = Bits(1, 1, 0, 0, 1, 1, 1, 0)
    registers.write(reg_address, reg_value)
    registers.clock_tick(True)

    memory_address = Bits(0, 0, 1, 1, 0, 1, 0, 1)

    opcode = Bits(0, 0, 0, 0, 1, 0, 0, 0)

    operand = Bits(reg_address + [0] * 3 +  memory_address)
    control_unit.execute(opcode, operand)

    memory.clock_tick(True)

    assert memory.read(memory_address) == reg_value

def test_store_reg(control_unit: ControlUnit, registers: Registers, memory: Memory):
    reg_address_a = Bits(1, 0, 1)
    reg_address_b = Bits(0, 1, 0)
    reg_value_a = Bits(1, 1, 0, 0, 1, 1, 1, 0)
    reg_value_b = Bits(0, 0, 0, 1, 1, 0, 0, 0)
    registers.write(reg_address_a, reg_value_a)
    registers.write(reg_address_b, reg_value_b)
    registers.clock_tick(True)

    opcode = Bits(0, 0, 0, 0, 1, 0, 0, 1)

    operand = Bits(reg_address_a + reg_address_b +  [0] * 8)
    control_unit.execute(opcode, operand)

    memory.clock_tick(True)

    assert memory.read(reg_value_b) == reg_value_a

def test_tran(control_unit: ControlUnit, registers: Registers):
    reg_address_a = Bits(1, 0, 1)
    reg_address_b = Bits(0, 1, 0)
    reg_value_a = Bits(1, 1, 0, 0, 1, 1, 1, 0)
    reg_value_b = Bits(0, 0, 0, 1, 1, 0, 0, 0)
    registers.write(reg_address_a, reg_value_a)
    registers.write(reg_address_b, reg_value_b)
    registers.clock_tick(True)

    opcode = Bits(0, 0, 0, 0, 1, 0, 1, 0)

    operand = Bits(reg_address_a + reg_address_b +  [0] * 8)
    control_unit.execute(opcode, operand)

    registers.clock_tick(True)

    assert registers.read(reg_address_b) == reg_value_a

def test_clc(control_unit: ControlUnit, registers: Registers):
    registers.cf = True

    opcode = Bits(0, 0, 0, 0, 1, 0, 1, 1)

    operand = Bits([0] * 3 + [0] * 3 +  [0] * 8)
    control_unit.execute(opcode, operand)

    registers.clock_tick(True)

    assert registers.cf is False

def test_stc(control_unit: ControlUnit, registers: Registers):
    registers.cf = False

    opcode = Bits(0, 0, 0, 0, 1, 1, 0, 0)

    operand = Bits([0] * 3 + [0] * 3 +  [0] * 8)
    control_unit.execute(opcode, operand)

    registers.clock_tick(True)

    assert registers.cf is True

def test_wrong_opcode_size(control_unit: ControlUnit):
    opcode = Bits([0] * 6)

    operand = Bits([0] * 14)

    with pytest.raises(ValueError):
        control_unit.execute(opcode, operand)

def test_wrong_operand_size(control_unit: ControlUnit):
    opcode = Bits([0] * 8)

    operand = Bits([0] * 13)

    with pytest.raises(ValueError):
        control_unit.execute(opcode, operand)
