"""
Test for Tran instructions
"""
from computer.data_types import Bits
from computer.instructions.tran import Tran
from computer.memory import SRAM
from computer.program_counter import ProgramCounter
from computer.registers import Registers



# pylint: disable=C0116
def test_tran(registers: Registers, sram: SRAM, program_counter: ProgramCounter):
    sram.reset()
    registers.reset()

    reg1 = Bits(0, 0, 1)
    reg2 = Bits(0, 1, 1)

    d = Bits(1, 1, 1, 0, 0, 0, 1, 1)
    registers.write(reg1, d)
    registers.clock_tick(True)

    operand = Bits(reg1 + reg2 + [0] * 8)
    tran = Tran(registers, sram, program_counter)
    tran(operand)
    registers.clock_tick(True)

    assert registers.read(reg2) == d
