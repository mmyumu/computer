"""
Flip flops circuits
"""
from abc import ABC
import random
from typing import Tuple
from computer.logic_gates.cmos import NANDGate, NOTGate


class FlipFlop(ABC):
    """
    Base class of flip flop
    """
    def __init__(self):
        self._q = bool(random.getrandbits(1))
        self._q_bar = bool(random.getrandbits(1))

    def reset_states(self):
        """
        Resets the state of the flip flop
        """
        self._q = False
        self._q_bar = True

    def __str__(self):
        """
        Print states
        """
        return f"Q={self._q}, Q bar={self._q_bar}"


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

    def __call__(self, input_set: bool, input_reset: bool, enable: bool) -> Tuple[bool, bool]:
        """
        Met à jour les états Q et notQ en fonction des entrées S (Set) et R (Reset).
        :param S: Entrée Set (active basse)
        :param R: Entrée Reset (active basse)
        """
        if input_set and input_reset:
            raise ValueError("Invalid state: set and reset both high")

        nand0 = self._nand0(input_set, enable)
        nand1 = self._nand1(enable, input_reset)

        next_q = self._nand2(nand0, self._q_bar)
        next_q_bar = self._nand3(self._q, nand1)

        self._q = next_q
        self._q_bar = next_q_bar

        return self._q, self._q_bar

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

    def __call__(self, input_signal: bool, enable: bool) -> bool:
        input_signal_bar = self._not(input_signal)
        return super().__call__(input_signal, input_signal_bar, enable)

    def __str__(self):
        return f"D Flip-Flop: {super().__str__()}"
