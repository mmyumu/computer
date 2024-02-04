"""
Test for Decoders
"""
import pytest
from computer.electronic.circuits.decoder import Decoder2To4

# pylint: disable=C0116

@pytest.fixture(name="decoder2to4")
def fixture_decoder2to4():
    return Decoder2To4()


def test_decoder2to4_a1_false_a0_false(decoder2to4: Decoder2To4):
    d3, d2, d1, d0 = decoder2to4(False, False)
    assert d3 is False
    assert d2 is False
    assert d1 is False
    assert d0 is True

def test_decoder2to4_a1_false_a0_true(decoder2to4: Decoder2To4):
    d3, d2, d1, d0 = decoder2to4(False, True)
    assert d3 is False
    assert d2 is False
    assert d1 is True
    assert d0 is False

def test_decoder2to4_a1_true_a0_false(decoder2to4: Decoder2To4):
    d3, d2, d1, d0 = decoder2to4(True, False)
    assert d3 is False
    assert d2 is True
    assert d1 is False
    assert d0 is False

def test_decoder2to4_a1_true_a0_true(decoder2to4: Decoder2To4):
    d3, d2, d1, d0 = decoder2to4(True, True)
    assert d3 is True
    assert d2 is False
    assert d1 is False
    assert d0 is False
