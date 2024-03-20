"""
Test for Control Unit module.
"""
import time
import pytest

from computer.data_types import Bits
from computer.memory import SRAM
from computer.screen import Screen


# pylint: disable=C0116,W0212

@pytest.fixture(name="screen")
def fixture_screen():
    memory = SRAM(size=8, register_size=3)
    memory.reset()
    return Screen(memory, resolution=10)

def test_memory_too_small():
    memory = SRAM(size=8, register_size=3)
    memory.reset()

    with pytest.raises(ValueError):
        Screen(memory, resolution=128)

def test_get_data(screen: Screen):
    screen._memory.write(Bits(255, size=8), Bits(1, size=8))
    screen._memory.clock_tick(True)

    screen_data = screen._get_data()
    assert any(screen_data[:98]) is False
    assert screen_data[99] is True

def test_refresh(screen: Screen):
    screen._memory.write(Bits(255, size=8), Bits(1, size=8))
    screen._memory.clock_tick(True)

    screen.refresh()
    screen_data = screen._screen_data
    assert any(screen_data[:98]) is False
    assert screen_data[99] is True

def test_thread(screen: Screen):
    screen._memory.write(Bits(255, size=8), Bits(1, size=8))
    screen._memory.clock_tick(True)

    screen.start()
    time.sleep(2 / screen._refresh_rate)
    screen.stop()
    screen.join()
    screen_data = screen._screen_data
    assert any(screen_data[:98]) is False
    assert screen_data[99] is True


def test_print_data(screen: Screen):
    screen._screen_data = [0] * 100
    screen._screen_data[99] = 1
    screen._print_data()
