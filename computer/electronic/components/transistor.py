"""
Transistor implementations
"""
from abc import ABC, abstractmethod

class Transistor(ABC):
    """
    Base class for transistors implementations
    """
    def __init__(self):
        self.control_gate = False    # On/Off
        self.source = False          # Input

    def apply_control_signal(self, signal):
        """
        Apply signal on control gate
        """
        assert signal is not None
        self.control_gate = signal

    def connect_source(self, source):
        """
        Connect source (input) of the transistor
        """
        assert source is not None
        self.source = source

    @abstractmethod
    def is_conducting(self):
        """
        Tells whether the transistor is conducting current or not (output).
        """

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
    def is_conducting(self):
        return self.control_gate and self.source


class PMOSTransistor(Transistor):
    """
    A PMOS transistor conducts current when the control gate is not supplied with voltage.
    """
    def is_conducting(self):
        return not self.control_gate and self.source
