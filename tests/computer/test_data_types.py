"""
Test data types module
"""

import pytest
from computer.data_types import Bits

# pylint: disable=C0116,C2801

def test_wrong_input():
    with pytest.raises(ValueError):
        Bits("aze")

def test_wrong_input_list():
    with pytest.raises(ValueError):
        Bits("aze", "poi")

def test_from_bin():
    my_bit = Bits.from_bin(0b101010, size=8)
    assert my_bit == [0, 0, 1, 0, 1, 0, 1, 0]

def test_from_bin_size_auto():
    my_bit = Bits.from_bin(0b101010)
    assert my_bit == [1, 0, 1, 0, 1, 0]

def test_from_bin_too_big():
    with pytest.raises(ValueError):
        Bits.from_bin(0b101010, size=4)


def test_str():
    my_bit = Bits.from_bin(0b101010, size=8)
    my_bit.__str__()
