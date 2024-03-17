"""
Program Counter (PC) module.
Program Counter increments its counter to point to the next instruction.
"""
from computer.data_types import Bits
from computer.electronic.circuits.adder import HalfAdder
from computer.electronic.circuits.register import PIPORegister


class ProgramCounter:
    """
    Program counter class.
    The counter is stored in a register.
    Use HalfAdder and Full adder to increment the register value.
    """
    def __init__(self, size=4):
        self._register = PIPORegister(size=2 ** size)

        self._half_adders = []
        for _ in range(2 ** size):
            self._half_adders.append(HalfAdder())

    def increment(self):
        """
        Increments the counter.
        """
        # Get bits from register
        bits = self._register.output

        # Perform increment
        new_bits = []
        for i, bit in enumerate(bits[::-1]):
            if i == 0:
                new_bit, carry = self._half_adders[i](bit, True)
            else:
                new_bit, carry = self._half_adders[i](bit, carry)
            new_bits.append(new_bit)

        if carry:
            raise ValueError("Program counter overflow.")

        # Update register
        self._register.set_d(*new_bits[::-1])

    def set(self, value: Bits):
        """
        Set the program counter to the given value

        Args:
            value (Bits): the value to set
        """
        self._register.set_d(*value)

    def clock_tick(self, enable: bool):
        """
        Update the program counter on clock tick
        """
        self._register.clock_tick(enable)

    @property
    def value(self):
        """
        Get the current counter value
        """
        return self._register.output

    def reset(self):
        """
        Reset the counter to initial state.
        """
        self._register.reset_states()
