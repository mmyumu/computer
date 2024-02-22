"""
Jump instructions module
"""
from computer.data_types import Bits
from computer.instructions.instruction import ControlInstruction

# pylint: disable=R0903
class Jump(ControlInstruction):
    """
    Set the Program Counter to the immediate value
    JMP IMD		; sets PC to the immediate 16-bit value
    """
    def compute(self, reg1: Bits, reg2: Bits, value: Bits):
        self._program_counter.set(value)
