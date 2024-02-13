"""
System module
"""
from computer.cpu import CPU
from computer.memory import SRAM


class System:
    """
    System class
    """
    def __init__(self, memory_size=16, register_size=4):
        self._memory = SRAM(size=memory_size, register_size=register_size)
        self.cpu = CPU(self._memory)
