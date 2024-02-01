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

    def operate(self, input_signal: bool) -> bool:
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
        return self.pmos.drain and not self.nmos.drain


class NANDGate:
    """
    NAND logic gate using CMOS technology
    """
    def __init__(self):
        self.nmos_a = NMOSTransistor()
        self.nmos_b = NMOSTransistor()
        self.pmos_a = PMOSTransistor()
        self.pmos_b = PMOSTransistor()

    def operate(self, input_signal_a: bool, input_signal_b: bool) -> bool:
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
        self.nmos_a.connect_source(self.nmos_b.drain)

        return (self.pmos_a.drain or self.pmos_b.drain) and not self.nmos_a.drain

class NORGate:
    """
    NOR logic gate using CMOS technology
    """
    def __init__(self):
        self.nmos_a = NMOSTransistor()
        self.nmos_b = NMOSTransistor()
        self.pmos_a = PMOSTransistor()
        self.pmos_b = PMOSTransistor()

    def operate(self, input_signal_a: bool, input_signal_b: bool) -> bool:
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
        self.pmos_b.connect_source(self.pmos_a.drain)

        return self.pmos_b.drain and not (self.nmos_a.drain or self.nmos_b.drain)


class ANDGate:
    """
    AND logic gate using CMOS technology
    """
    def __init__(self):
        self._nand_gate = NANDGate()
        self._not_gate = NOTGate()

    def operate(self, input_signal_a: bool, input_signal_b: bool) -> bool:
        """
        Logic gate operates inputs and returns output
        """
        return self._not_gate.operate(self._nand_gate.operate(input_signal_a, input_signal_b))


class ORGate:
    """
    OR logic gate using CMOS technology
    """
    def __init__(self):
        self._nor_gate = NORGate()
        self._not_gate = NOTGate()

    def operate(self, input_signal_a: bool, input_signal_b: bool) -> bool:
        """
        Logic gate operates inputs and returns output
        """
        return self._not_gate.operate(self._nor_gate.operate(input_signal_a, input_signal_b))


class XORGate:
    """
    XOR logic gate using CMOS technology
    """
    def __init__(self):
        self._nmos_a = NMOSTransistor()
        self._nmos_a_bar = NMOSTransistor()
        self._nmos_b = NMOSTransistor()
        self._nmos_b_bar = NMOSTransistor()
        self._pmos_a = PMOSTransistor()
        self._pmos_a_bar = PMOSTransistor()
        self._pmos_b = PMOSTransistor()
        self._pmos_b_bar = PMOSTransistor()

    def operate(self, input_signal_a: bool, input_signal_b: bool) -> bool:
        """
        Logic gate operates inputs and returns output
        """
        self._pmos_a_bar.apply_control_signal(not input_signal_a)
        self._pmos_a.apply_control_signal(input_signal_a)
        self._pmos_b_bar.apply_control_signal(not input_signal_b)
        self._pmos_b.apply_control_signal(input_signal_b)

        self._nmos_a_bar.apply_control_signal(not input_signal_a)
        self._nmos_a.apply_control_signal(input_signal_a)
        self._nmos_b_bar.apply_control_signal(not input_signal_b)
        self._nmos_b.apply_control_signal(input_signal_b)

        self._pmos_a_bar.connect_source(VDD)
        self._pmos_a.connect_source(VDD)
        self._nmos_b_bar.connect_source(GND)
        self._nmos_b.connect_source(GND)

        self._nmos_a_bar.connect_source(self._nmos_b_bar.drain)
        self._nmos_a.connect_source(self._nmos_b.drain)
        self._pmos_b_bar.connect_source(self._pmos_a.drain)
        self._pmos_b.connect_source(self._pmos_a_bar.drain)

        return (self._pmos_b.drain or self._pmos_b_bar.drain) and (not self._nmos_a_bar.drain or not self._nmos_a.drain)
