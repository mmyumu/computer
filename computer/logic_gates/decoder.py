"""
Binary decoders
"""
from typing import Tuple
from computer.logic_gates.cmos import ANDGate, NOTGate


class Decoder2To4:
    """
    2-to-4 binary decoder
    https://www.101computing.net/binary-decoders-using-logic-gates/
    """
    def __init__(self):
        self._not0 = NOTGate()
        self._not1 = NOTGate()

        self._and0 = ANDGate()
        self._and1 = ANDGate()
        self._and2 = ANDGate()
        self._and3 = ANDGate()


    def __call__(self, input_signal_a1: bool, input_signal_a0: bool) -> Tuple[bool, bool, bool, bool]:
        """
        Logic gate operates inputs and returns outputs
        """
        not0 = self._not0(input_signal_a0)
        not1 = self._not1(input_signal_a1)

        d0 = self._and0(not0, not1)
        d1 = self._and1(not1, input_signal_a0)
        d2 = self._and2(not0 input_signal_a1)
        d3 = self._and3(input_signal_a0, input_signal_a1)


        return d3, d2, d1, d0
