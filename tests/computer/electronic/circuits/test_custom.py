"""
Test of custom gates
"""
import pytest
from computer.electronic.circuits.custom import NOTGate

# pylint: disable=C0116

@pytest.fixture(name="custom_not_gate")
def fixture_nmos_transistor():
    return NOTGate()

def test_not_gate_true(custom_not_gate: NOTGate):
    assert custom_not_gate(True) is False

def test_not_gate_false(custom_not_gate: NOTGate):
    assert custom_not_gate(False) is True
