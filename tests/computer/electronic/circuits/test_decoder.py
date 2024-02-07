"""
Test for Decoders
"""
import pytest
from computer.electronic.circuits.decoder import Decoder2To4, Decoder3To8

# pylint: disable=C0116

@pytest.fixture(name="decoder2to4")
def fixture_decoder2to4():
    return Decoder2To4()

@pytest.fixture(name="decoder3to8")
def fixture_decoder3to8():
    return Decoder3To8()

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

def test_decoder3to8_a2_false_a1_false_a0_false(decoder3to8: Decoder3To8):
    d7, d6, d5, d4, d3, d2, d1, d0 = decoder3to8(False, False, False)
    assert d7 is False
    assert d6 is False
    assert d5 is False
    assert d4 is False
    assert d3 is False
    assert d2 is False
    assert d1 is False
    assert d0 is True

def test_decoder3to8_a2_false_a1_false_a0_true(decoder3to8: Decoder3To8):
    d7, d6, d5, d4, d3, d2, d1, d0 = decoder3to8(False, False, True)
    assert d7 is False
    assert d6 is False
    assert d5 is False
    assert d4 is False
    assert d3 is False
    assert d2 is False
    assert d1 is True
    assert d0 is False

def test_decoder3to8_a2_false_a1_true_a0_false(decoder3to8: Decoder3To8):
    d7, d6, d5, d4, d3, d2, d1, d0 = decoder3to8(False, True, False)
    assert d7 is False
    assert d6 is False
    assert d5 is False
    assert d4 is False
    assert d3 is False
    assert d2 is True
    assert d1 is False
    assert d0 is False

def test_decoder3to8_a2_false_a1_true_a0_true(decoder3to8: Decoder3To8):
    d7, d6, d5, d4, d3, d2, d1, d0 = decoder3to8(False, True, True)
    assert d7 is False
    assert d6 is False
    assert d5 is False
    assert d4 is False
    assert d3 is True
    assert d2 is False
    assert d1 is False
    assert d0 is False

def test_decoder3to8_a2_true_a1_false_a0_false(decoder3to8: Decoder3To8):
    d7, d6, d5, d4, d3, d2, d1, d0 = decoder3to8(True, False, False)
    assert d7 is False
    assert d6 is False
    assert d5 is False
    assert d4 is True
    assert d3 is False
    assert d2 is False
    assert d1 is False
    assert d0 is False

def test_decoder3to8_a2_true_a1_false_a0_true(decoder3to8: Decoder3To8):
    d7, d6, d5, d4, d3, d2, d1, d0 = decoder3to8(True, False, True)
    assert d7 is False
    assert d6 is False
    assert d5 is True
    assert d4 is False
    assert d3 is False
    assert d2 is False
    assert d1 is False
    assert d0 is False

def test_decoder3to8_a2_true_a1_true_a0_false(decoder3to8: Decoder3To8):
    d7, d6, d5, d4, d3, d2, d1, d0 = decoder3to8(True, True, False)
    assert d7 is False
    assert d6 is True
    assert d5 is False
    assert d4 is False
    assert d3 is False
    assert d2 is False
    assert d1 is False
    assert d0 is False

def test_decoder3to8_a2_true_a1_true_a0_true(decoder3to8: Decoder3To8):
    d7, d6, d5, d4, d3, d2, d1, d0 = decoder3to8(True, True, True)
    assert d7 is True
    assert d6 is False
    assert d5 is False
    assert d4 is False
    assert d3 is False
    assert d2 is False
    assert d1 is False
    assert d0 is False
