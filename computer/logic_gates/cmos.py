"""
CMOS Gates implementations
"""
from computer.electronic.transistor import NMOSTransistor
from computer.electronic.transistor import PMOSTransistor
from computer.logic_gates.voltage_levels import GND, VDD


class NOTGate:
    """
    NOT logic gate using CMOS technology
    """
    def __init__(self):
        # Initialize one NMOS and one PMOS transistor
        self.nmos = NMOSTransistor()
        self.pmos = PMOSTransistor()

    def operate(self, input_signal: bool):
        """
        Logic gate operates input and returns output
        """
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


class NANDGate:
    """
    NAND logic gate using CMOS technology
    """
    def __init__(self):
        self.nmos_a = NMOSTransistor()
        self.nmos_b = NMOSTransistor()
        self.pmos_a = PMOSTransistor()
        self.pmos_b = PMOSTransistor()

    def operate(self, input_signal_a: bool, input_signal_b: bool):
        """
        Logic gate operates inputs and returns output
        """
        self.nmos_a.apply_control_signal(input_signal_a)
        self.pmos_a.apply_control_signal(input_signal_a)
        self.nmos_b.apply_control_signal(input_signal_b)
        self.pmos_b.apply_control_signal(input_signal_b)

        self.pmos_a.connect_source(VDD)
        self.pmos_b.connect_source(VDD)

        self.nmos_b.connect_source(GND)
        self.nmos_a.connect_source(self.nmos_b.is_conducting())

        return (self.pmos_a.is_conducting() or self.pmos_b.is_conducting()) and not self.nmos_a.is_conducting()

class NORGate:
    """
    NOR logic gate using CMOS technology
    """
    def __init__(self):
        self.nmos_a = NMOSTransistor()
        self.nmos_b = NMOSTransistor()
        self.pmos_a = PMOSTransistor()
        self.pmos_b = PMOSTransistor()

    def operate(self, input_signal_a: bool, input_signal_b: bool):
        """
        Logic gate operates inputs and returns output
        """
        self.nmos_a.apply_control_signal(input_signal_a)
        self.pmos_a.apply_control_signal(input_signal_a)
        self.nmos_b.apply_control_signal(input_signal_b)
        self.pmos_b.apply_control_signal(input_signal_b)

        self.nmos_a.connect_source(GND)
        self.nmos_b.connect_source(GND)

        self.pmos_a.connect_source(VDD)
        self.pmos_b.connect_source(self.pmos_a.is_conducting())

        return self.pmos_b.is_conducting() and not (self.nmos_a.is_conducting() or self.nmos_b.is_conducting())
