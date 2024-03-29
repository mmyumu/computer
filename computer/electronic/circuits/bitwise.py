"""
Bitwise circuits module
"""
from typing import List, Tuple
from computer.data_types import Bits
from computer.electronic.circuits.adder import FullAdder
from computer.electronic.circuits.cmos import ANDGate, NOTGate, ORGate
from computer.electronic.circuits.mux import MUX2To1
from computer.electronic.circuits.subtractor import FullSubtractor, FullSubtractorRestore

# pylint: disable=R0903

class Bitwise:
    """
    Base class for bitwise operations
    """
    def __init__(self, size: int):
        self._size = size

    def _check_input(self, i: Bits, input_name: str):
        """
        Check if the given input is correct

        Args:
            i (Bits): the input to check
            input_name (str): the name of the input for logging purpose

        Raises:
            ValueError: raised if the input is not correct
        """
        if len(i) != self._size:
            raise ValueError(f"Length of {input_name} should be {self._size} but is {len(i)}")


class BitwiseAdd(Bitwise):
    """
    Bitwise adder of 2 N-bits numbers.
    Adder/subtractor could be merged in a adder-subtractor circuit.
    """
    def __init__(self, size: int):
        super().__init__(size)
        self._adders = [FullAdder() for _ in range(self._size)]

    def __call__(self, d1: Bits, d2: Bits, carry: bool) -> Tuple[Bits, bool]:
        self._check_input(d1, "d1")
        self._check_input(d2, "d2")

        carry_in = carry
        data = []
        for bit1, bit2, adder in zip(d1[::-1], d2[::-1], self._adders):
            result_bit, carry_out = adder(bit1, bit2, carry_in)
            carry_in = carry_out
            data.append(result_bit)
        data = data[::-1]

        return Bits(data), carry_out


class BitwiseSub(Bitwise):
    """
    Bitwise subtract of 2 N-bits numbers.
    Adder/subtractor could be merged in a adder-subtractor circuit.
    https://www.geeksforgeeks.org/parallel-adder-and-parallel-subtractor/
    """
    def __init__(self, size: int):
        super().__init__(size)
        self._subtractors = [FullSubtractor() for _ in range(self._size)]

    def __call__(self, d1: Bits, d2: Bits, borrow: bool) -> Tuple[Bits, bool]:
        self._check_input(d1, "d1")
        self._check_input(d2, "d2")

        borrow_in = borrow
        sub_data = []
        for bit1, bit2, subtractor in zip(d1[::-1], d2[::-1], self._subtractors):
            difference, borrow_out = subtractor(bit1, bit2, borrow_in)
            borrow_in = borrow_out
            sub_data.append(difference)

        return Bits(sub_data[::-1]), borrow_out


class BitwiseMult(Bitwise):
    """
    Bitwise multiply 2 N-bits numbers
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
        super().__init__(size)

        self._and_gates: List[List[ANDGate]] = []
        for _ in range(self._size):
            and_gates = []
            for _ in range(self._size):
                and_gates.append(ANDGate())
            self._and_gates.append(and_gates)

        self._bitwise_adds = [BitwiseAdd(self._size * 2) for _ in range((self._size) - 1)]


    def __call__(self, d1: Bits, d2: Bits) -> Tuple[Bits, bool]:
        self._check_input(d1, "d1")
        self._check_input(d2, "d2")

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


class BitwiseDiv(Bitwise):
    """
    Bitwise divide 2 N-bits numbers
    https://www.researchgate.net/profile/Shaahin-Angizi/publication/273886222/figure/fig2/AS:478206512898049@1491024725549/Schematic-logic-diagram-of-a-4-by-4-restoring-array-divider-33.png
    """
    def __init__(self, size: int):
        super().__init__(size)

        self._or_gates = []
        self._not_gates = []
        self._subrestores: List[List[FullSubtractorRestore]] = []
        for _ in range(self._size):
            self._not_gates.append(NOTGate())
            self._or_gates.append(ORGate())

            subrestores = []
            for _ in range(self._size):
                subrestores.append(FullSubtractorRestore())

            self._subrestores.append(subrestores)

    def __call__(self, a: Bits, d: Bits) -> Tuple[Bits, Bits]:
        self._check_input(a, "a")
        self._check_input(d, "d")

        if not any(d):
            raise ValueError("Divider cannot be 0")

        filled_a = Bits([0] * len(a) + a)

        quotient = []
        for i in range(self._size):
            if i == 0:
                bit_or = filled_a[0]
                row_a = filled_a[i + 1: i + 1 + self._size]
            else:
                bit_or = remainder_row[0]
                row_a = remainder_row[1:] + [a[i]]

            quotient_row, remainder_row = self._row(i, row_a, d, bit_or)
            quotient.append(quotient_row)

        return Bits(quotient), Bits(remainder_row)

    def _row(self, row: int,  a: Bits, d: Bits, bit_or: bool):
        if len(a) != self._size:
            raise ValueError(f"Length of input a should be {self._size} but is {len(a)}")

        borrow_in = False
        carry_in = True
        for subrestore, bit_a, bit_d in zip(self._subrestores[row], a[::-1], d[::-1]):
            subrestore_result, borrow_out = subrestore(bit_a, bit_d, borrow_in, carry_in)
            borrow_in = borrow_out

        not_borrow_out = self._not_gates[row](borrow_out)
        quotient = self._or_gates[row](bit_or, not_borrow_out)

        remainder = []
        carry_in = quotient
        for subrestore, bit_a, bit_d in zip(self._subrestores[row], a[::-1], d[::-1]):
            subrestore_result, borrow_out = subrestore(bit_a, bit_d, borrow_in, carry_in)
            remainder.append(subrestore_result)
            borrow_in = borrow_out

        return quotient, remainder[::-1]


class BitwiseMux(Bitwise):
    """
    Bitwise Mux between 2 N-bits numbers
    """
    def __init__(self, size: int):
        super().__init__(size)
        self._muxes = [MUX2To1() for _ in range(self._size)]

    def __call__(self, d1: Bits, d2: Bits, s: bool) -> Bits:
        self._check_input(d1, "d1")
        self._check_input(d2, "d2")

        data = []
        for bit1, bit2, mux in zip(d1[::-1], d2[::-1], self._muxes):
            result_bit = mux(bit1, bit2, s)
            data.append(result_bit)
        data = data[::-1]

        return Bits(data)
