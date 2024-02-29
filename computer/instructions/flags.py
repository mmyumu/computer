"""
Jump instructions module
"""
from computer.data_types import Bits
from computer.instructions.instruction import ControlInstruction

# pylint: disable=R0903
class CLC(ControlInstruction):
    """
    Clear the carry flag
    CLC			; sets CF to 0
    """
    def compute(self, reg1: Bits, reg2: Bits, value: Bits):
        self._registers.cf = False


class STC(ControlInstruction):
    """
    Set the carry flag
    STC			; sets CF to 1
    """
    def compute(self, reg1: Bits, reg2: Bits, value: Bits):
        self._registers.cf = True
