"""
Instruction module.
"""
from abc import ABC, abstractmethod
from typing import Any
from computer.data_types import Bits
from computer.memory import SRAM
from computer.program_counter import ProgramCounter
from computer.registers import Registers


class Instruction(ABC):
    """
    Instruction base class
    """
    def __init__(self, registers: Registers = None, memory: SRAM = None, program_counter: ProgramCounter = None) -> None:
        self._registers = registers
        self._memory = memory
        self._program_counter = program_counter

    def __call__(self, operand: Bits) -> Any:
        operand_check_size = self._memory.size + (self._registers.size * 2)
        if len(operand) != operand_check_size:
            raise ValueError(f"Length of operand should be {operand_check_size} but is {len(operand)}")

        reg1 = operand[:self._registers.size]
        reg2 = operand[self._registers.size:2*self._registers.size]
        value = operand[2*self._registers.size:2*self._registers.size + self._memory.size]
        self.compute(reg1, reg2, value)

    @abstractmethod
    def compute(self, reg1: Bits, reg2: Bits, value: Bits):
        """
        Compute the instruction
        """
