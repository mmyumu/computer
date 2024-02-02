"""
Test for Adders
"""
import pytest
from computer.logic_gates.adder import FullAdder, HalfAdder

# pylint: disable=C0116

@pytest.fixture(name="half_adder")
def fixture_half_adder():
    return HalfAdder()

@pytest.fixture(name="full_adder")
def fixture_full_adder():
    return FullAdder()


def test_halfadder_a_false_b_false(half_adder: HalfAdder):
    sum_result, carry = half_adder(False, False)
    assert sum_result is False
    assert carry is False

def test_halfadder_a_true_b_false(half_adder: HalfAdder):
    sum_result, carry = half_adder(True, False)
    assert sum_result is True
    assert carry is False

def test_halfadder_a_false_b_true(half_adder: HalfAdder):
    sum_result, carry = half_adder(False, True)
    assert sum_result is True
    assert carry is False

def test_halfadder_a_true_b_true(half_adder: HalfAdder):
    sum_result, carry = half_adder(True, True)
    assert sum_result is False
    assert carry is True

def test_fulladder_a_false_b_false_c_false(full_adder: FullAdder):
    sum_result, carry = full_adder(False, False, False)
    assert sum_result is False
    assert carry is False

def test_fulladder_a_false_b_false_c_true(full_adder: FullAdder):
    sum_result, carry = full_adder(False, False, True)
    assert sum_result is True
    assert carry is False

def test_fulladder_a_false_b_true_c_false(full_adder: FullAdder):
    sum_result, carry = full_adder(False, True, False)
    assert sum_result is True
    assert carry is False

def test_fulladder_a_false_b_true_c_true(full_adder: FullAdder):
    sum_result, carry = full_adder(False, True, True)
    assert sum_result is False
    assert carry is True

def test_fulladder_a_true_b_false_c_false(full_adder: FullAdder):
    sum_result, carry = full_adder(True, False, False)
    assert sum_result is True
    assert carry is False

def test_fulladder_a_true_b_false_c_true(full_adder: FullAdder):
    sum_result, carry = full_adder(True, False, True)
    assert sum_result is False
    assert carry is True

def test_fulladder_a_true_b_true_c_false(full_adder: FullAdder):
    sum_result, carry = full_adder(True, True, False)
    assert sum_result is False
    assert carry is True

def test_fulladder_a_true_b_true_c_true(full_adder: FullAdder):
    sum_result, carry = full_adder(True, True, True)
    assert sum_result is True
    assert carry is True
