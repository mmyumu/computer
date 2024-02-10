"""
Binary decoders
"""
from typing import Tuple
from computer.electronic.circuits.cmos import ANDGate, ANDGate3, NOTGate

# pylint: disable=R0913,R0914

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

        self._and_gates = [ANDGate()] * 8

    def __call__(self, input_signal_a2: bool, input_signal_a1: bool, input_signal_a0: bool, enable: bool) -> Tuple[bool, bool, bool, bool]:
        """
        Logic gate operates inputs and returns outputs
        """
        not2 = self._not(input_signal_a2)
        low = self._decoder2to4_0(input_signal_a1, input_signal_a0, not2)
        high = self._decoder2to4_1(input_signal_a1, input_signal_a0, input_signal_a2)

        ds = []
        for d, and_gate in zip(high + low, self._and_gates):
            ds.append(and_gate(d, enable))

        return ds


class Decoder4To16:
    """
    4-to-16 binary decoder
    https://www.tutorialspoint.com/digital_circuits/digital_circuits_decoders.htm
    """
    def __init__(self):
        self._not = NOTGate()
        self._decoder3to8_0 = Decoder3To8()
        self._decoder3to8_1 = Decoder3To8()

        self._and_gates = [ANDGate()] * 16

    def __call__(self, input_signal_a3: bool, input_signal_a2: bool, input_signal_a1: bool, input_signal_a0: bool,
                 enable: bool) -> Tuple[bool, bool, bool, bool]:
        """
        Logic gate operates inputs and returns outputs
        """
        not3 = self._not(input_signal_a3)

        low = self._decoder3to8_0(input_signal_a2, input_signal_a1, input_signal_a0, not3)
        high = self._decoder3to8_0(input_signal_a2, input_signal_a1, input_signal_a0, input_signal_a3)

        ds = []
        for d, and_gate in zip(high + low, self._and_gates):
            ds.append(and_gate(d, enable))

        return ds


class Decoder5To32:
    """
    5-to-32 binary decoder
    """
    def __init__(self):
        self._not = NOTGate()
        self._decoder4to16_0 = Decoder4To16()
        self._decoder4to16_1 = Decoder4To16()

        self._and_gates = [ANDGate()] * 32

    def __call__(self, input_signal_a4: bool, input_signal_a3: bool, input_signal_a2: bool, input_signal_a1: bool,
                 input_signal_a0: bool, enable: bool) -> Tuple[bool, bool, bool, bool]:
        """
        Logic gate operates inputs and returns outputs
        """
        not4 = self._not(input_signal_a4)

        low = self._decoder4to16_0(input_signal_a3, input_signal_a2, input_signal_a1, input_signal_a0, not4)
        high = self._decoder4to16_1(input_signal_a3, input_signal_a2, input_signal_a1, input_signal_a0, input_signal_a4)

        ds = []
        for d, and_gate in zip(high + low, self._and_gates):
            ds.append(and_gate(d, enable))

        return ds


class Decoder6To64:
    """
    6-to-64 binary decoder
    """
    def __init__(self):
        self._not = NOTGate()
        self._decoder5to32_0 = Decoder5To32()
        self._decoder5to32_1 = Decoder5To32()

        self._and_gates = [ANDGate()] * 64

    def __call__(self, input_signal_a5: bool, input_signal_a4: bool, input_signal_a3: bool, input_signal_a2: bool,
                 input_signal_a1: bool, input_signal_a0: bool, enable: bool) -> Tuple[bool, bool, bool, bool]:
        """
        Logic gate operates inputs and returns outputs
        """
        not5 = self._not(input_signal_a5)

        low = self._decoder5to32_0(input_signal_a4, input_signal_a3, input_signal_a2, input_signal_a1, input_signal_a0, not5)
        high = self._decoder5to32_0(input_signal_a4, input_signal_a3, input_signal_a2, input_signal_a1, input_signal_a0, input_signal_a5)

        ds = []
        for d, and_gate in zip(high + low, self._and_gates):
            ds.append(and_gate(d, enable))

        return ds


class Decoder7To128:
    """
    7-to-128 binary decoder
    """
    def __init__(self):
        self._not = NOTGate()
        self._decoder6to64_0 = Decoder6To64()
        self._decoder6to64_1 = Decoder6To64()

        self._and_gates = [ANDGate()] * 128

    def __call__(self, input_signal_a6: bool, input_signal_a5: bool, input_signal_a4: bool, input_signal_a3: bool,
                 input_signal_a2: bool, input_signal_a1: bool, input_signal_a0: bool, enable: bool) -> Tuple[bool, bool, bool, bool]:
        """
        Logic gate operates inputs and returns outputs
        """
        not6 = self._not(input_signal_a6)

        low = self._decoder6to64_0(input_signal_a5, input_signal_a4, input_signal_a3,
                                   input_signal_a2, input_signal_a1, input_signal_a0, not6)
        high = self._decoder6to64_0(input_signal_a5, input_signal_a4, input_signal_a3,
                                    input_signal_a2, input_signal_a1, input_signal_a0, input_signal_a6)

        ds = []
        for d, and_gate in zip(high + low, self._and_gates):
            ds.append(and_gate(d, enable))

        return ds


class Decoder8To256:
    """
    7-to-128 binary decoder
    """
    def __init__(self):
        self._not = NOTGate()
        self._decoder7to128_0 = Decoder7To128()
        self._decoder7to128_1 = Decoder7To128()

        self._and_gates = [ANDGate()] * 256

    def __call__(self, input_signal_a7: bool, input_signal_a6: bool, input_signal_a5: bool, input_signal_a4: bool,
                 input_signal_a3: bool, input_signal_a2: bool, input_signal_a1: bool, input_signal_a0: bool,
                 enable: bool) -> Tuple[bool, bool, bool, bool]:
        """
        Logic gate operates inputs and returns outputs
        """
        not7 = self._not(input_signal_a7)

        low = self._decoder7to128_0(input_signal_a6, input_signal_a5, input_signal_a4, input_signal_a3,
                                   input_signal_a2, input_signal_a1, input_signal_a0, not7)
        high = self._decoder7to128_1(input_signal_a6, input_signal_a5, input_signal_a4, input_signal_a3,
                                    input_signal_a2, input_signal_a1, input_signal_a0, input_signal_a7)

        ds = []
        for d, and_gate in zip(high + low, self._and_gates):
            ds.append(and_gate(d, enable))

        return ds


class Decoder:
    """
    Generic binary decoder that dynamically creates a decoder of size 2^N to 2^(N+1).
    """
    def __init__(self, depth: int):
        if depth == 1:
            raise ValueError("Depth must be greater than or equal to 2")

        self.depth = depth
        self._not_gate = NOTGate()
        if depth == 2:
            self._and_gates = [ANDGate3() for _ in range(2 ** depth)]
        else:
            self._and_gates = [ANDGate() for _ in range(2 ** depth)]
            self.lower_half = Decoder(depth - 1)
            self.upper_half = Decoder(depth - 1)

    def __call__(self, *inputs: bool, enable: bool = True) -> Tuple[bool, ...]:
        if len(inputs) != self.depth:
            raise ValueError(f"Expected {self.depth} input signals, got {len(inputs)}.")

        # Base case for a 2-to-4 decoder
        if self.depth == 2:
            input_signal_a1, input_signal_a0 = inputs
            not_a0 = self._not_gate(input_signal_a0)
            not_a1 = self._not_gate(input_signal_a1)
            outputs = (
                self._and_gates[0](not_a1, not_a0, enable),
                self._and_gates[1](not_a1, input_signal_a0, enable),
                self._and_gates[2](input_signal_a1, not_a0, enable),
                self._and_gates[3](input_signal_a1, input_signal_a0, enable),
            )
            return outputs[::-1]

        # Recursive case for decoders larger than 2-to-4
        not_input = self._not_gate(inputs[0])
        lower_outputs = self.lower_half(*inputs[1:], enable=not_input)
        upper_outputs = self.upper_half(*inputs[1:], enable=inputs[0])

        # Combine outputs from lower and upper halves through AND gates with the enable signal
        combined_outputs = tuple(self._and_gates[i](output, enable) for i, output in enumerate(upper_outputs + lower_outputs))
        return combined_outputs
