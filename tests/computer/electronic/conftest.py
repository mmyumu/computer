import pytest
from computer.electronic.nmos_transistor import NMOSTransistor
from computer.electronic.pmos_transistor import PMOSTransistor


@pytest.fixture(name="nmos_transistor")
def fixture_nmos_transistor():
    return NMOSTransistor()

@pytest.fixture(name="pmos_transistor")
def fixture_pmos_transistor():
    return PMOSTransistor()