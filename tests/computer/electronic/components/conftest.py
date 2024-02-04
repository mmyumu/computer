"""
Test configuration for electronic package
"""
import pytest
from computer.electronic.components.transistor import NMOSTransistor
from computer.electronic.components.transistor import PMOSTransistor


# pylint: disable=C0116

@pytest.fixture(name="nmos_transistor")
def fixture_nmos_transistor():
    return NMOSTransistor()

@pytest.fixture(name="pmos_transistor")
def fixture_pmos_transistor():
    return PMOSTransistor()
