"""
Test configuration for instructions package
"""
import pytest

from computer.memory import SRAM
from computer.registers import Registers


# pylint: disable=C0116

@pytest.fixture(name="registers")
def fixture_registers():
    return Registers(size=3, register_size=3)

@pytest.fixture(name="sram")
def fixture_memory():
    return SRAM(size=8, register_size=3)
