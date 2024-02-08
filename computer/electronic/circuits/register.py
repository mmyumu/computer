"""
Registers module
"""
import random

from computer.electronic.circuits.flip_flop import DFlipFlop


class Register:
    """
    Register 4bits
    """
    def __init__(self, size=4) -> None:
        self._size = size
        self._d_flip_flops = tuple(DFlipFlop() for _ in range(size))

    def reset_states(self):
        """
        Reset state of the register
        """
        # TODO: Is it a good implementation of the reset?
        # It does not use the clock...
        for d_flip_flop in self._d_flip_flops:
            d_flip_flop.reset_states()

    def __str__(self):
        out_str = ""
        for i, d_flip_flop in enumerate(self._d_flip_flops[::-1]):
            out_str += f"{i}: {d_flip_flop}"

            if i != 0:
                out_str += " \n"

        return out_str


class SISORegister(Register):
    """
    SISO (Serial-In Serial-Out) register
    https://www.elprocus.com/siso-shift-register/
    """
    def __init__(self, size=4) -> None:
        super().__init__(size=size)
        self._d = bool(random.getrandbits(1))

    @property
    def output(self):
        """
        Return the output of the register
        """
        return self._d_flip_flops[0].q

    def set_d(self, input_d: bool):
        """
        Set the D input of the register
        """
        self._d = input_d

    def reset_states(self):
        super().reset_states()
        # TODO: Is it magical to force input value on reset?
        self._d = False

    def clock_tick(self, enable: bool):
        """
        Update flip-flop status on clock tick
        """
        for i, d_flip_flop in enumerate(self._d_flip_flops):
            if i < len(self._d_flip_flops) - 1:
                previous_d_flip_flop = self._d_flip_flops[i + 1]
                d_flip_flop.set_d(previous_d_flip_flop.q)
            else:
                d_flip_flop.set_d(self._d)

        for d_flip_flop in self._d_flip_flops:
            d_flip_flop.clock_tick(enable)

        return self.output


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
        return tuple(d_flip_flop.q for d_flip_flop in self._d_flip_flops[::-1])


class PIPORegister(Register):
    """
    SISO (Serial-In Serial-Out) register
    https://www.elprocus.com/sipo-shift-register/
    """
    def __init__(self, size=4) -> None:
        super().__init__(size=size)

        self._ds = []
        for _ in range(size):
            self._ds.append(bool(random.getrandbits(1)))

    @property
    def output(self):
        """
        Return the output of the register
        """
        return tuple(d_flip_flop.q for d_flip_flop in self._d_flip_flops[::-1])

    def reset_states(self):
        super().reset_states()

        # TODO: Is it magical to force input values on reset?
        self._ds = [False] * self._size

    def set_d(self, *args):
        """
        Set inputs d3, d2, d1, d0 of the register
        """

        if not isinstance(args, (list, tuple)) or len(args) != self._size:
            raise ValueError(f"Inputs should be {self._size} bits but are: {args}")

        self._ds = args[::-1]

    def clock_tick(self, enable: bool):
        """
        Update flip-flop status on clock tick
        """
        for d_flip_flop, d_input in zip(self._d_flip_flops, self._ds):
            d_flip_flop.set_d(d_input)

        for d_flip_flop in self._d_flip_flops:
            d_flip_flop.clock_tick(enable)

        return self.output
