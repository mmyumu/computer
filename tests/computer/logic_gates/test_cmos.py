"""
Test for CMOS logic gates
"""
import pytest
from computer.logic_gates.cmos import ANDGate, NANDGate, NORGate, NOTGate, ORGate, XORGate

# pylint: disable=C0116

@pytest.fixture(name="cmos_not_gate")
def fixture_cmos_not_gate():
    return NOTGate()

@pytest.fixture(name="cmos_nand_gate")
def fixture_cmod_nand_gate():
    return NANDGate()

@pytest.fixture(name="cmos_nor_gate")
def fixture_cmod_nor_gate():
    return NORGate()

@pytest.fixture(name="cmos_and_gate")
def fixture_cmod_and_gate():
    return ANDGate()

@pytest.fixture(name="cmos_or_gate")
def fixture_cmod_or_gate():
    return ORGate()

@pytest.fixture(name="cmos_xor_gate")
def fixture_cmod_xor_gate():
    return XORGate()


def test_not_gate_true(cmos_not_gate: NOTGate):
    assert cmos_not_gate.operate(True) is False

def test_not_gate_false(cmos_not_gate: NOTGate):
    assert cmos_not_gate.operate(False) is True

def test_nand_gate_a_false_b_false(cmos_nand_gate: NANDGate):
    assert cmos_nand_gate.operate(False, False) is True

def test_nand_gate_a_true_b_false(cmos_nand_gate: NANDGate):
    assert cmos_nand_gate.operate(True, False) is True

def test_nand_gate_a_false_b_true(cmos_nand_gate: NANDGate):
    assert cmos_nand_gate.operate(False, True) is True

def test_nand_gate_a_true_b_true(cmos_nand_gate: NANDGate):
    assert cmos_nand_gate.operate(True, True) is False

def test_nor_gate_a_false_b_false(cmos_nor_gate: NORGate):
    assert cmos_nor_gate.operate(False, False) is True

def test_nor_gate_a_true_b_false(cmos_nor_gate: NORGate):
    assert cmos_nor_gate.operate(True, False) is False

def test_nor_gate_a_false_b_true(cmos_nor_gate: NORGate):
    assert cmos_nor_gate.operate(False, True) is False

def test_nor_gate_a_true_b_true(cmos_nor_gate: NORGate):
    assert cmos_nor_gate.operate(True, True) is False

def test_and_gate_a_false_b_false(cmos_and_gate: ANDGate):
    assert cmos_and_gate.operate(False, False) is False

def test_and_gate_a_true_b_false(cmos_and_gate: ANDGate):
    assert cmos_and_gate.operate(True, False) is False

def test_and_gate_a_false_b_true(cmos_and_gate: ANDGate):
    assert cmos_and_gate.operate(False, True) is False

def test_and_gate_a_true_b_true(cmos_and_gate: ANDGate):
    assert cmos_and_gate.operate(True, True) is True

def test_or_gate_a_false_b_false(cmos_or_gate: ORGate):
    assert cmos_or_gate.operate(False, False) is False

def test_or_gate_a_true_b_false(cmos_or_gate: ORGate):
    assert cmos_or_gate.operate(True, False) is True

def test_or_gate_a_false_b_true(cmos_or_gate: ORGate):
    assert cmos_or_gate.operate(False, True) is True

def test_or_gate_a_true_b_true(cmos_or_gate: ORGate):
    assert cmos_or_gate.operate(True, True) is True

def test_xor_gate_a_false_b_false(cmos_xor_gate: XORGate):
    assert cmos_xor_gate.operate(False, False) is False

def test_xor_gate_a_true_b_false(cmos_xor_gate: XORGate):
    assert cmos_xor_gate.operate(True, False) is True

def test_xor_gate_a_false_b_true(cmos_xor_gate: XORGate):
    assert cmos_xor_gate.operate(False, True) is True

def test_xor_gate_a_true_b_true(cmos_xor_gate: XORGate):
    assert cmos_xor_gate.operate(True, True) is False
