"""
Bitwise AND instruction module
"""
from computer_legacy.instructions.instructions import Instruction


class BitwiseAnd(Instruction):
    """
    Bitwise AND instruction
    """
    def __init__(self, dest_reg, src_reg1, src_reg2):
        self.dest_reg = dest_reg
        self.src_reg1 = src_reg1
        self.src_reg2 = src_reg2

    def execute(self, cpu):
        cpu.alu.bitwise_and(cpu.registers, self.dest_reg, self.src_reg1, self.src_reg2)
