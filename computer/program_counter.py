"""
Program Counter (PC) module.
Program Counter increments its counter to point to the next instruction.
"""
from computer.electronic.circuits.adder import FullAdder, HalfAdder
from computer.electronic.circuits.register import PIPORegister4


class ProgramCounter:
    """
    Program counter class.
    The counter is stored in a register.
    Use HalfAdder and Full adder to increment the register value.
    """
    def __init__(self):
        self._register = PIPORegister4()
        self._half_adder = HalfAdder()
        self._full_adder = FullAdder()

    def increment(self):
        """
        Increments the counter.
        """
        # Get bits from register
        b3, b2, b1, b0 = self._register.output

        # Perform increment
        b0, carry = self._half_adder(b0, True)
        b1, carry = self._half_adder(b1, carry)
        b2, carry = self._half_adder(b2, carry)
        b3, carry = self._half_adder(b3, carry)

        if carry:
            raise ValueError("Program counter overflow.")

        # Update register
        self._register.set_d(b3, b2, b1, b0)

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
