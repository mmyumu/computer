"""
Bitwise circuits mopdule
"""
from typing import Tuple
from computer.data_types import Bits
from computer.electronic.circuits.adder import FullAdder
from computer.electronic.circuits.complement import TwoComplement


class BitwiseAdd:
    """
    Bitwise adder of 2 N bits numbers
    """
    def __init__(self, size: int):
        self._size = size

        self._adders = [FullAdder() for _ in range(2 ** self._size)]


    def __call__(self, d1: Bits, d2: Bits, carry: bool) -> Tuple[Bits, bool]:
        if len(d1) != 2 ** self._size:
            raise ValueError(f"Length of d1 should be {2 ** self._size} but is {len(d1)}")

        if len(d2) != 2 ** self._size:
            raise ValueError(f"Length of d2 should be {2 ** self._size} but is {len(d2)}")

        carry_in = carry
        data = []
        for bit1, bit2, adder in zip(d1[::-1], d2[::-1], self._adders):
            result_bit, carry_out = adder(bit1, bit2, carry_in)
            carry_in = carry_out
            data.append(result_bit)
        data = data[::-1]

        return data, carry_out


class BitwiseSub:
    """
    Bitwise sub of 2 N bits numbers
    """
    def __init__(self, size: int):
        self._size = size
        self._adder = BitwiseAdd(self._size)
        self._complement = TwoComplement(self._size)


    def __call__(self, d1: Bits, d2: Bits) -> Tuple[Bits, bool]:
        if len(d1) != 2 ** self._size:
            raise ValueError(f"Length of d1 should be {2 ** self._size} but is {len(d1)}")

        if len(d2) != 2 ** self._size:
            raise ValueError(f"Length of d2 should be {2 ** self._size} but is {len(d2)}")

        complement_data2 = self._complement(d2)
        sub_data, _ = self._adder(d1, complement_data2, False)

        return sub_data
