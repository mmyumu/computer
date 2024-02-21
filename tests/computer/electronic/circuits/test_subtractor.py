"""
Test for Adders
"""
import pytest
from computer.electronic.circuits.subtractor import FullSubtractor, FullSubtractorRestore, HalfSubtractor

# pylint: disable=C0116,R1702

@pytest.fixture(name="half_subtractor")
def fixture_half_subtractor():
    return HalfSubtractor()

@pytest.fixture(name="full_subtractor")
def fixture_full_subtractor():
    return FullSubtractor()

@pytest.fixture(name="full_subtractor_restore")
def fixture_full_subtractor_restore():
    return FullSubtractorRestore()

def test_halfsubtractor_a_false_b_false(half_subtractor: HalfSubtractor):
    difference, borrow = half_subtractor(False, False)
    assert difference is False
    assert borrow is False

def test_halfsubtractor_a_true_b_false(half_subtractor: HalfSubtractor):
    difference, borrow = half_subtractor(True, False)
    assert difference is True
    assert borrow is False

def test_halfsubtractor_a_false_b_true(half_subtractor: HalfSubtractor):
    difference, borrow = half_subtractor(False, True)
    assert difference is True
    assert borrow is True

def test_halfsubtractor_a_true_b_true(half_subtractor: HalfSubtractor):
    difference, borrow = half_subtractor(True, True)
    assert difference is False
    assert borrow is False

def test_fullsubtractor_a_false_b_false_c_false(full_subtractor: FullSubtractor):
    difference, borrow = full_subtractor(False, False, False)
    assert difference is False
    assert borrow is False

def test_fullsubtractor_a_false_b_false_c_true(full_subtractor: FullSubtractor):
    difference, borrow = full_subtractor(False, False, True)
    assert difference is True
    assert borrow is True

def test_fullsubtractor_a_false_b_true_c_false(full_subtractor: FullSubtractor):
    difference, borrow = full_subtractor(False, True, False)
    assert difference is True
    assert borrow is True

def test_fullsubtractor_a_false_b_true_c_true(full_subtractor: FullSubtractor):
    difference, borrow = full_subtractor(False, True, True)
    assert difference is False
    assert borrow is True

def test_fullsubtractor_a_true_b_false_c_false(full_subtractor: FullSubtractor):
    difference, borrow = full_subtractor(True, False, False)
    assert difference is True
    assert borrow is False

def test_fullsubtractor_a_true_b_false_c_true(full_subtractor: FullSubtractor):
    difference, borrow = full_subtractor(True, False, True)
    assert difference is False
    assert borrow is False

def test_fullsubtractor_a_true_b_true_c_false(full_subtractor: FullSubtractor):
    difference, borrow = full_subtractor(True, True, False)
    assert difference is False
    assert borrow is False

def test_fullsubtractor_a_true_b_true_c_true(full_subtractor: FullSubtractor):
    difference, borrow = full_subtractor(True, True, True)
    assert difference is True
    assert borrow is True

def test_fullsubtractorrestore(full_subtractor_restore: FullSubtractorRestore):
    for a in [False, True]:
        for b in [False, True]:
            for borrow_in in [False, True]:
                for carry in [False, True]:
                    result, borrow_out = full_subtractor_restore(a, b, borrow_in, carry)

                    if carry:
                        if a < b + borrow_in:
                            assert borrow_out is True, f"Inputs: a={a}, b={b}, borrow_in={borrow_in}, carry={carry}"
                        assert result is ((a + b + borrow_in) % 2 != 0)
                    else:
                        assert result == a, f"Inputs: a={a}, b={b}, borrow_in={borrow_in}, carry={carry}"
