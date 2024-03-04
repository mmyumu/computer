"""
No operation instruction module
"""

from typing import Any

from computer.data_types import Bits


# pylint: disable=R0903

class Nop:
    """
    Does nothing
    """
    def __call__(self, operand: Bits) -> Any:
        pass
