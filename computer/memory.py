"""
Memory module
"""
from computer.data_types import Bits, Data16
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

    def write(self, a: Bits, d: Data16):
        """
        Write the given value at the given address of the memory block
        """
        select_lines = self._decoder(*a, enable=True)
        for i, select in enumerate(select_lines[::-1]):
            if select:
                self._registers[i].set_d(*d)
                break

    def read(self, a: Bits):
        """
        Read data from memory block at the given address
        """
        select_lines = self._decoder(*a, enable=True)
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
        for i, register in enumerate(self._registers):
            out_str += f"Register {i}: \n"
            out_str += f"{register} \n"
        return out_str


class SRAM:
    """
    Memory class.
    SRAM is a list of blocks of RAM for optimization.
    """
    def __init__(self, size=16, level=0):
        self._size = size
        self._level = level

        if level == 0:
            logger.info(f"Initializing RAM (size: {2**size})...")

        self._sram_blocks = []
        self._sub_sram = []
        if size == 4:
            self._sram_blocks = [SRAMBlock(size=2) for _ in range(4)]
        elif size > 4:
            self._sub_sram = [SRAM(size=size - 2, level=level+1) for _ in range(4)]
        else:
            raise ValueError(f"Invalid RAM size: {size}")

        self._decoder = Decoder(2)

        if level == 0:
            logger.info(f"RAM (size: {2**size}) initialized")

    def write(self, address: Bits, d: Data16):
        """
        Write the given value at the given address of the memory
        """
        upper_address = address[:2]
        lower_address = address[2:]
        if self._size > 4:
            select_lines = self._decoder(*upper_address)
            for i, select in enumerate(select_lines[::-1]):
                if select:
                    return self._sub_sram[i].write(lower_address, d)
            raise ValueError(f"Sub RAM not found at address {upper_address}")

        select_lines = self._decoder(*upper_address)
        for i, select in enumerate(select_lines[::-1]):
            if select:
                return self._sram_blocks[i].write(lower_address, d)
        raise ValueError(f"RAM block not found at address {address}")

    def read(self, address: Bits):
        """
        Read data from memory at the given address
        """
        upper_address = address[:2]
        lower_address = address[2:]
        if self._size > 4:
            select_lines = self._decoder(*upper_address)
            for i, select in enumerate(select_lines[::-1]):
                if select:
                    return self._sub_sram[i].read(lower_address)
            raise ValueError(f"Sub RAM not found at address {upper_address}")

        select_lines = self._decoder(*upper_address)
        for i, select in enumerate(select_lines[::-1]):
            if select:
                return self._sram_blocks[i].read(lower_address)
        raise ValueError(f"RAM block not found at address {address}")



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
