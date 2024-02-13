"""
Jump instructions module
"""
from computer.data_types import Bits
from computer.instructions.instruction import Instruction

# pylint: disable=R0903
class Jump(Instruction):
    """
    Load from memory address to register class.
    LOAD REG MEM	; loads the specified memory unit into REG
    """
    def compute(self, reg1: Bits, reg2: Bits, value: Bits):
        data = self._memory.read(value)
        self._registers.write(reg1, data)
