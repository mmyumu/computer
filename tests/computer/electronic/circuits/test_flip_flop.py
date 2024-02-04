"""
Test for Flip Flops
"""
import pytest
from computer.electronic.circuits.flip_flop import DFlipFlop, SRFlipFlop

# pylint: disable=C0116,W0212

@pytest.fixture(name="srflipflop")
def fixture_srflipflop():
    return SRFlipFlop()

@pytest.fixture(name="dflipflop")
def fixture_dflipflop():
    return DFlipFlop()

def test_srflipflop_set0_reset0(srflipflop: SRFlipFlop):
    srflipflop.reset_states()
    assert srflipflop(False, False, True) == (False, True)

def test_srflipflop_set0_reset1(srflipflop: SRFlipFlop):
    srflipflop.reset_states()
    assert srflipflop(False, True, True) == (False, True)

def test_srflipflop_set1_reset0(srflipflop: SRFlipFlop):
    srflipflop.reset_states()
    srflipflop(True, False, True)
    assert srflipflop(True, False, True) == (True, False)

def test_srflipflop_set1_reset1(srflipflop: SRFlipFlop):
    with pytest.raises(ValueError):
        srflipflop(True, True, True)

def test_srflipflop_memory_sequence(srflipflop: SRFlipFlop):
    srflipflop.reset_states()

    # Initial state
    assert srflipflop(False, False, False) == (False, True)
    assert srflipflop(False, False, False) == (False, True)

    # Set new state: 1
    srflipflop(True, False, True)
    assert srflipflop(True, False, True) == (True, False)

    # Memorized previous state
    assert srflipflop(False, False, False) == (True, False)
    assert srflipflop(False, False, False) == (True, False)

    # Set new state: 0
    srflipflop(False, True, True)
    assert srflipflop(False, True, True) == (False, True)

def test_dflipflop_set0_clock0(dflipflop: DFlipFlop):
    dflipflop.reset_states()
    assert dflipflop(False, False) == (False, True)
    assert dflipflop(False, False) == (False, True)

def test_dflipflop_set0_clock1(dflipflop: DFlipFlop):
    dflipflop.reset_states()
    assert dflipflop(False, True) == (False, True)
    assert dflipflop(False, True) == (False, True)


def test_dflipflop_set1_clock0(dflipflop: DFlipFlop):
    dflipflop.reset_states()
    assert dflipflop(True, False) == (False, True)
    assert dflipflop(True, False) == (False, True)

def test_dflipflop_set1_clock1(dflipflop: DFlipFlop):
    dflipflop.reset_states()
    dflipflop(True, True)
    assert dflipflop(True, True) == (True, False)

def test_dflipflop_set0_clock0_initial_q1_qbar0(dflipflop: DFlipFlop):
    dflipflop._q = True
    dflipflop._q_bar = False
    assert dflipflop(False, False) == (True, False)

def test_dflipflop_set0_clock1_initial_q1_qbar0(dflipflop: DFlipFlop):
    dflipflop._q = True
    dflipflop._q_bar = False
    dflipflop(False, True)
    assert dflipflop(False, True) == (False, True)

def test_dflipflop_set1_clock0_initial_q1_qbar0(dflipflop: DFlipFlop):
    dflipflop._q = True
    dflipflop._q_bar = False
    assert dflipflop(True, False) == (True, False)
    assert dflipflop(True, False) == (True, False)

def test_dflipflop_set1_clock1_initial_q1_qbar0(dflipflop: DFlipFlop):
    dflipflop._q = True
    dflipflop._q_bar = False
    assert dflipflop(True, True) == (True, False)


def test_dflipflop_memory_sequence(dflipflop: DFlipFlop):
    dflipflop.reset_states()

    # Initial state
    assert dflipflop(False, False) == (False, True)
    assert dflipflop(False, False) == (False, True)

    # Set new state: 1
    dflipflop(True, True)
    assert dflipflop(True, True) == (True, False)

    # Memorized previous state
    assert dflipflop(False, False) == (True, False)
    assert dflipflop(False, False) == (True, False)

    # Set new state: 0
    dflipflop(False, True)
    assert dflipflop(False, True) == (False, True)

def test_dflipflop_unstable_initial_state_true(dflipflop: DFlipFlop):
    #This state should be avoided
    dflipflop._q = True
    dflipflop._q_bar = True

    # Initial state
    assert dflipflop(False, False) == (False, False)
    assert dflipflop(False, False) == (True, True)
    assert dflipflop(False, False) == (False, False)
    assert dflipflop(False, False) == (True, True)

def test_dflipflop_unstable_initial_state_false(dflipflop: DFlipFlop):
    #This state should be avoided
    dflipflop._q = False
    dflipflop._q_bar = False

    # Initial state
    assert dflipflop(False, False) == (True, True)
    assert dflipflop(False, False) == (False, False)
    assert dflipflop(False, False) == (True, True)
    assert dflipflop(False, False) == (False, False)
