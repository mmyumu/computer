"""
CPU module
"""
from computer.clock import Clock
from computer.control_unit import ControlUnit
from computer.memory import Memory
from computer.program_counter import ProgramCounter
from computer.registers import Registers
from computer.rom import ROM


# pylint: disable=R0913

class CPU:
    """
    CPU class
    """
    def __init__(self, clock: Clock, memory: Memory, rom: ROM, registers_size: int=4, register_size: int=4):
        self._clock = clock
        self._memory = memory
        self._rom = rom
        self._registers = Registers(size=registers_size, register_size=register_size)
        self._program_counter = ProgramCounter(size=memory.register_size)
        self._control_unit = ControlUnit(self._registers, memory, self._program_counter)
        # self._alu = ALU(self._registers, memory.size)

    def run(self):
        """
        Run the CPU
        """
        while self._clock.tick():
            self._program_counter.clock_tick(self._clock.clock_state)
            self._memory.clock_tick(self._clock.clock_state)
            self._registers.clock_tick(self._clock.clock_state)

            instruction = self._rom.read(self._program_counter.value)
            self._control_unit.execute(instruction[:8], instruction[8:])
