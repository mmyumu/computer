"""
Test for multiplexers and demultiplexers
"""
import pytest
from computer.logic_gates.mux import MUX2To1, MUX4To1

# pylint: disable=C0116

@pytest.fixture(name="mux2to1")
def fixture_mux2to1():
    return MUX2To1()

@pytest.fixture(name="mux4to1")
def fixture_mux4to1():
    return MUX4To1()


def test_mux2to1(mux2to1: MUX2To1):
    for a0 in [False, True]:
        for a1 in [False, True]:
            assert mux2to1(a0, a1, False) == a0, f"Inputs: a0={a0}, a1={a1}"
            assert mux2to1(a0, a1, True) == a1, f"Inputs: a0={a0}, a1={a1}"

def test_mux4to1(mux4to1: MUX4To1):
    for a0 in [False, True]:
        for a1 in [False, True]:
            for a2 in [False, True]:
                for a3 in [False, True]:
                    assert mux4to1(a0, a1, a2, a3, False, False) == a0, f"Inputs: a0={a0}, a1={a1}, a2={a2}, a3={a3}"
                    assert mux4to1(a0, a1, a2, a3, False, True) == a1, f"Inputs: a0={a0}, a1={a1}, a2={a2}, a3={a3}"
                    assert mux4to1(a0, a1, a2, a3, True, False) == a2, f"Inputs: a0={a0}, a1={a1}, a2={a2}, a3={a3}"
                    assert mux4to1(a0, a1, a2, a3, True, True) == a3, f"Inputs: a0={a0}, a1={a1}, a2={a2}, a3={a3}"
