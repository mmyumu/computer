"""
Load instructions module
"""
from computer.data_types import Bits
from computer.instructions.instruction import Instruction

class LoadMem(Instruction):
    """
    Load to memory class.
    LOAD REG MEM	; loads the specified memory unit into REG
    """
    def compute(self, reg1: Bits, reg2: Bits, value: Bits):
        data = self._memory.read(value)
        self._registers.write(reg1, data)


class LoadImd(Instruction):
    """
    Load to immediate value to register.
    LOAD REG IMD	; load specified 16-bit immediate value into REG
    """
    def compute(self, reg1: Bits, reg2: Bits, value: Bits):
        self._registers.write(reg1, value)
