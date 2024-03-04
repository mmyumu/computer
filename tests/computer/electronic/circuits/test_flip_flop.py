"""
Test for Flip Flops
"""
import pytest
from computer.electronic.circuits.flip_flop import DFlipFlop, SRFlipFlop

# pylint: disable=C0116,W0212,C2801

@pytest.fixture(name="srflipflop")
def fixture_srflipflop():
    return SRFlipFlop()

@pytest.fixture(name="dflipflop")
def fixture_dflipflop():
    return DFlipFlop()

def test_srflipflop_set0_reset0(srflipflop: SRFlipFlop):
    srflipflop.reset_states()
    srflipflop.set_sr(False, False)
    assert srflipflop.output == (False, True)
    assert srflipflop.clock_tick(True) == (False, True)

def test_srflipflop_set0_reset1(srflipflop: SRFlipFlop):
    srflipflop.reset_states()
    srflipflop.set_sr(False, True)
    assert srflipflop.output == (False, True)
    assert srflipflop.clock_tick(True) == (False, True)

def test_srflipflop_set1_reset0(srflipflop: SRFlipFlop):
    srflipflop.reset_states()
    srflipflop.set_sr(True, False)
    assert srflipflop.output == (False, True)
    assert srflipflop.clock_tick(True) == (True, False)

def test_srflipflop_set1_reset1(srflipflop: SRFlipFlop):
    srflipflop.set_sr(True, True)
    with pytest.raises(ValueError):
        srflipflop.clock_tick(True)

def test_srflipflop_memory_sequence(srflipflop: SRFlipFlop):
    srflipflop.reset_states()

    assert srflipflop.output == (False, True)

    # Initial state
    assert srflipflop.clock_tick(False) == (False, True)

    # Set new state: 1
    srflipflop.set_sr(True, False)
    assert srflipflop.clock_tick(False) == (False, True)
    assert srflipflop.clock_tick(True) == (True, False)

    # Memorized previous state
    assert srflipflop.output == (True, False)
    assert srflipflop.clock_tick(False) == (True, False)

    # Set new state: 0
    srflipflop.set_sr(False, True)
    assert srflipflop.output == (True, False)
    assert srflipflop.clock_tick(True) == (False, True)

def test_srflipflop_str(srflipflop: SRFlipFlop):
    srflipflop.__str__()

def test_dflipflop_set0_clock0(dflipflop: DFlipFlop):
    dflipflop.reset_states()
    dflipflop.set_d(False)
    assert dflipflop.output == (False, True)
    assert dflipflop.clock_tick(False) == (False, True)

def test_dflipflop_set0_clock1(dflipflop: DFlipFlop):
    dflipflop.reset_states()
    dflipflop.set_d(False)
    assert dflipflop.clock_tick(True) == (False, True)

def test_dflipflop_set1_clock0(dflipflop: DFlipFlop):
    dflipflop.reset_states()
    dflipflop.set_d(True)
    assert dflipflop.clock_tick(False) == (False, True)

def test_dflipflop_set1_clock1(dflipflop: DFlipFlop):
    dflipflop.reset_states()
    dflipflop.set_d(True)
    assert dflipflop.clock_tick(True) == (True, False)

def test_dflipflop_set0_clock0_initial_q1_qbar0(dflipflop: DFlipFlop):
    dflipflop.q = True
    dflipflop.q_bar = False

    dflipflop.set_d(False)
    assert dflipflop.clock_tick(False) == (True, False)

def test_dflipflop_set0_clock1_initial_q1_qbar0(dflipflop: DFlipFlop):
    dflipflop.q = True
    dflipflop.q_bar = False

    dflipflop.set_d(False)
    assert dflipflop.clock_tick(True) == (False, True)

def test_dflipflop_set1_clock0_initial_q1_qbar0(dflipflop: DFlipFlop):
    dflipflop.q = True
    dflipflop.q_bar = False

    dflipflop.set_d(True)
    assert dflipflop.clock_tick(False) == (True, False)

def test_dflipflop_set1_clock1_initial_q1_qbar0(dflipflop: DFlipFlop):
    dflipflop.q = True
    dflipflop.q_bar = False

    dflipflop.set_d(True)
    assert dflipflop.clock_tick(True) == (True, False)

def test_dflipflop_memory_sequence(dflipflop: DFlipFlop):
    dflipflop.reset_states()

    # Initial state
    dflipflop.set_d(False)
    assert dflipflop.clock_tick(False) == (False, True)

    # Set new state: 1
    dflipflop.set_d(True)
    assert dflipflop.clock_tick(True) == (True, False)

    # Memorized previous state
    assert dflipflop.clock_tick(False) == (True, False)

    # Set new state: 0
    dflipflop.set_d(False)
    assert dflipflop.clock_tick(True) == (False, True)

def test_dflipflop_unstable_initial_state_true(dflipflop: DFlipFlop):
    #This state should be avoided
    dflipflop.q = True
    dflipflop.q_bar = True

    # Initial state
    dflipflop.set_d(False)
    assert dflipflop.clock_tick(False) == (True, False)
    assert dflipflop.clock_tick(False) == (True, False)

def test_dflipflop_unstable_initial_state_false(dflipflop: DFlipFlop):
    #This state should be avoided
    dflipflop.q = False
    dflipflop.q_bar = False

    # Initial state
    dflipflop.set_d(False)
    assert dflipflop.clock_tick(False) == (False, True)
    assert dflipflop.clock_tick(False) == (False, True)


def test_dflipflop_str(dflipflop: DFlipFlop):
    dflipflop.__str__()
