from computer.electronic.transistor import Transistor


class PMOSTransistor(Transistor):
    """
    A PMOS transistor conducts current when the control gate is not supplied with voltage.
    """
    def _get_default_control_gate(self):
        return True
    
    def apply_control_signal(self, signal):
        self.control_gate = not signal
