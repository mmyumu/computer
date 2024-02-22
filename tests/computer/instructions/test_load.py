"""
Test for Load instructions
"""
import pytest
from computer.data_types import Bits, Data16
from computer.instructions.load import LoadImd, LoadMem, LoadReg
from computer.memory import SRAM
from computer.program_counter import ProgramCounter
from computer.registers import Registers



# pylint: disable=C0116
def test_load_mem(registers: Registers, sram: SRAM, program_counter: ProgramCounter):
    sram.reset()
    registers.reset()

    d = Data16([1] * 4 + [0] * 4)
    register_address = Bits(0, 0, 1)
    memory_address = Bits(0, 0, 0, 0, 1, 1, 1, 1)
    sram.write(memory_address, d)
    sram.clock_tick(True)

    load_mem = LoadMem(registers, sram, program_counter)
    operand = Bits(register_address + [0] * 3 + memory_address)
    load_mem(operand)
    sram.clock_tick(True)
    registers.clock_tick(True)

    assert registers.read(register_address) == d

def test_load_mem_invalid_memory_address(registers: Registers, sram: SRAM, program_counter: ProgramCounter):
    register_address = Bits(0, 0, 1)
    memory_address = Bits(0, 0, 0, 0, 1, 1, 1, 1, 1) # Too long

    load_mem = LoadMem(registers, sram, program_counter)
    operand = Bits(register_address + [0] * 3 + memory_address)

    with pytest.raises(ValueError):
        load_mem(operand)

def test_load_mem_invalid_reg1_address(registers: Registers, sram: SRAM, program_counter: ProgramCounter):
    register_address = Bits(0, 0, 1, 1) # Too long
    memory_address = Bits(0, 0, 0, 0, 1, 1, 1, 1)

    load_mem = LoadMem(registers, sram, program_counter)
    operand = Bits(register_address + [0] * 4 + memory_address)

    with pytest.raises(ValueError):
        load_mem(operand)

def test_load_imd(registers: Registers, sram: SRAM, program_counter: ProgramCounter):
    sram.reset()
    registers.reset()

    register_address = Bits(0, 0, 1)
    value = Bits(0, 0, 0, 0, 1, 1, 1, 1)

    load_imd = LoadImd(registers, sram, program_counter)
    operand = Bits(register_address + [0] * 3 + value)
    load_imd(operand)
    sram.clock_tick(True)
    registers.clock_tick(True)

    assert registers.read(register_address) == value

def test_load_imd_invalid_reg1_address(registers: Registers, sram: SRAM, program_counter: ProgramCounter):
    sram.reset()
    registers.reset()

    register_address = Bits(0, 0, 1, 1) # Too long
    value = Bits(0, 0, 0, 0, 1, 1, 1, 1)

    load_imd = LoadImd(registers, sram, program_counter)
    operand = Bits(register_address + [0] * 3 + value)
    with pytest.raises(ValueError):
        load_imd(operand)

def test_load_imd_invalid_value(registers: Registers, sram: SRAM, program_counter: ProgramCounter):
    sram.reset()
    registers.reset()

    register_address = Bits(0, 0, 1)
    value = Bits(0, 0, 0, 0, 1, 1, 1, 1, 1) # Too long

    load_imd = LoadImd(registers, sram, program_counter)
    operand = Bits(register_address + [0] * 3 + value)
    with pytest.raises(ValueError):
        load_imd(operand)

def test_load_reg(registers: Registers, sram: SRAM, program_counter: ProgramCounter):
    sram.reset()
    registers.reset()

    memory_address = Bits(1, 1, 1, 1, 0, 0, 0, 0)
    value = Bits(0, 0, 0, 0, 1, 1, 1, 1)
    sram.write(memory_address, value)
    sram.clock_tick(True)

    register_address1 = Bits(0, 0, 1)
    register_address2 = Bits(0, 1, 0)

    registers.write(register_address2, memory_address)
    registers.clock_tick(True)

    load_reg = LoadReg(registers, sram, program_counter)
    operand = Bits(register_address1 + register_address2 + [0] * 8)
    load_reg(operand)
    sram.clock_tick(True)
    registers.clock_tick(True)

    assert registers.read(register_address1) == value
    assert registers.read(register_address2) == memory_address
