"""
Test for Jump instructions
"""
from computer.data_types import Bits, Data16
from computer.instructions.jump import JEQ, JGE, JLT, Jump
from computer.memory import SRAM
from computer.program_counter import ProgramCounter
from computer.registers import Registers



# pylint: disable=C0116
def test_jump(registers: Registers, sram: SRAM, program_counter: ProgramCounter):
    sram.reset()
    registers.reset()

    d = Data16([1] * 4 + [0] * 4)
    jump = Jump(registers, sram, program_counter)
    operand = Bits([0] * 6 + d)
    jump(operand)
    program_counter.clock_tick(True)

    assert program_counter.value == d

def test_jeq_zf_false(registers: Registers, sram: SRAM, program_counter: ProgramCounter):
    sram.reset()
    registers.reset()

    registers.zf = False

    initial_pc_address = Bits(0, 0, 0, 0, 1, 1, 1, 1)
    program_counter.set(initial_pc_address)
    program_counter.clock_tick(True)

    new_pc_address = Bits(0, 1, 0, 1, 0, 1, 0, 1)
    operand = Bits([0] * 6 + new_pc_address)

    jump = JEQ(registers, sram, program_counter)
    operand = Bits([0] * 6 + new_pc_address)
    jump(operand)
    program_counter.clock_tick(True)

    assert program_counter.value == initial_pc_address

def test_jeq_zf_true(registers: Registers, sram: SRAM, program_counter: ProgramCounter):
    sram.reset()
    registers.reset()

    registers.zf = True

    initial_pc_address = Bits(0, 0, 0, 0, 1, 1, 1, 1)
    program_counter.set(initial_pc_address)
    program_counter.clock_tick(True)

    new_pc_address = Bits(0, 1, 0, 1, 0, 1, 0, 1)
    operand = Bits([0] * 6 + new_pc_address)

    jump = JEQ(registers, sram, program_counter)
    operand = Bits([0] * 6 + new_pc_address)
    jump(operand)
    program_counter.clock_tick(True)

    assert program_counter.value == new_pc_address

def test_jlt_cf_false(registers: Registers, sram: SRAM, program_counter: ProgramCounter):
    sram.reset()
    registers.reset()

    registers.cf = False

    initial_pc_address = Bits(0, 0, 0, 0, 1, 1, 1, 1)
    program_counter.set(initial_pc_address)
    program_counter.clock_tick(True)

    new_pc_address = Bits(0, 1, 0, 1, 0, 1, 0, 1)
    operand = Bits([0] * 6 + new_pc_address)

    jump = JLT(registers, sram, program_counter)
    operand = Bits([0] * 6 + new_pc_address)
    jump(operand)
    program_counter.clock_tick(True)

    assert program_counter.value == new_pc_address

def test_jlt_cf_true(registers: Registers, sram: SRAM, program_counter: ProgramCounter):
    sram.reset()
    registers.reset()

    registers.cf = True

    initial_pc_address = Bits(0, 0, 0, 0, 1, 1, 1, 1)
    program_counter.set(initial_pc_address)
    program_counter.clock_tick(True)

    new_pc_address = Bits(0, 1, 0, 1, 0, 1, 0, 1)
    operand = Bits([0] * 6 + new_pc_address)

    jump = JLT(registers, sram, program_counter)
    operand = Bits([0] * 6 + new_pc_address)
    jump(operand)
    program_counter.clock_tick(True)

    assert program_counter.value == initial_pc_address

def test_jge_cf_false_zf_false(registers: Registers, sram: SRAM, program_counter: ProgramCounter):
    sram.reset()
    registers.reset()

    registers.cf = False
    registers.zf = False

    initial_pc_address = Bits(0, 0, 0, 0, 1, 1, 1, 1)
    program_counter.set(initial_pc_address)
    program_counter.clock_tick(True)

    new_pc_address = Bits(0, 1, 0, 1, 0, 1, 0, 1)
    operand = Bits([0] * 6 + new_pc_address)

    jump = JGE(registers, sram, program_counter)
    operand = Bits([0] * 6 + new_pc_address)
    jump(operand)
    program_counter.clock_tick(True)

    assert program_counter.value == initial_pc_address

def test_jge_cf_false_zf_true(registers: Registers, sram: SRAM, program_counter: ProgramCounter):
    sram.reset()
    registers.reset()

    registers.cf = False
    registers.zf = True

    initial_pc_address = Bits(0, 0, 0, 0, 1, 1, 1, 1)
    program_counter.set(initial_pc_address)
    program_counter.clock_tick(True)

    new_pc_address = Bits(0, 1, 0, 1, 0, 1, 0, 1)
    operand = Bits([0] * 6 + new_pc_address)

    jump = JGE(registers, sram, program_counter)
    operand = Bits([0] * 6 + new_pc_address)
    jump(operand)
    program_counter.clock_tick(True)

    assert program_counter.value == new_pc_address

def test_jge_cf_true_zf_false(registers: Registers, sram: SRAM, program_counter: ProgramCounter):
    sram.reset()
    registers.reset()

    registers.cf = True
    registers.zf = False

    initial_pc_address = Bits(0, 0, 0, 0, 1, 1, 1, 1)
    program_counter.set(initial_pc_address)
    program_counter.clock_tick(True)

    new_pc_address = Bits(0, 1, 0, 1, 0, 1, 0, 1)
    operand = Bits([0] * 6 + new_pc_address)

    jump = JGE(registers, sram, program_counter)
    operand = Bits([0] * 6 + new_pc_address)
    jump(operand)
    program_counter.clock_tick(True)

    assert program_counter.value == new_pc_address

def test_jge_cf_true_zf_true(registers: Registers, sram: SRAM, program_counter: ProgramCounter):
    sram.reset()
    registers.reset()

    registers.cf = True
    registers.zf = True

    initial_pc_address = Bits(0, 0, 0, 0, 1, 1, 1, 1)
    program_counter.set(initial_pc_address)
    program_counter.clock_tick(True)

    new_pc_address = Bits(0, 1, 0, 1, 0, 1, 0, 1)
    operand = Bits([0] * 6 + new_pc_address)

    jump = JGE(registers, sram, program_counter)
    operand = Bits([0] * 6 + new_pc_address)
    jump(operand)
    program_counter.clock_tick(True)

    assert program_counter.value == new_pc_address
