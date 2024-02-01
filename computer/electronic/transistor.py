"""
Transistor implementations
"""
from abc import ABC, abstractmethod

class Transistor(ABC):
    """
    Base class for transistors implementations
    """
    def __init__(self):
        self.control_gate = self._get_default_control_gate()    # On/Off
        self.source = False                                     # Input

    @abstractmethod
    def _get_default_control_gate(self):
        pass

    @abstractmethod
    def apply_control_signal(self, signal):
        """
        Apply signal on control gate
        """

    def connect_source(self, source):
        """
        Connect source (input) of the transistor
        """
        self.source = source

    def is_conducting(self):
        """
        Tells whether the transistor is conducting current or not (output).
        """
        return self.control_gate and self.source

    @property
    def drain(self):
        """
        Returns the drain value (aka if the transistor is conducting or not)
        """
        return self.is_conducting()


class NMOSTransistor(Transistor):
    """
    A NMOS transistor conducts current when the control gate is supplied with voltage.
    """
    def _get_default_control_gate(self):
        return False

    def apply_control_signal(self, signal):
        self.control_gate = signal


class PMOSTransistor(Transistor):
    """
    A PMOS transistor conducts current when the control gate is not supplied with voltage.
    """
    def _get_default_control_gate(self):
        return True

    def apply_control_signal(self, signal):
        self.control_gate = not signal
