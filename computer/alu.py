"""
Arithmetic logic unit (ALU) module
"""
from computer.instruction_executor import InstructionExecutor
from computer.instructions.algebra import Add, Cmp, Dec, Div, Inc, Mult, Sub
from computer.instructions.logic import ANDReg, NOTReg, ORReg, XORReg
from computer.instructions.rotate import ROL, ROR
from computer.registers import Registers


class ALU(InstructionExecutor):
    """
    Arithmetic logic unit class
    """
    def __init__(self, registers: Registers, memory_size: int):
        instructions = [
            Add(registers, memory_size),
            Sub(registers, memory_size),
            Mult(registers, memory_size),
            Div(registers, memory_size),
            Inc(registers, memory_size),
            Dec(registers, memory_size),
            ANDReg(registers, memory_size),
            ORReg(registers, memory_size),
            XORReg(registers, memory_size),
            NOTReg(registers, memory_size),
            ROL(registers, memory_size),
            ROR(registers, memory_size),
            Cmp(registers, memory_size)
        ]
        super().__init__(instructions)
