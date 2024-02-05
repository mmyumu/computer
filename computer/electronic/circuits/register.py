"""
Registers module
"""

from abc import ABC, abstractmethod
import random
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

        self._d = bool(random.getrandbits(1))

    @property
    def output(self):
        """
        Return the output of the register
        """
        return self._d_flip_flop0.q

    # def __call__(self, input_signal: bool, enable: bool) -> bool:
    def set_d(self, input_d: bool):
        """
        Set the D input of the register
        """
        self._d = input_d

    def clock_tick(self, enable: bool):
        """
        Update flip-flop status on clock tick
        """
        self._d_flip_flop0.set_d(self._d_flip_flop1.q)
        self._d_flip_flop1.set_d(self._d_flip_flop2.q)
        self._d_flip_flop2.set_d(self._d_flip_flop3.q)
        self._d_flip_flop3.set_d(self._d)

        self._d_flip_flop0.clock_tick(enable)
        self._d_flip_flop1.clock_tick(enable)
        self._d_flip_flop2.clock_tick(enable)
        self._d_flip_flop3.clock_tick(enable)

        return self.output

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

class SIPORegister(SISORegister):
    """
    SISO (Serial-In Serial-Out) register
    https://www.elprocus.com/sipo-shift-register/
    """
    @property
    def output(self):
        """
        Return the output of the register
        """
        return self._d_flip_flop3.q, self._d_flip_flop2.q, self._d_flip_flop1.q, self._d_flip_flop0.q

    # def clock_tick(self, enable: bool):
    #     super().clock_tick(enable)
    #     return self._d_flip_flop3.q, self._d_flip_flop2.q, self._d_flip_flop1.q, self._d_flip_flop0.q
