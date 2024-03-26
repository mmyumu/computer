"""
CPU module
"""
from computer.clock import Clock
from computer.control_unit import ControlUnit
from computer.memory import Memory
from computer.program_counter import ProgramCounter
from computer.registers import Registers
from computer.rom import ROM
from utils.logger import logger


# pylint: disable=R0913

class CPU:
    """
    CPU class
    """
    def __init__(self, clock: Clock, memory: Memory, rom: ROM, registers_size: int=4, register_size: int=4, cheating_optim: bool = True):
        self._clock = clock
        self._memory = memory
        self._rom = rom
        self._registers = Registers(size=registers_size, register_size=register_size)
        self._program_counter = ProgramCounter(size=memory.register_size)
        self._control_unit = ControlUnit(self._registers, memory, self._program_counter)

        self._cheating_optim = cheating_optim

    def reset(self):
        """
        Reset the states of CPU
        """
        self._registers.reset()
        self._program_counter.reset()

    def run(self):
        """
        Run the CPU
        """
        logger.info("CPU is now running...")
        while True:
            self._clock.tick()
            if self._cheating_optim is True and self._clock.clock_state is False:
                continue

            instruction = self._rom.read(self._program_counter.value)

            self._program_counter.increment()

            # Looks like cheating (call twice the clock tick on PC) but not sure what to do yet.
            # If we don't do it, conditional jumps do not work since they will jump to "current address" and erase the increment.
            self._program_counter.clock_tick(self._clock.clock_state)

            opcode = instruction[:8]
            if opcode.to_int() == 255:
                break

            self._control_unit.execute(instruction[:8], instruction[8:])

            self._program_counter.clock_tick(self._clock.clock_state)
            self._memory.clock_tick(self._clock.clock_state)
            self._registers.clock_tick(self._clock.clock_state)

        logger.info("CPU run has completed.")
