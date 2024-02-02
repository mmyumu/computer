"""
Test for multiplexers and demultiplexers
"""
import pytest

from computer.logic_gates.demux import DEMUX1To2, DEMUX1To4

# pylint: disable=C0116

@pytest.fixture(name="demux1to2")
def fixture_demux1to2():
    return DEMUX1To2()

@pytest.fixture(name="demux1to4")
def fixture_demux1to4():
    return DEMUX1To4()


def test_demux1to2(demux1to2: DEMUX1To2):
    for a in [False, True]:
        assert demux1to2(a, False) == (False, a), f"Inputs: a={a}"
        assert demux1to2(a, True) == (a, False), f"Inputs: a={a}"

def test_demux1to4(demux1to4: DEMUX1To4):
    for a in [False, True]:
        assert demux1to4(a, False, False) == (False, False, False, a), f"Inputs: a={a}"
        assert demux1to4(a, False, True) == (False, False, a, False), f"Inputs: a={a}"
        assert demux1to4(a, True, False) == (False, a, False, False), f"Inputs: a={a}"
        assert demux1to4(a, True, True) == (a, False, False, False), f"Inputs: a={a}"
