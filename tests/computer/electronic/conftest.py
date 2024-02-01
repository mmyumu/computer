import pytest
from computer.electronic.transistor import NMOSTransistor
from computer.electronic.transistor import PMOSTransistor


@pytest.fixture(name="nmos_transistor")
def fixture_nmos_transistor():
    return NMOSTransistor()

@pytest.fixture(name="pmos_transistor")
def fixture_pmos_transistor():
    return PMOSTransistor()