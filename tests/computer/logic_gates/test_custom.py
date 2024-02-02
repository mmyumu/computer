import pytest
from computer.logic_gates.custom import NOTGate


@pytest.fixture(name="custom_not_gate")
def fixture_nmos_transistor():
    return NOTGate()

def test_not_gate_true(custom_not_gate: NOTGate):
    assert custom_not_gate(True) is False

def test_not_gate_false(custom_not_gate: NOTGate):
    assert custom_not_gate(False) is True