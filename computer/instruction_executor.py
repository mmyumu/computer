"""
Instruction executor module
"""
from typing import List
from computer.data_types import Bits
from computer.electronic.circuits.decoder import Decoder
from computer.instructions.instruction import Instruction


class InstructionExecutor:
    """
    Base class for instruction executor.
    Use a decoder to execute the instruction matching the opcode among the given instructions.
    """
    def __init__(self, instructions: List[Instruction]) -> None:
        self._decoder = Decoder(7)
        self._instructions = instructions

    def execute_instruction(self, opcode: Bits, operand: Bits):
        """
        Execute the instruction matching the opcode with the operand as parameter

        Args:
            opcode (Bits): the opcode of the instruction to execute. 
                            7 bits since first one is used to know if it is alu or cu
            operand (Bits): the operand to pass to the instruction
        """
        bits = self._decoder(*opcode, enable=True)
        for i, bit in enumerate(bits[::-1]):
            if bit:
                self._instructions[i](operand)
                break
