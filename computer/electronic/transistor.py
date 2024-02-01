from abc import ABC, abstractmethod

class Transistor(ABC):
    def __init__(self):
        self.control_gate = self._get_default_control_gate()    # On/Off
        self.source = False                                     # Input

    @abstractmethod
    def _get_default_control_gate(self):
        pass

    @abstractmethod
    def apply_control_signal(self, signal):
        pass

    def connect_source(self, source):
        self.source = source

    def is_conducting(self):
        return self.control_gate and self.source

    @property
    def drain(self):
        return self.is_conducting()
