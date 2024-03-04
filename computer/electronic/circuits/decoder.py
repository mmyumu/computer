"""
Binary decoders
"""
from typing import Tuple
from computer.electronic.circuits.cmos import ANDGate, ANDGate3, NOTGate

# pylint: disable=R0913,R0914

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
