"""
Demultiplexers
"""


from computer.logic_gates.cmos import ANDGate, NOTGate


class DEMUX1To2():
    """
    Demultiplexer 2 to 1
    https://static.javatpoint.com/tutorial/digital-electronics/images/de-multiplexer3.png
    """
    def __init__(self):
        self._not = NOTGate()

        self._and0 = ANDGate()
        self._and1 = ANDGate()

    def __call__(self, input_signal_a: bool, s: bool) -> bool:
        not_s = self._not(s)

        and0 = self._and0(not_s, input_signal_a)
        and1 = self._and1(input_signal_a, s)

        return and1, and0


class DEMUX1To4():
    """
    Demultiplexer 2 to 1
    https://vlsiverify.com/wp-content/uploads/2022/12/1_4-demux-using-1_2-demux.jpg?ezimgfmt=rs:372x384/rscb1/ng:webp/ngcb1
    """
    def __init__(self):
        self._demux1to2_0 = DEMUX1To2()
        self._demux1to2_1 = DEMUX1To2()
        self._demux1to2_2 = DEMUX1To2()

    def __call__(self, input_signal_a: bool, s0: bool, s1: bool) -> bool:
        demux0_1, demux0_0 = self._demux1to2_0(input_signal_a, s0)

        d1, d0 = self._demux1to2_1(demux0_0, s1)
        d3, d2 = self._demux1to2_2(demux0_1, s1)

        return d3, d2, d1, d0
