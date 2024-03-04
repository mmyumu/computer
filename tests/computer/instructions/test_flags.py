"""
Test for flags instructions module
"""

from computer.data_types import Bits
from computer.instructions.flags import CLC, STC
from computer.memory import SRAM
from computer.program_counter import ProgramCounter
from computer.registers import Registers

# pylint: disable=C0116

def test_clc(registers: Registers, sram: SRAM, program_counter: ProgramCounter):
    registers.cf = True

    operand = Bits([0] * 14)
    clc = CLC(registers, sram, program_counter)
    clc(operand)

    assert registers.cf is False


def test_stc(registers: Registers, sram: SRAM, program_counter: ProgramCounter):
    registers.cf = False

    operand = Bits([0] * 14)
    stc = STC(registers, sram, program_counter)
    stc(operand)

    assert registers.cf is True
