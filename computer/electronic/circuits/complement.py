

from computer.data_types import Bits
from computer.electronic.circuits.adder import HalfAdder
from computer.electronic.circuits.cmos import NOTGate


class TwoComplement:
    """
    Two's complement of given number
    """
    def __init__(self, size: int):
        self._size = size

        self._nots = [NOTGate() for _ in range(2 ** self._size)]
        self._adders = [HalfAdder() for _ in range(2 ** self._size)]


    def __call__(self, d: Bits) -> Bits:
        if len(d) != 2 ** self._size:
            raise ValueError(f"Length of d should be {2 ** self._size} but is {len(d)}")

        not_d = []
        for bit2, not_gate in zip(d, self._nots):
            not_d.append(not_gate(bit2))

        complement = []
        carry_in = True
        for bit2, adder in zip(not_d[::-1], self._adders):
            complement_bit, carry_out = adder(bit2, carry_in)
            carry_in = carry_out
            complement.append(complement_bit)
        complement = complement[::-1]

        return complement
