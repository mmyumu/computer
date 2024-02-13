"""
CPU module
"""
from computer.control_unit import ControlUnit
from computer.data_types import Bits, Opcode8
from computer.registers import Registers


class CPU:
    """
    CPU class
    """
    def __init__(self, memory, registers_size: int=4, register_size: int=4):
        self._memory = memory
        self._registers = Registers(size=registers_size, register_size=register_size)
        self._control_unit = ControlUnit(self._registers, memory)

    def execute(self, opcode: Opcode8, operand: Bits):
        """
        Execute the operation defined with the opcode and with operand as parameter
        """
        operand_check_size = self._memory.size + (self._registers.size * 2)
        if len(operand) != operand_check_size:
            raise ValueError(f"Length of operand should be {operand_check_size} but is {len(operand)}")
