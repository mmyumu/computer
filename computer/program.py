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


class Requirements:
    """
    Class storing the program requirements
    """
    def __init__(self) -> None:
        self.memory_size = None
        self.register_size = None
        self.screen_resolution = None

    def get_kwargs_dict(self):
        """
        Returns a dictionary describing the requirements that can be used as kwargs for System

        Returns:
            _type_: _description_
        """
        return {
            "memory_size": self.memory_size,
            "register_size": self.register_size,
            "screen_resolution": self.screen_resolution
        }


class Program:
    """
    Class representing a full program (requirements and binary program)
    """
    def __init__(self, requirements: Requirements, binary_program: BinaryProgram):
        self.requirements = requirements
        self.binary_program = binary_program
