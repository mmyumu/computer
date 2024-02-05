"""
Program Counter (PC) module.
Program Counter increments its counter to point to the next instruction.
"""
from computer.electronic.circuits.adder import FullAdder, HalfAdder
from computer.electronic.circuits.register import SIPORegister


class ProgramCounter:
    """
    Program counter class.
    The counter is stored in a register.
    Use HalfAdder and Full adder to increment the register value.
    """
    def __init__(self):
        self._register = SIPORegister()
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
        self._register.set_d(b0)
        self._register.clock_tick(True)
        self._register.set_d(b1)
        self._register.clock_tick(True)
        self._register.set_d(b2)
        self._register.clock_tick(True)
        self._register.set_d(b3)
        self._register.clock_tick(True)

    @property
    def value(self):
        """
        Get the current counter value
        """
        return self._register.output

        # bits[0] = sum_bit
        # # On propage le retenue à travers les autres bits
        # for i in range(1, 4):
        #     sum_bit, new_carry = self.incrementer(bits[i], carry)
        #     bits[i] = sum_bit
        #     carry = new_carry
        # Mise à jour du registre avec la nouvelle valeur
        # for i, bit in enumerate(reversed(bits)):
        #     self.value(bit, self.clock.get_clock_state())

    # def get_value(self):
    #     return [self.value._d_flip_flop3._q, self.value._d_flip_flop2._q,
    #             self.value._d_flip_flop1._q, self.value._d_flip_flop0._q]

    # def set_value(self, new_value):
    #     # Cette fonction permet de définir manuellement la valeur du PC (pour les branchements par exemple)
    #     for bit in new_value:
    #         self.value(bit, self.clock.get_clock_state())

    def reset(self):
        """
        Reset the counter to initial state.
        """
        self._register.reset_states()
