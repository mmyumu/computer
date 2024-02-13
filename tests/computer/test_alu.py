"""
Test for ALU.
The tests are done with a light memory configuration: 
 - 2**8 bits RAM
 - 2**3 bits registers
 - 2**3 bits for each register
"""
import pytest

from computer.alu import ALU
from computer.registers import Registers


# pylint: disable=C0116,W0212

@pytest.fixture(name="alu")
def fixture_alu(registers: Registers):
    return ALU(registers)
