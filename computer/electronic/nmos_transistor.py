from electronic.transistor import Transistor


class NMOSTransistor(Transistor):
    """
    A NMOS transistor conducts current when the control gate is supplied with voltage.
    """
    def _get_default_control_gate(self):
        return False

    def apply_control_signal(self, signal):
        self.control_gate = signal
