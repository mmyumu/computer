"""
Test configuration for computer package
"""
import pytest
from computer.memory import SRAM

from computer.program_counter import ProgramCounter
from computer.registers import Registers


# pylint: disable=C0116

@pytest.fixture(name="program_counter")
def fixture_program_counter():
    return ProgramCounter(size=3)

@pytest.fixture(name="registers")
def fixture_registers():
    return Registers(size=3, register_size=3)

@pytest.fixture(name="memory")
def fixture_memory():
    return SRAM(size=8, register_size=3)
