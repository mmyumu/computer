"""
CPU Registers module
"""
from computer.data_types import Bits
from computer.electronic.circuits.decoder import Decoder
from computer.electronic.circuits.register import PIPORegister


class Registers(list):
    """
    CPU registers class.
    """
    def __init__(self, size: int=4, register_size: int=4):
        """
        Constructor of Registers

        Args:
            size (int, optional): The number of registers in the container (as a power of 2). Defaults to 4.
            register_size (int, optional): The size of each register (as a power of 2). Defaults to 4.
        """
        self.size = size
        self.register_size = register_size

        self.cf: bool = False
        self.zf: bool = False

        self._decoder = Decoder(size)
        for _ in range(2 ** size):
            self.append(PIPORegister(size=2 ** register_size))

    def write(self, a: Bits, d: Bits):
        """
        Write the given value at the given address of the memory block
        """
        select_lines = self._decoder(*a, enable=True)
        for i, select in enumerate(select_lines[::-1]):
            if select:
                self[i].set_d(*d)
                break

    def read(self, a: Bits):
        """
        Read data from memory block at the given address
        """
        select_lines = self._decoder(*a, enable=True)
        for i, select in enumerate(select_lines[::-1]):
            if select:
                return self[i].output
        raise ValueError(f"Address {a} cannot be read")

    def reset(self):
        """
        Set memory block to 0
        """
        for register in self:
            register.reset_states()

    def clock_tick(self, enable: bool):
        """
        Update memory block status on clock tick
        """
        for register in self:
            register.clock_tick(enable)

    def __str__(self):
        out_str = ""
        for i, register in enumerate(self):
            out_str += f"Register {i}: \n"
            out_str += f"{register} \n"
        return out_str
