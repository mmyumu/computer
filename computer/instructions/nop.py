"""
No operation instruction module
"""

from typing import Any

from computer.data_types import Operand24


# pylint: disable=R0903

class Nop:
    """
    Does nothing
    """
    def __call__(self, operand: Operand24) -> Any:
        pass
