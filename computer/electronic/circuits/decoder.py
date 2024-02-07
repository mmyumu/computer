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

        self._and0 = ANDGate3()
        self._and1 = ANDGate3()
        self._and2 = ANDGate3()
        self._and3 = ANDGate3()


    def __call__(self, input_signal_a1: bool, input_signal_a0: bool, enable: bool) -> Tuple[bool, bool, bool, bool]:
        """
        Logic gate operates inputs and returns outputs
        """
        not0 = self._not0(input_signal_a0)
        not1 = self._not1(input_signal_a1)

        d0 = self._and0(not0, not1, enable)
        d1 = self._and1(not1, input_signal_a0, enable)
        d2 = self._and2(not0, input_signal_a1, enable)
        d3 = self._and3(input_signal_a0, input_signal_a1, enable)


        return d3, d2, d1, d0


class Decoder3To8:
    """
    3-to-8 binary decoder
    https://www.101computing.net/binary-decoders-using-logic-gates/
    Not really the link above since they reverted A2, A1, A0 between truth table and diagram
    """
    def __init__(self):
        self._not = NOTGate()
        self._decoder2to4_0 = Decoder2To4()
        self._decoder2to4_1 = Decoder2To4()

        self._and0 = ANDGate()
        self._and1 = ANDGate()
        self._and2 = ANDGate()
        self._and3 = ANDGate()
        self._and4 = ANDGate()
        self._and5 = ANDGate()
        self._and6 = ANDGate()
        self._and7 = ANDGate()

    def __call__(self, input_signal_a2: bool, input_signal_a1: bool, input_signal_a0: bool, enable: bool) -> Tuple[bool, bool, bool, bool]:
        """
        Logic gate operates inputs and returns outputs
        """
        not2 = self._not(input_signal_a2)
        d3, d2, d1, d0 = self._decoder2to4_0(input_signal_a1, input_signal_a0, not2)
        d7, d6, d5, d4 = self._decoder2to4_1(input_signal_a1, input_signal_a0, input_signal_a2)

        d0 = self._and0(d0, enable)
        d1 = self._and0(d1, enable)
        d2 = self._and0(d2, enable)
        d3 = self._and0(d3, enable)
        d4 = self._and0(d4, enable)
        d5 = self._and0(d5, enable)
        d6 = self._and0(d6, enable)
        d7 = self._and0(d7, enable)

        return d7, d6, d5, d4, d3, d2, d1, d0


class Decoder4To16:
    """
    4-to-16 binary decoder
    https://www.tutorialspoint.com/digital_circuits/digital_circuits_decoders.htm
    """
    def __init__(self):
        self._not = NOTGate()
        self._decoder3to8_0 = Decoder3To8()
        self._decoder3to8_1 = Decoder3To8()

        self._and0 = ANDGate()
        self._and1 = ANDGate()
        self._and2 = ANDGate()
        self._and3 = ANDGate()
        self._and4 = ANDGate()
        self._and5 = ANDGate()
        self._and6 = ANDGate()
        self._and7 = ANDGate()
        self._and8 = ANDGate()
        self._and9 = ANDGate()
        self._and10 = ANDGate()
        self._and11 = ANDGate()
        self._and12 = ANDGate()
        self._and13 = ANDGate()
        self._and14 = ANDGate()
        self._and15 = ANDGate()

    def __call__(self, input_signal_a3: bool, input_signal_a2: bool, input_signal_a1: bool, input_signal_a0:
                 bool, enable: bool) -> Tuple[bool, bool, bool, bool]:
        """
        Logic gate operates inputs and returns outputs
        """
        not3 = self._not(input_signal_a3)

        d7, d6, d5, d4, d3, d2, d1, d0 = self._decoder3to8_0(input_signal_a2, input_signal_a1, input_signal_a0, not3)
        d15, d14, d13, d12, d11, d10, d9, d8 = self._decoder3to8_0(input_signal_a2, input_signal_a1, input_signal_a0, input_signal_a3)

        d0 = self._and0(d0, enable)
        d1 = self._and0(d1, enable)
        d2 = self._and0(d2, enable)
        d3 = self._and0(d3, enable)
        d4 = self._and0(d4, enable)
        d5 = self._and0(d5, enable)
        d6 = self._and0(d6, enable)
        d7 = self._and0(d7, enable)
        d8 = self._and0(d8, enable)
        d9 = self._and0(d9, enable)
        d10 = self._and0(d10, enable)
        d11 = self._and0(d11, enable)
        d12 = self._and0(d12, enable)
        d13 = self._and0(d13, enable)
        d14 = self._and0(d14, enable)
        d15 = self._and0(d15, enable)

        return d15, d14, d13, d12, d11, d10, d9, d8, d7, d6, d5, d4, d3, d2, d1, d0
