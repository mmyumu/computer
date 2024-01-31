

from electronic.nmos_transistor import NMOSTransistor
from electronic.pmos_transistor import PMOSTransistor


def test_transistor_nmos_no_source(nmos_transistor: NMOSTransistor):
    assert not nmos_transistor.is_conducting()

def test_transistor_pmos_no_source(pmos_transistor: PMOSTransistor):
    assert not pmos_transistor.is_conducting()

def test_transistor_nmos_source_false(nmos_transistor: NMOSTransistor):
    nmos_transistor.connect_source(False)
    assert not nmos_transistor.is_conducting()

def test_transistor_pmos_source_false(pmos_transistor: PMOSTransistor):
    pmos_transistor.connect_source(False)
    assert not pmos_transistor.is_conducting()

def test_transistor_nmos_source_true_no_control_signal(nmos_transistor: NMOSTransistor):
    nmos_transistor.connect_source(True)
    assert not nmos_transistor.is_conducting()

def test_transistor_pmos_source_true_no_control_signal(pmos_transistor: PMOSTransistor):
    pmos_transistor.connect_source(True)
    assert pmos_transistor.is_conducting()

def test_transistor_nmos_source_true_control_signal_false(nmos_transistor: NMOSTransistor):
    nmos_transistor.connect_source(True)
    nmos_transistor.apply_control_signal(False)
    assert not nmos_transistor.is_conducting()

def test_transistor_pmos_source_true_control_signal_false(pmos_transistor: PMOSTransistor):
    pmos_transistor.connect_source(True)
    pmos_transistor.apply_control_signal(False)
    assert pmos_transistor.is_conducting()

def test_transistor_nmos_source_true_control_signal_true(nmos_transistor: NMOSTransistor):
    nmos_transistor.connect_source(True)
    nmos_transistor.apply_control_signal(True)
    assert nmos_transistor.is_conducting()

def test_transistor_pmos_source_true_control_signal_true(pmos_transistor: PMOSTransistor):
    pmos_transistor.connect_source(True)
    pmos_transistor.apply_control_signal(True)
    assert not pmos_transistor.is_conducting()