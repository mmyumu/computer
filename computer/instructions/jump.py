"""
Jump instructions module
"""
from computer.data_types import Bits
from computer.instructions.instruction import ControlInstruction

# pylint: disable=R0903
class Jump(ControlInstruction):
    """
    Load from memory address to register class.
    LOAD REG MEM	; loads the specified memory unit into REG
    """
    def compute(self, reg1: Bits, reg2: Bits, value: Bits):
        self._program_counter.set(value)
