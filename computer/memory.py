"""
Memory module
"""
from computer.data_types import Address10, Data4
from computer.electronic.circuits.decoder import Decoder
from computer.electronic.circuits.register import PIPORegister


# TODO: Could be improved to a matrix of cells instead of an array
class SRAM:
    """
    Memory class.
    """
    def __init__(self, size=10):
        self._registers = [PIPORegister() for _ in range(2**size)]
        self._decoder = Decoder(10)

    def write(self, a: Address10, d: Data4):
        """
        Write the given value at the given address of the memory
        """
        select_lines = self._decoder(*a[::-1], enable=True)
        for i, select in enumerate(select_lines):
            if select:
                self._registers[i].set_d(d[3], d[2], d[1], d[0])
                break

    def read(self, a: Address10):
        """
        Read data from memory at the given address
        """
        select_lines = self._decoder(*a[::-1], enable=True)
        for i, select in enumerate(select_lines):
            if select:
                return self._registers[i].output
        raise ValueError(f"Address {a} cannot be read")

    def reset(self):
        """
        Set memory to 0
        """
        # TODO: Is it useful? Probably not, but for unit test it helps
        for register in self._registers:
            register.reset_states()

    def clock_tick(self, enable: bool):
        """
        Update memory status on clock tick
        """
        for register in self._registers:
            register.clock_tick(enable)

    def __str__(self):
        out_str = ""
        for i, register in enumerate(self._registers[::-1]):
            out_str += f"Register {i}: \n"
            out_str += f"{register} \n"
        return out_str
