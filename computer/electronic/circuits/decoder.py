"""
Binary decoders
"""
from typing import Tuple
from computer.electronic.circuits.cmos import ANDGate, ANDGate3, NOTGate


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
        d2 = self._and2(not0, input_signal_a1)
        d3 = self._and3(input_signal_a0, input_signal_a1)


        return d3, d2, d1, d0


class Decoder3To8:
    """
    3-to-8 binary decoder
    https://www.101computing.net/binary-decoders-using-logic-gates/
    Not really the link above since they reverted A2, A1, A0 between truth table and diagram
    """
    def __init__(self):
        self._not0 = NOTGate()
        self._not1 = NOTGate()
        self._not2 = NOTGate()

        self._and0 = ANDGate3()
        self._and1 = ANDGate3()
        self._and2 = ANDGate3()
        self._and3 = ANDGate3()
        self._and4 = ANDGate3()
        self._and5 = ANDGate3()
        self._and6 = ANDGate3()
        self._and7 = ANDGate3()

    def __call__(self, input_signal_a2: bool, input_signal_a1: bool, input_signal_a0: bool) -> Tuple[bool, bool, bool, bool]:
        """
        Logic gate operates inputs and returns outputs
        """
        not0 = self._not0(input_signal_a0)
        not1 = self._not1(input_signal_a1)
        not2 = self._not1(input_signal_a2)

        d0 = self._and0(not0, not1, not2)
        d1 = self._and1(input_signal_a0, not1, not2)
        d2 = self._and2(not0, input_signal_a1, not2)
        d3 = self._and3(input_signal_a0, input_signal_a1, not2)
        d4 = self._and3(not0, not1, input_signal_a2)
        d5 = self._and3(input_signal_a0, not1, input_signal_a2)
        d6 = self._and3(not0, input_signal_a1, input_signal_a2)
        d7 = self._and3(input_signal_a0, input_signal_a1, input_signal_a2)

        return d7, d6, d5, d4, d3, d2, d1, d0
