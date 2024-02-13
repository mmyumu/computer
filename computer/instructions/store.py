"""
Store instructions module
"""
from computer.data_types import Bits
from computer.instructions.instruction import ControlInstruction

# pylint: disable=R0903
class StoreMem(ControlInstruction):
    """
    Store from register to memory
    STORE REG MEM	; stores the value of REG to the address specified
    """
    def compute(self, reg1: Bits, reg2: Bits, value: Bits):
        data = self._registers.read(reg1)
        self._memory.write(value, data)


class StoreReg(ControlInstruction):
    """
    Store from register to memory address in register
    STORE REG REG 	; stores the value of REGA into the memory unit at the address in REGB
    """
    def compute(self, reg1: Bits, reg2: Bits, value: Bits):
        data = self._registers.read(reg1)
        memory_address = self._registers.read(reg2)
        self._memory.write(memory_address, data)
