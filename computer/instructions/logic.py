"""
Load instructions module
"""
from computer.data_types import Bits
from computer.electronic.circuits.cmos import ANDGate
from computer.instructions.instruction import LogicInstruction
from computer.registers import Registers

# pylint: disable=R0903

class AndReg(LogicInstruction):
    """
    And between 2 registers
    AND REG REG	; REGA AND REGB, result stored in REGA
    """
    def __init__(self, registers: Registers, memory_size: int) -> None:
        super().__init__(registers, memory_size)

        self._ands = []
        for _ in range(2 ** registers.register_size):
            self._ands.append(ANDGate())

    def compute(self, reg1: Bits, reg2: Bits, value: Bits):
        data1 = self._registers.read(reg1)
        data2 = self._registers.read(reg2)

        data = []
        for bit1, bit2, and_gate in zip(data1, data2, self._ands):
            data.append(and_gate(bit1, bit2))

        self._registers.write(reg1, data)
