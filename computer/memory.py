"""
Memory module
"""
import time
from abc import ABC, abstractmethod
from computer.data_types import Bits
from computer.electronic.circuits.decoder import Decoder
from computer.registers import Registers
from utils.logger import logger


# pylint: disable=R0902
class Memory(ABC):
    """
    Base class for memory
    """
    def __init__(self, size=16, register_size=4):
        self.size = size
        self.register_size = register_size

    @abstractmethod
    def write(self, address: Bits, d: Bits):
        """
        Write the given value at the given address of the memory
        """

    @abstractmethod
    def read(self, address: Bits) -> Bits:
        """
        Read data from memory at the given address
        """

    def clock_tick(self, enable: bool):
        """
        Clock tick input

        Args:
            enable (bool): the state of the clock
        """


class SRAM(Memory):
    """
    Memory class.
    SRAM is a list of blocks of RAM for optimization.
    Python cheating optimizations on clock tick can be enabled/disabled.
    """
    def __init__(self, size: int=16, register_size: int=4, level: int=0, cheating_optim: bool=True):
        super().__init__(size=size, register_size=register_size)
        self._cheating_optim = cheating_optim
        self._level = level

        if level == 0:
            start_time = time.time()
            logger.info(f"Initializing RAM (size: {2**size})...")

        self._written_subrams = []
        self._written_blocks = []

        self._sram_blocks = []
        self._sub_sram = []
        if size == 4:
            self._sram_blocks = [Registers(size=2, register_size=register_size) for _ in range(4)]
        elif size > 4:
            self._sub_sram = [SRAM(size=size - 2, register_size=register_size, level=level+1, cheating_optim=cheating_optim) for _ in range(4)]
        else:
            raise ValueError(f"Invalid RAM size: {size}")

        self._decoder = Decoder(2)

        if level == 0:
            logger.info(f"RAM (size: {2**size}) initialized in {time.time() - start_time:.2f}s")

    def write(self, address: Bits, d: Bits):
        # Cut address if the memory size is lower than the maximum size that can be used with the register size.
        # Exemple : if register size is 4 -> 2^4 = 16bits which means the memory can be maximum 16.
        # If memory size is only 10, it means it does not use all the 2^16 (=65536) potential addresses
        if len(address) > self.size:
            if any(address[:-self.size]):
                logger.error(f"It seems we are trying to access an address out of the memory limit: address={address}, memory size={self.size}")
            address = address[-self.size:]

        upper_address = address[:2]
        lower_address = address[2:]
        if self.size > 4:
            select_lines = self._decoder(*upper_address)
            for i, select in enumerate(select_lines[::-1]):
                if select:
                    if self._cheating_optim:
                        self._written_subrams.append(i)
                    return self._sub_sram[i].write(lower_address, d)
            raise ValueError(f"Sub RAM not found at address {upper_address}. Select lines: {select_lines[::-1]}, Sub RAM content: {self._sub_sram}")

        select_lines = self._decoder(*upper_address)
        for i, select in enumerate(select_lines[::-1]):
            if select:
                if self._cheating_optim:
                    self._written_blocks.append(i)
                return self._sram_blocks[i].write(lower_address, d)
        raise ValueError(f"RAM block not found at address {upper_address}. Select lines: {select_lines[::-1]},RAM block content: {self._sram_blocks}")

    def read(self, address: Bits) -> Bits:
        # Cut address if the memory size is lower than the maximum size that can be used with the register size.
        # Exemple : if register size is 4 -> 2^4 = 16bits which means the memory can be maximum 16.
        # If memory size is only 10, it means it does not use all the 2^16 (=65536) potential addresses
        if len(address) > self.size:
            if any(address[:-self.size]):
                logger.error(f"It seems we are trying to access an address out of the memory limit: address={address}, memory size={self.size}")
            address = address[-self.size:]

        upper_address = address[:2]
        lower_address = address[2:]
        if self.size > 4:
            select_lines = self._decoder(*upper_address)
            for i, select in enumerate(select_lines[::-1]):
                if select:
                    return self._sub_sram[i].read(lower_address)
            raise ValueError(f"Sub RAM not found at address {upper_address}. Select lines: {select_lines[::-1]}, Sub RAM content: {self._sub_sram}")

        select_lines = self._decoder(*upper_address)
        for i, select in enumerate(select_lines[::-1]):
            if select:
                return self._sram_blocks[i].read(lower_address)
        raise ValueError(f"RAM block not found at address {upper_address}. Select lines: {select_lines[::-1]},RAM block content: {self._sram_blocks}")



    def reset(self):
        """
        Set memory to 0
        """
        for ram_block in self._sub_sram:
            ram_block.reset()
        for ram_block in self._sram_blocks:
            ram_block.reset()

    def clock_tick(self, enable: bool):
        """
        Update memory status on clock tick
        """
        if self._cheating_optim:
            for subram_idx in self._written_subrams:
                self._sub_sram[subram_idx].clock_tick(enable)
            self._written_subrams = []
            for block_idx in self._written_blocks:
                self._sram_blocks[block_idx].clock_tick(enable)
            self._written_blocks = []
        else:
            for ram_block in self._sub_sram:
                ram_block.clock_tick(enable)
            for ram_block in self._sram_blocks:
                ram_block.clock_tick(enable)

    def __str__(self):
        out_str = ""
        for i, ram_block in enumerate(self._sub_sram):
            out_str += f"SubRAM {self._level}.{i}: \n"
            out_str += f"{ram_block} \n"

        for i, ram_block in enumerate(self._sram_blocks):
            out_str += f"Block {self._level}.{i}: \n"
            out_str += f"{ram_block} \n"
        return out_str
