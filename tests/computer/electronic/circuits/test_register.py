"""
Test for registers
"""
import pytest

from computer.electronic.circuits.register import SIPORegister, SISORegister


# pylint: disable=C0116

@pytest.fixture(name="siso_register")
def fixture_siso_register():
    return SISORegister()

@pytest.fixture(name="sipo_register")
def fixture_sipo_register():
    return SIPORegister()


def test_siso_register_reset(siso_register: SISORegister):
    siso_register.reset_states()

    assert siso_register(False, False) is False
    assert siso_register(False, False) is False
    assert siso_register(False, False) is False
    assert siso_register(False, False) is False


def test_siso_set1011(siso_register: SISORegister):
    siso_register.reset_states()

    siso_register(True, True)
    siso_register(True, True)
    siso_register(False, True)
    siso_register(True, True)

# def test_mux4to1(mux4to1: MUX4To1):
#     for a0 in [False, True]:
#         for a1 in [False, True]:
#             for a2 in [False, True]:
#                 for a3 in [False, True]:
#                     assert mux4to1(a0, a1, a2, a3, False, False) == a0, f"Inputs: a0={a0}, a1={a1}, a2={a2}, a3={a3}"
#                     assert mux4to1(a0, a1, a2, a3, False, True) == a1, f"Inputs: a0={a0}, a1={a1}, a2={a2}, a3={a3}"
#                     assert mux4to1(a0, a1, a2, a3, True, False) == a2, f"Inputs: a0={a0}, a1={a1}, a2={a2}, a3={a3}"
#                     assert mux4to1(a0, a1, a2, a3, True, True) == a3, f"Inputs: a0={a0}, a1={a1}, a2={a2}, a3={a3}"
