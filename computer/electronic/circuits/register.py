"""
Registers module
"""

from abc import ABC, abstractmethod
from typing import Tuple

from computer.electronic.circuits.flip_flop import DFlipFlop


class Register(ABC):
    """
    Base class for register
    """
    @abstractmethod
    def reset_states(self):
        """
        Reset state of the register
        """


class SISORegister(Register):
    """
    SISO (Serial-In Serial-Out) register
    https://www.elprocus.com/siso-shift-register/
    """
    def __init__(self) -> None:
        self._d_flip_flop0 = DFlipFlop()
        self._d_flip_flop1 = DFlipFlop()
        self._d_flip_flop2 = DFlipFlop()
        self._d_flip_flop3 = DFlipFlop()

    def __call__(self, input_signal: bool, enable: bool) -> bool:
        q0, _ = self._d_flip_flop0(self._d_flip_flop1._q, enable)
        self._d_flip_flop1(self._d_flip_flop2._q, enable)
        self._d_flip_flop2(self._d_flip_flop3._q, enable)
        self._d_flip_flop3(input_signal, enable)
        return q0

    def reset_states(self):
        # TODO: Is it a good implementation of the reset?
        # It does not use the clock...
        self._d_flip_flop3.reset_states()
        self._d_flip_flop2.reset_states()
        self._d_flip_flop1.reset_states()
        self._d_flip_flop0.reset_states()

    def __str__(self):
        out_str = f"3: {self._d_flip_flop3} \n"
        out_str += f"2: {self._d_flip_flop2} \n"
        out_str += f"1: {self._d_flip_flop1} \n"
        out_str += f"0: {self._d_flip_flop0}"

        return out_str

class SIPORegister(Register):
    """
    SISO (Serial-In Serial-Out) register
    https://www.elprocus.com/sipo-shift-register/
    """
    def __init__(self) -> None:
        pass

    def __call__(self, input_signal: bool, enable: bool) -> Tuple[bool, bool, bool, bool]:
        return False, False, False, False

    def reset_states(self):
        pass
