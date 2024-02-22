"""
Test for registers
"""
import pytest

from computer.electronic.circuits.register import PIPORegister, SIPORegister, SISORegister


# pylint: disable=C0116,W0212

@pytest.fixture(name="siso_register")
def fixture_siso_register():
    return SISORegister()

@pytest.fixture(name="sipo_register")
def fixture_sipo_register():
    return SIPORegister()

@pytest.fixture(name="pipo_register")
def fixture_pipo_register():
    return PIPORegister()


def test_siso_register_reset(siso_register: SISORegister):
    siso_register.reset_states()

    siso_register.set_d(False)
    assert siso_register.clock_tick(False) is False
    assert siso_register.clock_tick(False) is False
    assert siso_register.clock_tick(False) is False
    assert siso_register.clock_tick(False) is False


def test_siso_set1011(siso_register: SISORegister):
    siso_register.reset_states()

    siso_register.set_d(True)
    assert siso_register.clock_tick(True) is False

    siso_register.set_d(True)
    assert siso_register.clock_tick(True) is False

    siso_register.set_d(False)
    assert siso_register.clock_tick(True) is False

    siso_register.set_d(True)
    assert siso_register.clock_tick(True) is True

    assert siso_register._d_flip_flops[3].q is True
    assert siso_register._d_flip_flops[2].q is False
    assert siso_register._d_flip_flops[1].q is True
    assert siso_register._d_flip_flops[0].q is True


def test_siso_set1111(siso_register: SISORegister):
    siso_register.reset_states()

    siso_register.set_d(True)
    assert siso_register.clock_tick(True) is False

    siso_register.set_d(True)
    assert siso_register.clock_tick(True) is False

    siso_register.set_d(True)
    assert siso_register.clock_tick(True) is False

    siso_register.set_d(True)
    assert siso_register.clock_tick(True) is True

    assert siso_register._d_flip_flops[3].q is True
    assert siso_register._d_flip_flops[2].q is True
    assert siso_register._d_flip_flops[1].q is True
    assert siso_register._d_flip_flops[0].q is True


def test_siso_set1110(siso_register: SISORegister):
    siso_register.reset_states()

    siso_register.set_d(False)
    assert siso_register.clock_tick(True) is False

    siso_register.set_d(True)
    assert siso_register.clock_tick(True) is False

    siso_register.set_d(True)
    assert siso_register.clock_tick(True) is False

    siso_register.set_d(True)
    assert siso_register.clock_tick(True) is False

    assert siso_register._d_flip_flops[3].q is True
    assert siso_register._d_flip_flops[2].q is True
    assert siso_register._d_flip_flops[1].q is True
    assert siso_register._d_flip_flops[0].q is False


def test_siso_set1110_memorize(siso_register: SISORegister):
    siso_register.reset_states()

    siso_register.set_d(False)
    assert siso_register.clock_tick(True) is False

    siso_register.set_d(True)
    assert siso_register.clock_tick(True) is False

    siso_register.set_d(True)
    assert siso_register.clock_tick(True) is False

    siso_register.set_d(True)
    assert siso_register.clock_tick(True) is False

    assert siso_register._d_flip_flops[3].q is True
    assert siso_register._d_flip_flops[2].q is True
    assert siso_register._d_flip_flops[1].q is True
    assert siso_register._d_flip_flops[0].q is False

    for _ in range(10):
        siso_register.clock_tick(False)

    assert siso_register._d_flip_flops[3].q is True
    assert siso_register._d_flip_flops[2].q is True
    assert siso_register._d_flip_flops[1].q is True
    assert siso_register._d_flip_flops[0].q is False


def test_sipo_register_reset(sipo_register: SIPORegister):
    sipo_register.reset_states()
    assert sipo_register.clock_tick(False) == (False, False, False, False)


def test_sipo_set1011(sipo_register: SIPORegister):
    sipo_register.reset_states()

    sipo_register.set_d(True)
    assert sipo_register.clock_tick(True) == (True, False, False, False)

    sipo_register.set_d(True)
    assert sipo_register.clock_tick(True) == (True, True, False, False)

    sipo_register.set_d(False)
    assert sipo_register.clock_tick(True) == (False, True, True, False)

    sipo_register.set_d(True)
    assert sipo_register.clock_tick(True) == (True, False, True, True)


def test_sipo_set1111(sipo_register: SIPORegister):
    sipo_register.reset_states()

    sipo_register.set_d(True)
    assert sipo_register.clock_tick(True) == (True, False, False, False)

    sipo_register.set_d(True)
    assert sipo_register.clock_tick(True) == (True, True, False, False)

    sipo_register.set_d(True)
    assert sipo_register.clock_tick(True) == (True, True, True, False)

    sipo_register.set_d(True)
    assert sipo_register.clock_tick(True) == (True, True, True, True)


def test_sipo_set1110(sipo_register: SIPORegister):
    sipo_register.reset_states()

    sipo_register.set_d(True)
    assert sipo_register.clock_tick(True) == (True, False, False, False)

    sipo_register.set_d(True)
    assert sipo_register.clock_tick(True) == (True, True, False, False)

    sipo_register.set_d(True)
    assert sipo_register.clock_tick(True) == (True, True, True, False)

    sipo_register.set_d(False)
    assert sipo_register.clock_tick(True) == (False, True, True, True)


def test_sipo_set1110_memorize(sipo_register: SIPORegister):
    sipo_register.reset_states()

    sipo_register.set_d(True)
    assert sipo_register.clock_tick(True) == (True, False, False, False)

    sipo_register.set_d(True)
    assert sipo_register.clock_tick(True) == (True, True, False, False)

    sipo_register.set_d(True)
    assert sipo_register.clock_tick(True) == (True, True, True, False)

    sipo_register.set_d(False)
    assert sipo_register.clock_tick(True) == (False, True, True, True)

    for _ in range(10):
        assert sipo_register.clock_tick(False) == (False, True, True, True)


def test_pipo_set1011(pipo_register: PIPORegister):
    pipo_register.reset_states()

    pipo_register.set_d(True, False, True, True)
    assert pipo_register.clock_tick(True) == [True, False, True, True]


def test_pipo_set1111(pipo_register: PIPORegister):
    pipo_register.reset_states()

    pipo_register.set_d(True, True, True, True)
    assert pipo_register.clock_tick(True) == [True, True, True, True]


def test_pipo_set1110(pipo_register: PIPORegister):
    pipo_register.reset_states()

    pipo_register.set_d(True, True, True, False)
    assert pipo_register.clock_tick(True) == [True, True, True, False]


def test_pipo_set1110_memorize(pipo_register: PIPORegister):
    pipo_register.reset_states()

    pipo_register.set_d(True, True, True, False)
    assert pipo_register.clock_tick(True) == [True, True, True, False]

    for _ in range(10):
        assert pipo_register.clock_tick(False) == [True, True, True, False]
