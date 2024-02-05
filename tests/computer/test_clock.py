"""
Test for Clock
"""
import pytest
from computer.clock import Clock, RealTimeClock


# pylint: disable=C0116,W0212

@pytest.fixture(name="clock")
def fixture_clock():
    return Clock()

@pytest.fixture(name="real_time_clock")
def fixture_real_time_clock():
    return RealTimeClock(1000)


def test_clock(clock: Clock):
    assert clock.clock_state is False
    clock.tick()
    assert clock.clock_state is True
    clock.tick()
    assert clock.clock_state is False

def test_real_time_clock(real_time_clock: RealTimeClock):
    assert real_time_clock.clock_state is False
    real_time_clock.tick()
    assert real_time_clock.clock_state is True
    real_time_clock.tick()
    assert real_time_clock.clock_state is False
