from electronic.nmos_transistor import NMOSTransistor
from electronic.pmos_transistor import PMOSTransistor
from logic_gates.voltage_levels import GND, VDD


class NOTGate:
    def __init__(self):
        # Initialize one NMOS and one PMOS transistor
        self.nmos = NMOSTransistor()
        self.pmos = PMOSTransistor()

    def operate(self, input_signal):
        # Apply the input signal to the control gates of both transistors
        self.nmos.apply_control_signal(input_signal)
        self.pmos.apply_control_signal(input_signal)

        # Connect the source of the NMOS transistor to ground (GND)
        self.nmos.connect_source(GND)

        # Connect the source of the PMOS transistor to Vdd (positive supply voltage)
        self.pmos.connect_source(VDD)

        # The output is high if the PMOS is conducting and the NMOS is not
        # This occurs when the input is low (False)
        # Note that for a CMOS NOT gate, we must check the conduction state of both transistors
        return self.pmos.is_conducting() and not self.nmos.is_conducting()
