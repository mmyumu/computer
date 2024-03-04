"""
Rotation left/right module
"""

from abc import abstractmethod
from computer.data_types import Bits
from computer.electronic.circuits.shifter import BarrelShifter
from computer.instructions.instruction import ALUInstruction
from computer.registers import Registers


class Rotation(ALUInstruction):
    """
    Base class for rotation instructions
    """
    def __init__(self, registers: Registers, memory_size: int) -> None:
        super().__init__(registers, memory_size)
        self._barrel_shifter = self._build_barrel_shifter()

    @abstractmethod
    def _build_barrel_shifter(self):
        """
        Build the barrel shifter (right or left) to be used for the specific rotation
        """

    def compute(self, reg1: Bits, reg2: Bits, value: Bits):
        data1 = self._registers.read(reg1)
        result, carry_out = self._barrel_shifter(data1, value[-3:])
        self._registers.write(reg1, result)
        self._registers.cf = carry_out


class ROR(Rotation):
    """
    Perform rotation right.
    ROR REG IMD	; rightwise roll of bits of REGA carried out IMD times
				; IMD is a 4-bit value
    """
    def _build_barrel_shifter(self):
        return BarrelShifter(self._registers.size, right=True)


class ROL(Rotation):
    """
    Perform rotation right.
    ROR REG IMD	; rightwise roll of bits of REGA carried out IMD times
				; IMD is a 4-bit value
    """
    def _build_barrel_shifter(self):
        return BarrelShifter(self._registers.size, right=False)
