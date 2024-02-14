"""
Test for Jump instructions
"""
from computer.data_types import Bits, Data16
from computer.instructions.jump import Jump
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

    assert program_counter.value == tuple(d)
