import pytest
from logic_gates.cmos import NOTGate


@pytest.fixture(name="cmos_not_gate")
def fixture_nmos_transistor():
    return NOTGate()


def test_not_gate_true(cmos_not_gate: NOTGate):
    assert cmos_not_gate.operate(True) is False

def test_not_gate_false(cmos_not_gate: NOTGate):
    assert cmos_not_gate.operate(False) is True