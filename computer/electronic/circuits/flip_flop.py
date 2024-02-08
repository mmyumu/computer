"""
Flip flops circuits
"""
from abc import ABC
import random
from typing import Tuple
from computer.electronic.circuits.cmos import NANDGate, NOTGate


# pylint: disable=R0902

class FlipFlop(ABC):
    """
    Base class of flip flop
    """
    def __init__(self):
        self.q = bool(random.getrandbits(1))
        self.q_bar = bool(random.getrandbits(1))

    def reset_states(self):
        """
        Resets the state of the flip flop
        """
        self.q = False
        self.q_bar = True

    def __str__(self):
        """
        Print states
        """
        return f"Q={self.q}, Q bar={self.q_bar}"


class SRFlipFlop(FlipFlop):
    """
    Set/Reset flip flop
    https://www.javatpoint.com/basics-of-flip-flop-in-digital-electronics
    """
    def __init__(self):
        super().__init__()
        self._nand0 = NANDGate()
        self._nand1 = NANDGate()
        self._nand2 = NANDGate()
        self._nand3 = NANDGate()

        self._set = bool(random.getrandbits(1))
        self._reset = bool(random.getrandbits(1))

    @property
    def output(self):
        """
        Returns Q and Qbar outputs
        """
        return self.q, self.q_bar

    def set_sr(self, input_set: bool, input_reset: bool):
        """
        Set the SET/RESET inputs of the SR flip-flop
        """
        self._set = input_set
        self._reset = input_reset

    def reset_states(self):
        super().reset_states()
        self._set = False
        self._reset = True

    def clock_tick(self, enable: bool) -> Tuple[bool, bool]:
        """
        Update flip-flop status on clock tick
        """
        if self._set and self._reset:
            raise ValueError("Invalid state: set and reset both high")

        nand0 = self._nand0(self._set, enable)
        nand1 = self._nand1(enable, self._reset)

        next_q = self._nand2(nand0, self.q_bar)
        next_q_bar = self._nand3(self.q, nand1)

        # 2nd propagation to get the correct result
        next_q = self._nand2(nand0, next_q_bar)
        next_q_bar = self._nand3(next_q, nand1)

        self.q = next_q
        self.q_bar = next_q_bar

        return self.output

    def __str__(self):
        return f"SR Flip-Flop: {super().__str__()}"


class DFlipFlop(SRFlipFlop):
    """
    D flip-flop class.
    Inherits SR flip-flop since it is a SR flip-flop with set/resete being 
    complementary with a NOT gate.
    https://www.paturage.be/electro/inforauto/portes/bascule.html
    """
    def __init__(self):
        super().__init__()
        self._not = NOTGate()

    def set_d(self, input_d: bool):
        """
        Set the D input of the D flip-flop
        """
        input_d_bar = self._not(input_d)
        return self.set_sr(input_d, input_d_bar)

    def __str__(self):
        return f"D Flip-Flop: {super().__str__()}"
