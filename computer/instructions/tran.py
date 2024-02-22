"""
Tran instructions module
"""
from computer.data_types import Bits
from computer.instructions.instruction import ControlInstruction

# pylint: disable=R0903
class Tran(ControlInstruction):
    """
    Transfer value from Reg A to Reg B
    TRAN REG REG	; transfers value from REGA to REGB
    """
    def compute(self, reg1: Bits, reg2: Bits, value: Bits):
        value = self._registers.read(reg1)
        self._registers.write(reg2, value)
