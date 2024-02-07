"""
Memory module
"""
from computer.data_types import Address2, Data4
from computer.electronic.circuits.decoder import Decoder2To4
from computer.electronic.circuits.register import PIPORegister4


class Memory:
    """
    Memory class.
    """
    def __init__(self):
        self._registers = [PIPORegister4() for _ in range(4)]
        self._decoder = Decoder2To4()

    def write(self, a: Address2, d: Data4):
        """
        Write the given value at the given address of the memory
        """
        select_lines = self._decoder(a[1], a[0], True)
        for i, select in enumerate(select_lines):
            if select:
                self._registers[i].set_d(d[3], d[2], d[1], d[0])
                break

    def read(self, a: Address2):
        """
        Read data from memory at the given address
        """
        select_lines = self._decoder(a[1], a[0], True)
        for i, select in enumerate(select_lines):
            if select:
                return self._registers[i].output

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
