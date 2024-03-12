"""
ROM module
"""


from typing import List
from computer.data_types import Bits
from computer.electronic.circuits.register import PIPORegister
from computer.memory import Memory
from program.program import BinaryProgram


class ROM(Memory):
    """
    ROM class
    """
    def __init__(self, size=12, register_size=4):
        super().__init__(size, register_size)
        self._registers: List[PIPORegister] = []
        for _ in range(2 ** self.size):
            self._registers.append(PIPORegister(size=register_size))

    def write(self, address: Bits, d: Bits):
        raise NotImplementedError("Cannot write ROM")

    def read(self, address: Bits):
        return self._registers[address.to_int()].output

    def set(self, program: BinaryProgram):
        """
        Write the ROM registers

        Args:
            registers (List[Register]): the registers of the ROM
        """
        for i, operation in enumerate(program):
            self._registers[i].set_d(*operation)

    def clock_tick(self, enable: bool):
        for register in self._registers:
            register.clock_tick(enable)
