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
        # TODO: check if this is a correct way to reset or a hack
        self._q = True
        self._q_bar = True


class SRFlipFlop(FlipFlop):
    """
    Set/Reset flip flop
    https://www.javatpoint.com/basics-of-flip-flop-in-digital-electronics
    """
    def __init__(self):
        super().__init__()
        self._nand0 = NANDGate()
        self._nand1 = NANDGate()

    def __call__(self, input_set: bool, input_reset: bool) -> Tuple[bool, bool]:
        """
        Met à jour les états Q et notQ en fonction des entrées S (Set) et R (Reset).
        :param S: Entrée Set (active basse)
        :param R: Entrée Reset (active basse)
        """
        if input_set and input_reset:
            raise ValueError("Invalid state: set and reset both high")

        new_q = self._nand0(not input_set, self._q_bar)

        # TODO: computation uses current state of Q (using new_q), it is weird but it seems it works
        new_q_bar = self._nand1(new_q, not input_reset)

        self._q = new_q
        self._q_bar = new_q_bar

        return self._q, self._q_bar


class DFlipFlop(FlipFlop):
    """
    D flip flop
    https://www.paturage.be/electro/inforauto/portes/bascule.html
    """
    def __init__(self):
        super().__init__()
        self._not = NOTGate()
        self._nand0 = NANDGate()
        self._nand1 = NANDGate()
        self._nand2 = NANDGate()
        self._nand3 = NANDGate()

    def __call__(self, input_signal: bool, enable: bool) -> bool:
        input_signal_bar = self._not(input_signal)

        nand0 = self._nand0(input_signal, enable)
        nand1 = self._nand1(input_signal_bar, enable)

        new_q = self._nand2(nand0, self._q_bar)

        # TODO: computation uses current state of Q (using new_q), it is weird but it seems it works
        new_q_bar = self._nand1(new_q, nand1)

        self._q = new_q
        self._q_bar = new_q_bar

        return self._q, self._q_bar
