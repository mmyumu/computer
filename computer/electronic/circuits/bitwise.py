"""
Bitwise circuits mopdule
"""
from typing import List, Tuple
from computer.data_types import Bits
from computer.electronic.circuits.adder import FullAdder
from computer.electronic.circuits.cmos import ANDGate
from computer.electronic.circuits.complement import TwoComplement

# TODO: write unit tests for all operations

# pylint: disable=R0903

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
    Bitwise subtract of 2 N bits numbers
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




class BitwiseMult:
    """
    Bitwise multiply 2 N bits numbers
        1011   (this is binary for decimal 11)
        × 1110   (this is binary for decimal 14)
        ======
        0000   (this is 1011 × 0)
        1011    (this is 1011 × 1, shifted one position to the left)
        1011     (this is 1011 × 1, shifted two positions to the left)
    + 1011      (this is 1011 × 1, shifted three positions to the left)
    =========
    10011010   (this is binary for decimal 154)
    """
    def __init__(self, size: int):
        self._size = size

        self._and_gates: List[List[ANDGate]] = []
        for _ in range(2 ** self._size):
            and_gates = []
            for _ in range(2 ** self._size):
                and_gates.append(ANDGate())
            self._and_gates.append(and_gates)

        self._bitwise_adds = [BitwiseAdd(self._size + 1) for _ in range((2 ** self._size) - 1)]


    def __call__(self, d1: Bits, d2: Bits) -> Tuple[Bits, bool]:
        if len(d1) != 2 ** self._size:
            raise ValueError(f"Length of d1 should be {2 ** self._size} but is {len(d1)}")

        if len(d2) != 2 ** self._size:
            raise ValueError(f"Length of d2 should be {2 ** self._size} but is {len(d2)}")

        aggregated_and_result = None
        for i, (bit2, and_gates) in enumerate(zip(d2[::-1], self._and_gates)):
            and_result = [False] * (len(d2) - i)
            for bit1, and_gate in zip(d1, and_gates):
                and_bit = and_gate(bit1, bit2)
                and_result.append(and_bit)
            and_result += [False] * i

            if aggregated_and_result is not None:
                aggregated_and_result, _ = self._bitwise_adds[i - 1](and_result, aggregated_and_result, False)
            else:
                aggregated_and_result = and_result

        return aggregated_and_result
