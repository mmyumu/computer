"""
Custom implementation of Logic gate (for testing purpose)
"""
from computer.electronic.transistor import PMOSTransistor
from computer.logic_gates.voltage_levels import VDD


class NOTGate:
    """
    Custom implementation of NOT Gate.
    According to ChatGPT, it works in simulation, but it would not work in real life.

    """
    def __init__(self):
        self.pmos = PMOSTransistor()

    def operate(self, input_signal):
        """
        Logic gate operates input and returns output
        """
        self.pmos.connect_source(VDD)

        self.pmos.apply_control_signal(input_signal)

        return self.pmos.is_conducting()
