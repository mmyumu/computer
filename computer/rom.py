"""
ROM module
"""
import time
from typing import List
from computer.data_types import Bits
from computer.electronic.circuits.register import PIPORegister
from computer.program import BinaryProgram
from utils.logger import logger

class ROM:
    """
    ROM class
    """
    def __init__(self, size=12, register_size=16):
        start_time = time.time()
        logger.info(f"Initializing ROM (size: {2**size})...")
        self._size = size
        self._register_size = register_size

        self._registers: List[PIPORegister] = []
        for _ in range(2 ** self._size):
            self._registers.append(PIPORegister(size=register_size))
        self.initialized = False
        logger.info(f"ROM (size: {2**size}) initialized in {time.time() - start_time:.2f}s")

    def read(self, address: Bits) -> Bits:
        """
        Read data from ROM at the given address

        Args:
            address (Bits): _description_

        Returns:
            Bits: the bits readen from the ROM
        """
        value = self._registers[address.to_int()].output
        logger.debug(f"Reading value {value} from ROM address {address.to_int()}")
        return value

    def set(self, program: BinaryProgram):
        """
        Write the ROM registers

        Args:
            registers (List[Register]): the registers of the ROM
        """
        for i, operation in enumerate(program):
            self._registers[i].set_d(*operation)
        self.initialized = True

    def clock_tick(self, enable: bool):
        """
        Clock tick input

        Args:
            enable (bool): the state of the clock
        """
        for register in self._registers:
            register.clock_tick(enable)
