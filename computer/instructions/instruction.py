"""
Instruction module.
"""
from abc import ABC, abstractmethod
from typing import Any
from computer.data_types import Bits
from computer.electronic.circuits.cmos import NOTGate, ORGate
from computer.memory import SRAM
from computer.program_counter import ProgramCounter
from computer.registers import Registers
from utils.logger import logger


class Instruction(ABC):
    """
    Instruction base class
    """
    def __init__(self, registers_size: int, memory_register_size: int) -> None:
        self._registers_size = registers_size
        self._memory_register_size = memory_register_size

    def __call__(self, operand: Bits) -> Any:
        operand_check_size = (2 ** self._memory_register_size) + (self._registers_size * 2)
        if len(operand) != operand_check_size:
            raise ValueError(f"Length of operand should be {operand_check_size} but is {len(operand)}")

        reg1 = operand[:self._registers_size]
        reg2 = operand[self._registers_size:2*self._registers_size]
        value = operand[2*self._registers_size:2*self._registers_size + (2 ** self._memory_register_size)]

        logger.debug(f"Executing {self.__class__.__name__}: reg1={reg1.to_int()}, reg2={reg2.to_int()}, value={value.to_int()}")
        self.compute(reg1, reg2, value)

    @abstractmethod
    def compute(self, reg1: Bits, reg2: Bits, value: Bits):
        """
        Compute the instruction
        """


class ALUInstruction(Instruction):
    """
    Logic instruction base class
    """
    def __init__(self, registers: Registers, memory_register_size: int) -> None:
        super().__init__(registers_size=registers.register_size, memory_register_size=memory_register_size)
        self._registers = registers

        self._zf_or_gates = [ORGate() for _ in range(2 ** self._registers.size)]
        self._zf_not_gate = NOTGate()

    def update_zf(self, result: Bits):
        """
        Update ZF with the given result.
        ZF is updated if result is 0.

        Args:
            result (Bits): result to be checked to update ZF
        """
        or_result = 0
        for bit, or_gate in zip(result, self._zf_or_gates):
            or_result = or_gate(or_result, bit)
        self._registers.zf = self._zf_not_gate(or_result)


class ControlInstruction(Instruction):
    """
    Control instruction base class
    """
    def __init__(self, registers: Registers, memory: SRAM, program_counter: ProgramCounter) -> None:
        super().__init__(registers_size=registers.register_size, memory_register_size=memory.register_size)
        self._registers = registers
        self._memory = memory
        self._program_counter = program_counter
