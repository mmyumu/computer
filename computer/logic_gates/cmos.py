from electronic.nmos_transistor import NMOSTransistor
from electronic.pmos_transistor import PMOSTransistor


class NOTGate:
    def __init__(self):
        self.nmos = NMOSTransistor()
        self.pmos = PMOSTransistor()

    def operate(self, input_signal):
        self.nmos.apply_control_signal(input_signal)
        self.pmos.apply_control_signal(input_signal)

        self.nmos.connect_source(False)
        self.pmos.connect_source(True)

        return not self.nmos.is_conducting()