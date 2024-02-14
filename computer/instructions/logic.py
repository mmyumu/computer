"""
Load instructions module
"""
from abc import abstractmethod
from computer.data_types import Bits
from computer.electronic.circuits.cmos import ANDGate, NOTGate, ORGate, XORGate
from computer.instructions.instruction import LogicInstruction
from computer.registers import Registers

# pylint: disable=R0903

class BitwiseLogicInstruction(LogicInstruction):
    """
    Perform bitwise logic operation
    """
    def __init__(self, registers: Registers, memory_size: int) -> None:
        super().__init__(registers, memory_size)
        self._gates = self._build_gates()

    def compute(self, reg1: Bits, reg2: Bits, value: Bits):
        data1 = self._registers.read(reg1)
        data2 = self._registers.read(reg2)

        data = []
        for bit1, bit2, gate in zip(data1, data2, self._gates):
            data.append(gate(bit1, bit2))

        self._registers.write(reg1, data)

    @abstractmethod
    def _build_gates(self):
        pass


class ANDReg(BitwiseLogicInstruction):
    """
    AND between 2 registers
    AND REG REG	; REGA AND REGB, result stored in REGA
    """
    def _build_gates(self):
        and_gates = []
        for _ in range(2 ** self._registers.register_size):
            and_gates.append(ANDGate())
        return and_gates


class ORReg(BitwiseLogicInstruction):
    """
    OR between 2 registers
    OR REG REG		; REGA OR REGB, result stored in REGA
    """
    def _build_gates(self):
        or_gates = []
        for _ in range(2 ** self._registers.register_size):
            or_gates.append(ORGate())
        return or_gates


class XORReg(BitwiseLogicInstruction):
    """
    XOR between 2 registers
    XOR REG REG	; REGA XOR REGB, result stored in REGA
    """
    def _build_gates(self):
        xor_gates = []
        for _ in range(2 ** self._registers.register_size):
            xor_gates.append(XORGate())
        return xor_gates

class NOTReg(LogicInstruction):
    """
    NOT on register and store it
    NOT REG 		; NOT REGA, result stored in REGA
    """
    def __init__(self, registers: Registers, memory_size: int) -> None:
        super().__init__(registers, memory_size)
        self._gates = []
        for _ in range(2 ** self._registers.register_size):
            self._gates.append(NOTGate())

    def compute(self, reg1: Bits, reg2: Bits, value: Bits):
        data1 = self._registers.read(reg1)

        data = []
        for bit1, gate in zip(data1, self._gates):
            data.append(gate(bit1))

        self._registers.write(reg1, data)
