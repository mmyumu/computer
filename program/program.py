"""
Program module
"""
from computer.data_types import Bits


class BinaryProgram(list):
    """
    Binary program class.
    It is a list of operations (Bits)
    """
    def append(self, __object: Bits) -> None:
        if not isinstance(__object, Bits):
            raise ValueError(f"Object should be Bits but is {type(__object)}")
        return super().append(__object)
