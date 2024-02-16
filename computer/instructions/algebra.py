"""
Algebra instructions module
"""
from computer.data_types import Bits
from computer.electronic.circuits.adder import FullAdder
from computer.electronic.circuits.bitwise import BitwiseAdd, BitwiseSub
from computer.electronic.circuits.complement import TwoComplement
from computer.instructions.instruction import ALUInstruction
from computer.registers import Registers

# pylint: disable=R0903

class Add(ALUInstruction):
    """
    Add between 2 registers
    ADD REG REG	; REGA + REGB + CF, result stored in REGA
    """
    def __init__(self, registers: Registers, memory_size: int) -> None:
        super().__init__(registers, memory_size)
        self._adder = BitwiseAdd(self._registers.register_size)

    def compute(self, reg1: Bits, reg2: Bits, value: Bits):
        data1 = self._registers.read(reg1)
        data2 = self._registers.read(reg2)

        data, carry_out = self._adder(data1, data2, self._registers.cf)

        self._registers.cf = carry_out
        self._registers.write(reg1, data)


class Sub(ALUInstruction):
    """
    Sub between 2 registers
    SUB REG REG	; (REGA - REGB) - CF, result stored in REGA
    """
    def __init__(self, registers: Registers, memory_size: int) -> None:
        super().__init__(registers, memory_size)
        self._sub1 = BitwiseSub(self._registers.size)
        self._sub2 = BitwiseSub(self._registers.size)

    def compute(self, reg1: Bits, reg2: Bits, value: Bits):
        data1 = self._registers.read(reg1)
        data2 = self._registers.read(reg2)

        sub1 = self._sub1(data1, data2)

        cf = [0] * 7 + [self._registers.cf]
        sub2 = self._sub2(sub1, cf)

        self._registers.cf = False
        self._registers.write(reg1, sub2)

