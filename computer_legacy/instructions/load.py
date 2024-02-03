"""
Load instruction module
"""
from computer_legacy.instructions.instructions import Instruction


class Load(Instruction):
    """
    Load instruction class
    """
    def __init__(self, register_index, value):
        self.register_index = register_index
        self.value = value

    def execute(self, cpu):
        cpu.alu.load(cpu.registers, self.register_index, self.value)
