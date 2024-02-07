"""
Test for CMOS logic gates
"""
import pytest
from computer.electronic.circuits.cmos import ANDGate, ANDGate3, NANDGate, NORGate, NOTGate, ORGate, XNORGate, XORGate


# pylint: disable=C0116

@pytest.fixture(name="cmos_not_gate")
def fixture_cmos_not_gate():
    return NOTGate()

@pytest.fixture(name="cmos_nand_gate")
def fixture_cmos_nand_gate():
    return NANDGate()

@pytest.fixture(name="cmos_nor_gate")
def fixture_cmos_nor_gate():
    return NORGate()

@pytest.fixture(name="cmos_and_gate")
def fixture_cmos_and_gate():
    return ANDGate()

@pytest.fixture(name="cmos_and_gate3")
def fixture_cmos_and_gate3():
    return ANDGate3()

@pytest.fixture(name="cmos_or_gate")
def fixture_cmos_or_gate():
    return ORGate()

@pytest.fixture(name="cmos_xor_gate")
def fixture_cmos_xor_gate():
    return XORGate()

@pytest.fixture(name="cmos_xnor_gate")
def fixture_cmos_xnor_gate():
    return XNORGate()


def test_not_gate_true(cmos_not_gate: NOTGate):
    assert cmos_not_gate(True) is False

def test_not_gate_false(cmos_not_gate: NOTGate):
    assert cmos_not_gate(False) is True

def test_nand_gate_a_false_b_false(cmos_nand_gate: NANDGate):
    assert cmos_nand_gate(False, False) is True

def test_nand_gate_a_true_b_false(cmos_nand_gate: NANDGate):
    assert cmos_nand_gate(True, False) is True

def test_nand_gate_a_false_b_true(cmos_nand_gate: NANDGate):
    assert cmos_nand_gate(False, True) is True

def test_nand_gate_a_true_b_true(cmos_nand_gate: NANDGate):
    assert cmos_nand_gate(True, True) is False

def test_nor_gate_a_false_b_false(cmos_nor_gate: NORGate):
    assert cmos_nor_gate(False, False) is True

def test_nor_gate_a_true_b_false(cmos_nor_gate: NORGate):
    assert cmos_nor_gate(True, False) is False

def test_nor_gate_a_false_b_true(cmos_nor_gate: NORGate):
    assert cmos_nor_gate(False, True) is False

def test_nor_gate_a_true_b_true(cmos_nor_gate: NORGate):
    assert cmos_nor_gate(True, True) is False

def test_and_gate_a_false_b_false(cmos_and_gate: ANDGate):
    assert cmos_and_gate(False, False) is False

def test_and_gate_a_true_b_false(cmos_and_gate: ANDGate):
    assert cmos_and_gate(True, False) is False

def test_and_gate_a_false_b_true(cmos_and_gate: ANDGate):
    assert cmos_and_gate(False, True) is False

def test_and_gate_a_true_b_true(cmos_and_gate: ANDGate):
    assert cmos_and_gate(True, True) is True

def test_and_gate3_a_false_b_false_c_false(cmos_and_gate3: ANDGate3):
    assert cmos_and_gate3(False, False, False) is False

def test_and_gate3_a_false_b_false_c_true(cmos_and_gate3: ANDGate3):
    assert cmos_and_gate3(False, False, True) is False

def test_and_gate3_a_true_b_false_c_false(cmos_and_gate3: ANDGate3):
    assert cmos_and_gate3(True, False, False) is False

def test_and_gate3_a_true_b_false_c_true(cmos_and_gate3: ANDGate3):
    assert cmos_and_gate3(True, False, True) is False

def test_and_gate3_a_false_b_true_c_false(cmos_and_gate3: ANDGate3):
    assert cmos_and_gate3(False, True, False) is False

def test_and_gate3_a_false_b_true_c_true(cmos_and_gate3: ANDGate3):
    assert cmos_and_gate3(False, True, True) is False

def test_and_gate3_a_true_b_true_c_false(cmos_and_gate3: ANDGate3):
    assert cmos_and_gate3(True, True, False) is False

def test_and_gate3_a_true_b_true_c_true(cmos_and_gate3: ANDGate3):
    assert cmos_and_gate3(True, True, True) is True

def test_or_gate_a_false_b_false(cmos_or_gate: ORGate):
    assert cmos_or_gate(False, False) is False

def test_or_gate_a_true_b_false(cmos_or_gate: ORGate):
    assert cmos_or_gate(True, False) is True

def test_or_gate_a_false_b_true(cmos_or_gate: ORGate):
    assert cmos_or_gate(False, True) is True

def test_or_gate_a_true_b_true(cmos_or_gate: ORGate):
    assert cmos_or_gate(True, True) is True

def test_xor_gate_a_false_b_false(cmos_xor_gate: XORGate):
    assert cmos_xor_gate(False, False) is False

def test_xor_gate_a_true_b_false(cmos_xor_gate: XORGate):
    assert cmos_xor_gate(True, False) is True

def test_xor_gate_a_false_b_true(cmos_xor_gate: XORGate):
    assert cmos_xor_gate(False, True) is True

def test_xor_gate_a_true_b_true(cmos_xor_gate: XORGate):
    assert cmos_xor_gate(True, True) is False

def test_xnor_gate_a_false_b_false(cmos_xnor_gate: XNORGate):
    assert cmos_xnor_gate(False, False) is True

def test_xnor_gate_a_true_b_false(cmos_xnor_gate: XNORGate):
    assert cmos_xnor_gate(True, False) is False

def test_xnor_gate_a_false_b_true(cmos_xnor_gate: XNORGate):
    assert cmos_xnor_gate(False, True) is False

def test_xnor_gate_a_true_b_true(cmos_xnor_gate: XNORGate):
    assert cmos_xnor_gate(True, True) is True
