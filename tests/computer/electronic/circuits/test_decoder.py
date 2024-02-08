"""
Test for Decoders
"""
import pytest
from computer.electronic.circuits.decoder import Decoder2To4, Decoder3To8, Decoder4To16, Decoder5To32, Decoder6To64, Decoder7To128, Decoder8To256

# pylint: disable=C0116,R1702

@pytest.fixture(name="decoder2to4")
def fixture_decoder2to4():
    return Decoder2To4()

@pytest.fixture(name="decoder3to8")
def fixture_decoder3to8():
    return Decoder3To8()

@pytest.fixture(name="decoder4to16")
def fixture_decoder4to16():
    return Decoder4To16()

@pytest.fixture(name="decoder5to32")
def fixture_decoder5to32():
    return Decoder5To32()

@pytest.fixture(name="decoder6to64")
def fixture_decoder6to64():
    return Decoder6To64()

@pytest.fixture(name="decoder7to128")
def fixture_decoder7to128():
    return Decoder7To128()

@pytest.fixture(name="decoder8to256")
def fixture_decoder8to256():
    return Decoder8To256()


def test_decoder2to4_a1_false_a0_false_enabled(decoder2to4: Decoder2To4):
    d3, d2, d1, d0 = decoder2to4(False, False, True)
    assert d3 is False
    assert d2 is False
    assert d1 is False
    assert d0 is True

def test_decoder2to4_a1_false_a0_true_enabled(decoder2to4: Decoder2To4):
    d3, d2, d1, d0 = decoder2to4(False, True, True)
    assert d3 is False
    assert d2 is False
    assert d1 is True
    assert d0 is False

def test_decoder2to4_a1_true_a0_false_enabled(decoder2to4: Decoder2To4):
    d3, d2, d1, d0 = decoder2to4(True, False, True)
    assert d3 is False
    assert d2 is True
    assert d1 is False
    assert d0 is False

def test_decoder2to4_a1_true_a0_true_enabled(decoder2to4: Decoder2To4):
    d3, d2, d1, d0 = decoder2to4(True, True, True)
    assert d3 is True
    assert d2 is False
    assert d1 is False
    assert d0 is False

def test_decoder2to4_a1_false_a0_false_disabled(decoder2to4: Decoder2To4):
    d3, d2, d1, d0 = decoder2to4(False, False, False)
    assert d3 is False
    assert d2 is False
    assert d1 is False
    assert d0 is False

def test_decoder2to4_a1_false_a0_true_disabled(decoder2to4: Decoder2To4):
    d3, d2, d1, d0 = decoder2to4(False, True, False)
    assert d3 is False
    assert d2 is False
    assert d1 is False
    assert d0 is False

def test_decoder2to4_a1_true_a0_false_disabled(decoder2to4: Decoder2To4):
    d3, d2, d1, d0 = decoder2to4(True, False, False)
    assert d3 is False
    assert d2 is False
    assert d1 is False
    assert d0 is False

def test_decoder2to4_a1_true_a0_true_disabled(decoder2to4: Decoder2To4):
    d3, d2, d1, d0 = decoder2to4(True, True, False)
    assert d3 is False
    assert d2 is False
    assert d1 is False
    assert d0 is False

def test_decoder3to8_a2_false_a1_false_a0_false_enabled(decoder3to8: Decoder3To8):
    d7, d6, d5, d4, d3, d2, d1, d0 = decoder3to8(False, False, False, True)
    assert d7 is False
    assert d6 is False
    assert d5 is False
    assert d4 is False
    assert d3 is False
    assert d2 is False
    assert d1 is False
    assert d0 is True

def test_decoder3to8_a2_false_a1_false_a0_true_enabled(decoder3to8: Decoder3To8):
    d7, d6, d5, d4, d3, d2, d1, d0 = decoder3to8(False, False, True, True)
    assert d7 is False
    assert d6 is False
    assert d5 is False
    assert d4 is False
    assert d3 is False
    assert d2 is False
    assert d1 is True
    assert d0 is False

def test_decoder3to8_a2_false_a1_true_a0_false_enabled(decoder3to8: Decoder3To8):
    d7, d6, d5, d4, d3, d2, d1, d0 = decoder3to8(False, True, False, True)
    assert d7 is False
    assert d6 is False
    assert d5 is False
    assert d4 is False
    assert d3 is False
    assert d2 is True
    assert d1 is False
    assert d0 is False

def test_decoder3to8_a2_false_a1_true_a0_true_enabled(decoder3to8: Decoder3To8):
    d7, d6, d5, d4, d3, d2, d1, d0 = decoder3to8(False, True, True, True)
    assert d7 is False
    assert d6 is False
    assert d5 is False
    assert d4 is False
    assert d3 is True
    assert d2 is False
    assert d1 is False
    assert d0 is False

def test_decoder3to8_a2_true_a1_false_a0_false_enabled(decoder3to8: Decoder3To8):
    d7, d6, d5, d4, d3, d2, d1, d0 = decoder3to8(True, False, False, True)
    assert d7 is False
    assert d6 is False
    assert d5 is False
    assert d4 is True
    assert d3 is False
    assert d2 is False
    assert d1 is False
    assert d0 is False

def test_decoder3to8_a2_true_a1_false_a0_true_enabled(decoder3to8: Decoder3To8):
    d7, d6, d5, d4, d3, d2, d1, d0 = decoder3to8(True, False, True, True)
    assert d7 is False
    assert d6 is False
    assert d5 is True
    assert d4 is False
    assert d3 is False
    assert d2 is False
    assert d1 is False
    assert d0 is False

def test_decoder3to8_a2_true_a1_true_a0_false_enabled(decoder3to8: Decoder3To8):
    d7, d6, d5, d4, d3, d2, d1, d0 = decoder3to8(True, True, False, True)
    assert d7 is False
    assert d6 is True
    assert d5 is False
    assert d4 is False
    assert d3 is False
    assert d2 is False
    assert d1 is False
    assert d0 is False

def test_decoder3to8_a2_true_a1_true_a0_true_enabled(decoder3to8: Decoder3To8):
    d7, d6, d5, d4, d3, d2, d1, d0 = decoder3to8(True, True, True, True)
    assert d7 is True
    assert d6 is False
    assert d5 is False
    assert d4 is False
    assert d3 is False
    assert d2 is False
    assert d1 is False
    assert d0 is False

def test_decoder3to8_a2_false_a1_false_a0_false_disabled(decoder3to8: Decoder3To8):
    d7, d6, d5, d4, d3, d2, d1, d0 = decoder3to8(False, False, False, False)
    assert d7 is False
    assert d6 is False
    assert d5 is False
    assert d4 is False
    assert d3 is False
    assert d2 is False
    assert d1 is False
    assert d0 is False

def test_decoder3to8_a2_false_a1_false_a0_true_disabled(decoder3to8: Decoder3To8):
    d7, d6, d5, d4, d3, d2, d1, d0 = decoder3to8(False, False, True, False)
    assert d7 is False
    assert d6 is False
    assert d5 is False
    assert d4 is False
    assert d3 is False
    assert d2 is False
    assert d1 is False
    assert d0 is False

def test_decoder3to8_a2_false_a1_true_a0_false_disabled(decoder3to8: Decoder3To8):
    d7, d6, d5, d4, d3, d2, d1, d0 = decoder3to8(False, True, False, False)
    assert d7 is False
    assert d6 is False
    assert d5 is False
    assert d4 is False
    assert d3 is False
    assert d2 is False
    assert d1 is False
    assert d0 is False

def test_decoder3to8_a2_false_a1_true_a0_true_disabled(decoder3to8: Decoder3To8):
    d7, d6, d5, d4, d3, d2, d1, d0 = decoder3to8(False, True, True, False)
    assert d7 is False
    assert d6 is False
    assert d5 is False
    assert d4 is False
    assert d3 is False
    assert d2 is False
    assert d1 is False
    assert d0 is False

def test_decoder3to8_a2_true_a1_false_a0_false_disabled(decoder3to8: Decoder3To8):
    d7, d6, d5, d4, d3, d2, d1, d0 = decoder3to8(True, False, False, False)
    assert d7 is False
    assert d6 is False
    assert d5 is False
    assert d4 is False
    assert d3 is False
    assert d2 is False
    assert d1 is False
    assert d0 is False

def test_decoder3to8_a2_true_a1_false_a0_true_disabled(decoder3to8: Decoder3To8):
    d7, d6, d5, d4, d3, d2, d1, d0 = decoder3to8(True, False, True, False)
    assert d7 is False
    assert d6 is False
    assert d5 is False
    assert d4 is False
    assert d3 is False
    assert d2 is False
    assert d1 is False
    assert d0 is False

def test_decoder3to8_a2_true_a1_true_a0_false_disabled(decoder3to8: Decoder3To8):
    d7, d6, d5, d4, d3, d2, d1, d0 = decoder3to8(True, True, False, False)
    assert d7 is False
    assert d6 is False
    assert d5 is False
    assert d4 is False
    assert d3 is False
    assert d2 is False
    assert d1 is False
    assert d0 is False

def test_decoder3to8_a2_true_a1_true_a0_true_disabled(decoder3to8: Decoder3To8):
    d7, d6, d5, d4, d3, d2, d1, d0 = decoder3to8(True, True, True, False)
    assert d7 is False
    assert d6 is False
    assert d5 is False
    assert d4 is False
    assert d3 is False
    assert d2 is False
    assert d1 is False
    assert d0 is False

def test_decoder4to16_enabled(decoder4to16: Decoder4To16):
    bit_true_index = 0
    for a3 in [False, True]:
        for a2 in [False, True]:
            for a1 in [False, True]:
                for a0 in [False, True]:
                    bits = decoder4to16(a3, a2, a1, a0, True)

                    for bit_index, bit in enumerate(bits[::-1]):
                        if bit_index == bit_true_index:
                            assert bit is True, f"Inputs: a3={a3}, a2={a2}, a1={a1}, a0={a0}"
                        else:
                            assert bit is False, f"Inputs: a3={a3}, a2={a2}, a1={a1}, a0={a0}"

                    bit_true_index += 1

def test_decoder5to32_enabled(decoder5to32: Decoder5To32):
    bit_true_index = 0
    for a4 in [False, True]:
        for a3 in [False, True]:
            for a2 in [False, True]:
                for a1 in [False, True]:
                    for a0 in [False, True]:
                        bits = decoder5to32(a4, a3, a2, a1, a0, True)

                        for bit_index, bit in enumerate(bits[::-1]):
                            if bit_index == bit_true_index:
                                assert bit is True, f"Inputs: a4={a4}, a3={a3}, a2={a2}, a1={a1}, a0={a0}"
                            else:
                                assert bit is False, f"Inputs: a4={a4}, a3={a3}, a2={a2}, a1={a1}, a0={a0}"

                        bit_true_index += 1

def test_decoder6to64_enabled(decoder6to64: Decoder6To64):
    bit_true_index = 0
    for a5 in [False, True]:
        for a4 in [False, True]:
            for a3 in [False, True]:
                for a2 in [False, True]:
                    for a1 in [False, True]:
                        for a0 in [False, True]:
                            bits = decoder6to64(a5, a4, a3, a2, a1, a0, True)

                            for bit_index, bit in enumerate(bits[::-1]):
                                if bit_index == bit_true_index:
                                    assert bit is True, f"Inputs: a5={a5}, a4={a4}, a3={a3}, a2={a2}, a1={a1}, a0={a0}"
                                else:
                                    assert bit is False, f"Inputs: a5={a5}, a4={a4}, a3={a3}, a2={a2}, a1={a1}, a0={a0}"

                            bit_true_index += 1

def test_decoder7to128_enabled(decoder7to128: Decoder7To128):
    bit_true_index = 0
    for a6 in [False, True]:
        for a5 in [False, True]:
            for a4 in [False, True]:
                for a3 in [False, True]:
                    for a2 in [False, True]:
                        for a1 in [False, True]:
                            for a0 in [False, True]:
                                bits = decoder7to128(a6, a5, a4, a3, a2, a1, a0, True)

                                for bit_index, bit in enumerate(bits[::-1]):
                                    if bit_index == bit_true_index:
                                        assert bit is True, f"Inputs: a6={a6}, a5={a5}, a4={a4}, a3={a3}, a2={a2}, a1={a1}, a0={a0}"
                                    else:
                                        assert bit is False, f"Inputs: a6={a6}, a5={a5}, a4={a4}, a3={a3}, a2={a2}, a1={a1}, a0={a0}"

                                bit_true_index += 1

def test_decoder8to256_enabled(decoder8to256: Decoder8To256):
    bit_true_index = 0
    for a7 in [False, True]:
        for a6 in [False, True]:
            for a5 in [False, True]:
                for a4 in [False, True]:
                    for a3 in [False, True]:
                        for a2 in [False, True]:
                            for a1 in [False, True]:
                                for a0 in [False, True]:
                                    bits = decoder8to256(a7, a6, a5, a4, a3, a2, a1, a0, True)

                                    for bit_index, bit in enumerate(bits[::-1]):
                                        if bit_index == bit_true_index:
                                            assert bit is True, f"Inputs: a7={a7}, a6={a6}, a5={a5}, a4={a4}, a3={a3}, a2={a2}, a1={a1}, a0={a0}"
                                        else:
                                            assert bit is False, f"Inputs: a7={a7}, a6={a6}, a5={a5}, a4={a4}, a3={a3}, a2={a2}, a1={a1}, a0={a0}"

                                    bit_true_index += 1
