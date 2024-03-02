"""
Barrel shifter module
"""
from typing import Any, List

from computer.data_types import Bits
from computer.electronic.circuits.mux import MUX2To1


class BarrelShifter:
    """
    Barrel shifter (aka bit rotation).
    It does both right and left depending on the given parameter.
    """
    def __init__(self, size, right: bool = True) -> None:
        self._size = size
        self._right = right
        self._muxes: List[List[MUX2To1]] = []

        for _ in range(size):
            muxes = []
            for _ in range(2** size):
                muxes.append(MUX2To1())
            self._muxes.append(muxes)

    def __call__(self, i: Bits, s: Bits) -> Any:
        if len(s) != self._size:
            raise ValueError(f"Length of s should be {self._size} but is {len(s)}")

        if len(i) != 2 ** self._size:
            raise ValueError(f"Length of i should be {2 ** self._size} but is {len(i)}")

        if self._right:
            current_i = i
        else:
            current_i = i[::-1]

        for index_s, bit_s in enumerate(s[::-1]):
            number_of_zero = 2 ** index_s

            output = []
            for index_i, bit_i in enumerate(current_i):
                if index_i < number_of_zero:
                    a1 = current_i[(2**self._size) - number_of_zero + index_i]
                else:
                    a1 = current_i[index_i - number_of_zero]

                a0 = bit_i
                mux_result = self._muxes[index_s][index_i](a0, a1, bit_s)

                output.append(mux_result)
            current_i = output

        if self._right:
            result = Bits(output)
            carry_out = result[0]
        else:
            result = Bits(output[::-1])
            carry_out = result[-1]
        return result, carry_out
