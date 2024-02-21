"""
Subtractors
"""
from typing import Tuple
from computer.electronic.circuits.adder import FullAdder
from computer.electronic.circuits.cmos import ANDGate, NOTGate, ORGate, XORGate
from computer.electronic.circuits.mux import MUX2To1


class HalfSubtractor:
    """
    Subtract 2 bits: A and B
    Returns the difference and borrow out
    https://www.geeksforgeeks.org/half-subtractor-in-digital-logic/
    """
    def __init__(self):
        self._xor = XORGate()
        self._not = NOTGate()
        self._and = ANDGate()


    def __call__(self, input_signal_a: bool, input_signal_b: bool) -> Tuple[bool, bool]:
        """
        Logic gate operates inputs and returns outputs
        """
        difference = self._xor(input_signal_a, input_signal_b)
        not_input_signal_a = self._not(input_signal_a)
        borrow = self._and(not_input_signal_a, input_signal_b)

        return difference, borrow


class FullSubtractor:
    """
    Subtract 3 bits: A, B and borrow in
    Returns the difference and the borrow out
    https://www.geeksforgeeks.org/full-subtractor-in-digital-logic/
    """
    def __init__(self):
        self._xor1 = XORGate()
        self._xor2 = XORGate()
        self._not1 = NOTGate()
        self._not2 = NOTGate()
        self._and1 = ANDGate()
        self._and2 = ANDGate()
        self._or = ORGate()


    def __call__(self, input_signal_a: bool, input_signal_b: bool, input_signal_borrow_in: bool) -> Tuple[bool, bool]:
        """
        Logic gate operates inputs and returns outputs
        """
        xor1 = self._xor1(input_signal_a, input_signal_b)
        difference = self._xor2(xor1, input_signal_borrow_in)

        not_input_signal_a = self._not1(input_signal_a)
        and1 = self._and1(not_input_signal_a, input_signal_b)

        not_xor1 = self._not2(xor1)
        and2 = self._and2(not_xor1, input_signal_borrow_in)

        borrow_out = self._or(and1, and2)

        return difference, borrow_out



class FullSubtractorRestore:
    """
    Subtract 3 bits: A, B and borrow in.
    Restore value A if result is negative
    Returns the difference and the borrow out
    https://www.geeksforgeeks.org/full-subtractor-in-digital-logic/
    """
    def __init__(self):
        self._subtractor = FullSubtractor()
        self._mux = MUX2To1()


    def __call__(self, input_signal_a: bool, input_signal_b: bool, input_signal_borrow_in: bool, input_signal_carry: bool) -> Tuple[bool, bool]:
        """
        Logic gate operates inputs and returns outputs
        """
        difference, borrow_out = self._subtractor(input_signal_a, input_signal_b, input_signal_borrow_in)
        mux_result = self._mux(input_signal_a, difference, input_signal_carry)


        return mux_result, borrow_out
