"""
System module
"""
import time
from computer.clock import Clock
from computer.cpu import CPU
from computer.memory import SRAM
from computer.program import BinaryProgram
from computer.rom import ROM
from computer.screen import Screen
from utils.logger import logger


# pylint: disable=R0913
class System:
    """
    System class
    """
    def __init__(self, memory_size: int=16, register_size: int=4, embedded_screen: bool=False,
                 screen_resolution:int = 128, screen_refresh_rate:int = 30):
        self._clock = Clock()

        self._memory = SRAM(size=memory_size, register_size=register_size)
        self._rom = ROM(size=12, register_size=8 + 2 * register_size + 2 ** register_size)
        self._cpu = CPU(self._clock, self._memory, self._rom)
        self._screen_resolution = screen_resolution
        self._screen_refresh_rate = screen_refresh_rate

        self._screen = None
        if embedded_screen:
            self._screen = Screen(self._memory, resolution=self._screen_resolution, refresh_rate=self._screen_refresh_rate)

    def load_rom(self, program: BinaryProgram):
        """
        Load given binary program into ROM

        Args:
            program (BinaryProgram): the program to load into ROM
        """
        star_time = time.time()
        logger.info("Loading ROM...")
        self._rom.set(program)
        self._rom.clock_tick(True)
        logger.info(f"ROM loaded in {time.time() - star_time:.2f}")

    def turn_on(self):
        """
        Turn on the system.
        Reset then starts the components.
        """
        if self._screen:
            self._screen.start()

        self._memory.reset()
        self._cpu.reset()
        self._cpu.run()

        if self._screen:
            self._screen.stop()
