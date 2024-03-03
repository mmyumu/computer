"""
System module
"""
from computer.clock import RealTimeClock
from computer.cpu import CPU
from computer.memory import SRAM
from computer.rom import ROM


class System:
    """
    System class
    """
    def __init__(self, memory_size=16, register_size=4):
        self._clock = RealTimeClock(10)

        self._memory = SRAM(size=memory_size, register_size=register_size)
        self._rom = ROM(size=12, register_size=32)
        self._cpu = CPU(self._clock, self._memory, self._rom)
