"""
Load instructions module
"""
from computer.data_types import Bits
from computer.instructions.instruction import ControlInstruction

# pylint: disable=R0903

class LoadMem(ControlInstruction):
    """
    Load from memory address to register class.
    LOAD REG MEM	; loads the specified memory unit into REG
    """
    def compute(self, reg1: Bits, reg2: Bits, value: Bits):
        data = self._memory.read(value)
        self._registers.write(reg1, data)


class LoadImd(ControlInstruction):
    """
    Load immediate value to register.
    LOAD REG IMD	; load specified 16-bit immediate value into REG
    """
    def compute(self, reg1: Bits, reg2: Bits, value: Bits):
        self._registers.write(reg1, value)


class LoadReg(ControlInstruction):
    """
    Load from memory address in register to register.
    LOAD REG REG	; loads memory unit at the address stored in REGB into REGA
    """
    def compute(self, reg1: Bits, reg2: Bits, value: Bits):
        memory_address = self._registers.read(reg2)
        data = self._memory.read(memory_address)
        self._registers.write(reg1, data)
