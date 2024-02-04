"""
CMOS Gates implementations
"""
from computer.electronic.components.transistor import NMOSTransistor
from computer.electronic.components.transistor import PMOSTransistor
from computer.electronic.circuits.voltage_levels import GND, VDD


class NOTGate:
    """
    NOT logic gate using CMOS technology
    """
    def __init__(self):
        # Initialize one NMOS and one PMOS transistor
        self._nmos = NMOSTransistor()
        self._pmos = PMOSTransistor()

    def __call__(self, input_signal: bool) -> bool:
        """
        Logic gate operates input and returns output
        """
        # Apply the input signal to the control gates of both transistors
        self._nmos.apply_control_signal(input_signal)
        self._pmos.apply_control_signal(input_signal)

        # Connect the source of the NMOS transistor to ground (GND)
        self._nmos.connect_source(GND)

        # Connect the source of the PMOS transistor to Vdd (positive supply voltage)
        self._pmos.connect_source(VDD)

        # The output is high if the PMOS is conducting and the NMOS is not
        # This occurs when the input is low (False)
        # Note that for a CMOS NOT gate, we must check the conduction state of both transistors
        return self._pmos.drain and not self._nmos.drain


class NANDGate:
    """
    NAND logic gate using CMOS technology
    """
    def __init__(self):
        self._nmos_a = NMOSTransistor()
        self._nmos_b = NMOSTransistor()
        self._pmos_a = PMOSTransistor()
        self._pmos_b = PMOSTransistor()

    def __call__(self, input_signal_a: bool, input_signal_b: bool) -> bool:
        """
        Logic gate operates inputs and returns output
        """
        self._nmos_a.apply_control_signal(input_signal_a)
        self._pmos_a.apply_control_signal(input_signal_a)
        self._nmos_b.apply_control_signal(input_signal_b)
        self._pmos_b.apply_control_signal(input_signal_b)

        self._pmos_a.connect_source(VDD)
        self._pmos_b.connect_source(VDD)

        self._nmos_b.connect_source(GND)
        self._nmos_a.connect_source(self._nmos_b.drain)

        return (self._pmos_a.drain or self._pmos_b.drain) and not self._nmos_a.drain

class NORGate:
    """
    NOR logic gate using CMOS technology
    """
    def __init__(self):
        self._nmos_a = NMOSTransistor()
        self._nmos_b = NMOSTransistor()
        self._pmos_a = PMOSTransistor()
        self._pmos_b = PMOSTransistor()

    def __call__(self, input_signal_a: bool, input_signal_b: bool) -> bool:
        """
        Logic gate operates inputs and returns output
        """
        self._nmos_a.apply_control_signal(input_signal_a)
        self._pmos_a.apply_control_signal(input_signal_a)
        self._nmos_b.apply_control_signal(input_signal_b)
        self._pmos_b.apply_control_signal(input_signal_b)

        self._nmos_a.connect_source(GND)
        self._nmos_b.connect_source(GND)

        self._pmos_a.connect_source(VDD)
        self._pmos_b.connect_source(self._pmos_a.drain)

        return self._pmos_b.drain and not (self._nmos_a.drain or self._nmos_b.drain)


class ANDGate:
    """
    AND logic gate using CMOS technology
    """
    def __init__(self):
        self._nand_gate = NANDGate()
        self._not_gate = NOTGate()

    def __call__(self, input_signal_a: bool, input_signal_b: bool) -> bool:
        """
        Logic gate operates inputs and returns output
        """
        return self._not_gate(self._nand_gate(input_signal_a, input_signal_b))


class ORGate:
    """
    OR logic gate using CMOS technology
    """
    def __init__(self):
        self._nor_gate = NORGate()
        self._not_gate = NOTGate()

    def __call__(self, input_signal_a: bool, input_signal_b: bool) -> bool:
        """
        Logic gate operates inputs and returns output
        """
        return self._not_gate(self._nor_gate(input_signal_a, input_signal_b))


class XORGate:
    """
    XOR logic gate using CMOS technology
    https://vlsi-iitg.vlabs.ac.in/images/4.3.png
    """
    def __init__(self):
        self._pmos_a = PMOSTransistor()
        self._pmos_a_bar = PMOSTransistor()
        self._pmos_b = PMOSTransistor()
        self._pmos_b_bar = PMOSTransistor()
        self._nmos_a = NMOSTransistor()
        self._nmos_a_bar = NMOSTransistor()
        self._nmos_b = NMOSTransistor()
        self._nmos_b_bar = NMOSTransistor()


    def __call__(self, input_signal_a: bool, input_signal_b: bool) -> bool:
        """
        Logic gate operates inputs and returns output
        """
        self._pmos_a.apply_control_signal(input_signal_a)
        self._pmos_a_bar.apply_control_signal(not input_signal_a)
        self._pmos_b_bar.apply_control_signal(not input_signal_b)
        self._pmos_b.apply_control_signal(input_signal_b)

        self._nmos_a.apply_control_signal(input_signal_a)
        self._nmos_a_bar.apply_control_signal(not input_signal_a)
        self._nmos_b.apply_control_signal(input_signal_b)
        self._nmos_b_bar.apply_control_signal(not input_signal_b)

        self._pmos_a.connect_source(VDD)
        self._pmos_a_bar.connect_source(VDD)
        self._nmos_b.connect_source(GND)
        self._nmos_b_bar.connect_source(GND)

        self._pmos_b_bar.connect_source(self._pmos_a.drain)
        self._pmos_b.connect_source(self._pmos_a_bar.drain)
        self._nmos_a.connect_source(self._nmos_b.drain)
        self._nmos_a_bar.connect_source(self._nmos_b_bar.drain)

        return (self._pmos_b.drain or self._pmos_b_bar.drain) and (not self._nmos_a_bar.drain or not self._nmos_a.drain)


class XNORGate:
    """
    XNOR logic gate using CMOS technology
    https://vlsi-iitg.vlabs.ac.in/images/4.3.png
    """
    def __init__(self):
        self._pmos_a = PMOSTransistor()
        self._pmos_a_bar = PMOSTransistor()
        self._pmos_b = PMOSTransistor()
        self._pmos_b_bar = PMOSTransistor()
        self._nmos_a = NMOSTransistor()
        self._nmos_a_bar = NMOSTransistor()
        self._nmos_b = NMOSTransistor()
        self._nmos_b_bar = NMOSTransistor()


    def __call__(self, input_signal_a: bool, input_signal_b: bool) -> bool:
        """
        Logic gate operates inputs and returns output
        """
        self._pmos_a.apply_control_signal(input_signal_a)
        self._pmos_a_bar.apply_control_signal(not input_signal_a)
        self._pmos_b.apply_control_signal(input_signal_b)
        self._pmos_b_bar.apply_control_signal(not input_signal_b)

        self._nmos_a.apply_control_signal(input_signal_a)
        self._nmos_a_bar.apply_control_signal(not input_signal_a)
        self._nmos_b_bar.apply_control_signal(not input_signal_b)
        self._nmos_b.apply_control_signal(input_signal_b)

        self._pmos_a.connect_source(VDD)
        self._pmos_a_bar.connect_source(VDD)
        self._nmos_b_bar.connect_source(GND)
        self._nmos_b.connect_source(GND)

        self._pmos_b.connect_source(self._pmos_a.drain)
        self._pmos_b_bar.connect_source(self._pmos_a_bar.drain)
        self._nmos_a.connect_source(self._nmos_b_bar.drain)
        self._nmos_a_bar.connect_source(self._nmos_b.drain)

        return (self._pmos_b.drain or self._pmos_b_bar.drain) and (not self._nmos_a_bar.drain or not self._nmos_a.drain)
