"""
Memory module
"""
from computer.data_types import Address16, Bits, Data16
from computer.electronic.circuits.decoder import Decoder
from computer.registers import Registers
from utils.logger import logger


class SRAMBlock:
    """
    Block of SRAM containing a given number of registers (each registers is a list of register)
    """
    def __init__(self, size=16) -> None:
        self._registers = Registers(2 ** size)
        self._decoder = Decoder(size)

    def write(self, a: Address16, d: Data16):
        """
        Write the given value at the given address of the memory block
        """
        select_lines = self._decoder(*a, enable=True)
        for i, select in enumerate(select_lines[::-1]):
            if select:
                self._registers[i].set_d(*d)
                break

    def read(self, a: Address16):
        """
        Read data from memory block at the given address
        """
        select_lines = self._decoder(*a[::-1], enable=True)
        for i, select in enumerate(select_lines[::-1]):
            if select:
                return self._registers[i].output
        raise ValueError(f"Address {a} cannot be read")

    def reset(self):
        """
        Set memory block to 0
        """
        # TODO: Is it useful? Probably not, but for unit test it helps
        for register in self._registers:
            register.reset_states()

    def clock_tick(self, enable: bool):
        """
        Update memory block status on clock tick
        """
        for register in self._registers:
            register.clock_tick(enable)

    def __str__(self):
        out_str = ""
        for i, register in enumerate(self._registers[::-1]):
            out_str += f"Register {i}: \n"
            out_str += f"{register} \n"
        return out_str


class SRAM:
    """
    Memory class.
    SRAM is a list of blocks of RAM for optimization.
    """
    def __init__(self, size=16, blocks_size=16):
        if size < blocks_size:
            raise ValueError(f"Size ({size}) must be greater or equal than block size ({blocks_size})")

        self._sram_size = size
        self._sram_block_size = blocks_size
        self._blocks_number = 2 ** (size - blocks_size)

        logger.info(f"Initializing RAM (size: {2**size}, blocks size: {2**blocks_size}, number of blocks: {self._blocks_number})...")

        self._sram_blocks = [SRAMBlock(size=self._sram_block_size) for _ in range(self._blocks_number)]

        if self._blocks_number > 1:
            self._decoder = Decoder(self._sram_block_size)
        else:
            self._decoder = None

        logger.info(f"RAM (size: {2**size}, blocks size: {2**blocks_size}, number of blocks: {self._blocks_number}) initialized")

    def write(self, address: Bits, d: Data16):
        """
        Write the given value at the given address of the memory
        """
        if self._decoder is None:
            return self._sram_blocks[0].write(address, d)

        ram_block_address = address[:self._sram_block_size]
        select_lines = self._decoder(*ram_block_address)
        for i, select in enumerate(select_lines[::-1]):
            if select:
                return self._sram_blocks[i].write(address[self._sram_block_size:], d)
        raise ValueError(f"RAM block not found at address {ram_block_address}")

    def read(self, address: Bits):
        """
        Read data from memory at the given address
        """
        if self._decoder is None:
            return self._sram_blocks[0].read(address)

        ram_block_address = address[:self._sram_block_size]
        select_lines = self._decoder(*ram_block_address)
        for i, select in enumerate(select_lines[::-1]):
            if select:
                return self._sram_blocks[i].read(address[self._sram_block_size:])
        raise ValueError(f"RAM block not found at address {ram_block_address}")

    def reset(self):
        """
        Set memory to 0
        """
        for ram_block in self._sram_blocks:
            ram_block.reset()

    def clock_tick(self, enable: bool):
        """
        Update memory status on clock tick
        """
        for ram_block in self._sram_blocks:
            ram_block.clock_tick(enable)

    def __str__(self):
        out_str = ""
        for i, ram_block in enumerate(self._sram_blocks[::-1]):
            out_str += f"Block {i}: \n"
            out_str += f"{ram_block} \n"
        return out_str
