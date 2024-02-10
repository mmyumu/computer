"""
CPU Registers module
"""
from computer.electronic.circuits.register import PIPORegister


class Registers(list):
    """
    CPU registers class
    """
    def __init__(self, size=16):
        for _ in range(size):
            self.append(PIPORegister(size=16))
