"""
Memory module
"""
from computer.electronic.circuits.decoder import Decoder2To4
from computer.electronic.circuits.register import PIPORegister4


class Address2:
    """
    Class to store an address of 2 bits
    """
    def __init__(self, a1: bool, a0: bool) -> None:
        self.a1 = a1
        self.a0 = a0


class Data4:
    """
    Class to store a data of 4 bits
    """
    def __init__(self, d3: bool, d2: bool, d1: bool, d0: bool) -> None:
        self.d3 = d3
        self.d2 = d2
        self.d1 = d1
        self.d0 = d0


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
        select_lines = self._decoder(a.a1, a.a0, True)
        for i, select in enumerate(select_lines):
            if select:
                self._registers[i].set_d(d.d3, d.d2, d.d1, d.d0)
                break

    def read(self, a: Address2):
        """
        Read data from memory at the given address
        """
        select_lines = self._decoder(a.a1, a.a0, True)
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
