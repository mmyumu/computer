"""
Test for Flip Flops
"""
import pytest
from computer.logic_gates.flip_flop import DFlipFlop, SRFlipFlop

# pylint: disable=C0116

@pytest.fixture(name="srflipflop")
def fixture_srflipflop():
    return SRFlipFlop()

@pytest.fixture(name="dflipflop")
def fixture_dflipflop():
    return DFlipFlop()

def test_srflipflop_set0_reset0(srflipflop: SRFlipFlop):
    srflipflop.reset_states()
    assert srflipflop(False, False) == (False, True)

def test_srflipflop_set0_reset1(srflipflop: SRFlipFlop):
    srflipflop.reset_states()
    assert srflipflop(False, True) == (False, True)

def test_srflipflop_set1_reset0(srflipflop: SRFlipFlop):
    srflipflop.reset_states()
    assert srflipflop(True, False) == (True, False)

def test_srflipflop_set1_reset1(srflipflop: SRFlipFlop):
    with pytest.raises(ValueError):
        srflipflop(True, True)

def test_dflipflop_set0_clock0(dflipflop: DFlipFlop):
    dflipflop.reset_states()
    assert dflipflop(False, False) == (False, True)

def test_dflipflop_set0_clock1(dflipflop: DFlipFlop):
    dflipflop.reset_states()
    assert dflipflop(False, True) == (False, True)

def test_dflipflop_set1_clock0(dflipflop: DFlipFlop):
    dflipflop.reset_states()
    assert dflipflop(True, False) == (False, True)

def test_dflipflop_set1_clock1(dflipflop: DFlipFlop):
    dflipflop.reset_states()
    assert dflipflop(True, True) == (True, False)

def test_dflipflop_memory_sequence(dflipflop: DFlipFlop):
    dflipflop.reset_states()

    # Initial state
    assert dflipflop(False, False) == (False, True)

    # Set new state
    assert dflipflop(True, True) == (True, False)

    # Memorized previous state
    assert dflipflop(False, False) == (True, False)
