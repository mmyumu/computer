"""
Test for Store instructions
"""
from computer.data_types import Bits, Data16
from computer.instructions.store import StoreMem, StoreReg
from computer.memory import SRAM
from computer.program_counter import ProgramCounter
from computer.registers import Registers



# pylint: disable=C0116
def test_store_mem(registers: Registers, sram: SRAM, program_counter: ProgramCounter):
    sram.reset()
    registers.reset()

    d = Data16([1] * 4 + [0] * 4)
    register_address = Bits(0, 0, 1)
    registers.write(register_address, d)
    registers.clock_tick(True)

    memory_address = Bits(0, 0, 1, 1, 0, 0, 1, 1)
    operand = Bits(register_address + [0] * 3 + memory_address)

    store_mem = StoreMem(registers, sram, program_counter)
    store_mem(operand)

    sram.clock_tick(True)

    assert sram.read(memory_address) == d

def test_store_reg(registers: Registers, sram: SRAM, program_counter: ProgramCounter):
    sram.reset()
    registers.reset()

    d = Data16([1] * 4 + [0] * 4)
    register_address1 = Bits(0, 0, 1)
    register_address2 = Bits(1, 0, 0)
    memory_address = Bits(0, 0, 1, 1, 0, 0, 1, 1)
    registers.write(register_address1, d)
    registers.write(register_address2, memory_address)
    registers.clock_tick(True)

    operand = Bits(register_address1 + register_address2 + [0] * 8)

    store_reg = StoreReg(registers, sram, program_counter)
    store_reg(operand)

    sram.clock_tick(True)

    assert sram.read(memory_address) == d
