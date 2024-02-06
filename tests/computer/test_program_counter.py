"""
Test for Program counter
"""
import pytest

from computer.program_counter import ProgramCounter


# pylint: disable=C0116,W0212

@pytest.fixture(name="program_counter")
def fixture_program_counter():
    return ProgramCounter()


def test_reset(program_counter: ProgramCounter):
    program_counter.reset()
    assert program_counter.value == (0, 0, 0, 0)


def test_increment1(program_counter: ProgramCounter):
    program_counter.reset()
    program_counter.increment()
    program_counter.clock_tick(True)
    assert program_counter.value == (0, 0, 0, 1)


def test_increment10(program_counter: ProgramCounter):
    program_counter.reset()
    for _ in range(10):
        program_counter.increment()
        program_counter.clock_tick(True)
    assert program_counter.value == (1, 0, 1, 0)


def test_increment_overflow(program_counter: ProgramCounter):
    program_counter.reset()
    for _ in range(15):
        program_counter.increment()
        program_counter.clock_tick(True)
    assert program_counter.value == (1, 1, 1, 1)

    with pytest.raises(ValueError):
        program_counter.increment()
        program_counter.clock_tick(True)


def test_increment_tick_tack(program_counter: ProgramCounter):
    program_counter.reset()
    for _ in range(15):
        program_counter.increment()
        program_counter.clock_tick(False)
        program_counter.increment()
        program_counter.clock_tick(True)
    assert program_counter.value == (1, 1, 1, 1)
