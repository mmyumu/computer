"""
Test combination of mux/demux
"""
import pytest
from computer.logic_gates.demux import DEMUX1To2, DEMUX1To4

from computer.logic_gates.mux import MUX2To1, MUX4To1

# pylint: disable=C0116

@pytest.fixture(name="mux2to1")
def fixture_mux2to1():
    return MUX2To1()

@pytest.fixture(name="mux4to1")
def fixture_mux4to1():
    return MUX4To1()

@pytest.fixture(name="demux1to2")
def fixture_demux1to2():
    return DEMUX1To2()

@pytest.fixture(name="demux1to4")
def fixture_demux1to4():
    return DEMUX1To4()

def test_mux1to2_demux2to1(mux2to1: MUX2To1, demux1to2: DEMUX1To2):
    for a0 in [False, True]:
        for a1 in [False, True]:
            for s in [False, True]:
                assert demux1to2(mux2to1(a0, a1, s), s), f"Inputs: a0={a0}, a1={a1}"

def test_mux1to4_demux4to1(mux4to1: MUX4To1, demux1to4: DEMUX1To4):
    for a0 in [False, True]:
        for a1 in [False, True]:
            for a2 in [False, True]:
                for a3 in [False, True]:
                    for s0 in [False, True]:
                        for s1 in [False, True]:
                            assert demux1to4(mux4to1(a0, a1, a2, a3, s0, s1), s0, s1), f"Inputs: a0={a0}, a1={a1}"
