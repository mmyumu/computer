"""
Test for GUIGNOL interpreter module
"""

import pytest

from computer.system import System
from guignol.interpreter import BinaryProgramInterpreter

# pylint: disable=C0116

@pytest.fixture(name="system")
def fixture_system():
    return System(memory_size=8, register_size=4)

def test_system_load_rom(system: System):
    interpreter = BinaryProgramInterpreter([], register_size=4)
    program = interpreter("program/test_perf.guignol", from_file=True)

    system.load_rom(program)

def test_system_run(system: System):
    interpreter = BinaryProgramInterpreter([], register_size=4)
    program = interpreter("program/test_perf.guignol", from_file=True)

    system.load_rom(program)
    system.turn_on()
