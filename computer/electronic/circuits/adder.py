"""
Adders
"""
from typing import Tuple
from computer.electronic.circuits.cmos import ANDGate, ORGate, XORGate


class HalfAdder:
    """
    Add 2 bits: A and B
    Returns the sum and the carry out
    https://www.elprocus.com/wp-content/uploads/HA-Logical-Diagram.jpg
    """
    def __init__(self):
        self._xor = XORGate()
        self._and = ANDGate()


    def __call__(self, input_signal_a: bool, input_signal_b: bool) -> Tuple[bool, bool]:
        """
        Logic gate operates inputs and returns outputs
        """
        sum_result = self._xor(input_signal_a, input_signal_b)
        carry = self._and(input_signal_a, input_signal_b)

        return sum_result, carry


class FullAdder:
    """
    Add 3 bits: A, B and carry in
    Returns the sum and the carry out
    https://www.elprocus.com/wp-content/uploads/Full-Adder-Logical-Diagram.png
    """
    def __init__(self):
        self._xor1 = XORGate()
        self._xor2 = XORGate()
        self._and1 = ANDGate()
        self._and2 = ANDGate()
        self._or = ORGate()


    def __call__(self, input_signal_a: bool, input_signal_b: bool, input_signal_carry_in: bool) -> Tuple[bool, bool]:
        """
        Logic gate operates inputs and returns outputs
        """
        xor1 = self._xor1(input_signal_a, input_signal_b)
        sum_result = self._xor2(xor1, input_signal_carry_in)

        and1 = self._and1(input_signal_carry_in, xor1)
        and2 = self._and2(input_signal_a, input_signal_b)

        carry = self._or(and1, and2)

        return sum_result, carry
