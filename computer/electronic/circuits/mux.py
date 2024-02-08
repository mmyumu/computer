"""
Multiplexers
https://fr.wikipedia.org/wiki/Multiplexeur
"""

from computer.electronic.circuits.cmos import ANDGate, NOTGate, ORGate


# pylint: disable=R0913

class MUX2To1():
    """
    Multiplexer 2 to 1
    """
    def __init__(self):
        self._not = NOTGate()

        self._and0 = ANDGate()
        self._and1 = ANDGate()

        self._or = ORGate()

    def __call__(self, input_signal_a0: bool, input_signal_a1: bool, s: bool) -> bool:
        not_s = self._not(s)

        and0 = self._and0(input_signal_a0, not_s)
        and1 = self._and1(input_signal_a1, s)

        return self._or(and0, and1)


class MUX4To1():
    """
    Multiplexer 4 to 1
    https://bravelearn.com/wp-content/uploads/2017/01/4x2_mux.png
    """
    def __init__(self):
        self._mux2to1_0 = MUX2To1()
        self._mux2to1_1 = MUX2To1()
        self._mux2to1_2 = MUX2To1()


    def __call__(self, input_signal_a0: bool, input_signal_a1: bool, input_signal_a2: bool, input_signal_a3: bool,
                 s0: bool, s1: bool) -> bool:
        mux0 = self._mux2to1_0(input_signal_a0, input_signal_a1, s1)
        mux1 = self._mux2to1_1(input_signal_a2, input_signal_a3, s1)

        return self._mux2to1_2(mux0, mux1, s0)
