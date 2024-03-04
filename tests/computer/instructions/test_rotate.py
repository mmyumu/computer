"""
Test for Rotation instructions
"""
from computer.data_types import Bits
from computer.instructions.rotate import ROL, ROR
from computer.memory import SRAM
from computer.registers import Registers



# pylint: disable=C0116,R0801
def test_ror(registers: Registers, sram: SRAM):
    sram.reset()
    registers.reset()

    d1 = Bits(1, 0, 0, 0, 0, 0, 0, 1)
    register_address1 = Bits(0, 0, 1)
    registers.write(register_address1, d1)

    imd = Bits(0, 0, 0, 0, 0, 0, 1, 0)

    registers.clock_tick(True)

    ror = ROR(registers, sram.size)
    operand = Bits(register_address1 + [0] * 3 + imd)
    ror(operand)
    registers.clock_tick(True)

    assert registers.read(register_address1) == [0, 1, 1, 0, 0, 0, 0, 0]
    assert registers.cf is False
    assert registers.zf is False

def test_ror_cf(registers: Registers, sram: SRAM):
    sram.reset()
    registers.reset()

    d1 = Bits(1, 1, 0, 0, 0, 0, 0, 1)
    register_address1 = Bits(0, 0, 1)
    registers.write(register_address1, d1)

    imd = Bits(0, 0, 0, 0, 0, 0, 0, 1)

    registers.clock_tick(True)

    ror = ROR(registers, sram.size)
    operand = Bits(register_address1 + [0] * 3 + imd)
    ror(operand)
    registers.clock_tick(True)

    assert registers.read(register_address1) == [1, 1, 1, 0, 0, 0, 0, 0]
    assert registers.cf is True
    assert registers.zf is False

def test_rol(registers: Registers, sram: SRAM):
    sram.reset()
    registers.reset()

    d1 = Bits(1, 0, 0, 0, 0, 0, 0, 1)
    register_address1 = Bits(0, 0, 1)
    registers.write(register_address1, d1)

    imd = Bits(0, 0, 0, 0, 0, 0, 1, 0)

    registers.clock_tick(True)

    rol = ROL(registers, sram.size)
    operand = Bits(register_address1 + [0] * 3 + imd)
    rol(operand)
    registers.clock_tick(True)

    assert registers.read(register_address1) == [0, 0, 0, 0, 0, 1, 1, 0]
    assert registers.cf is False
    assert registers.zf is False

def test_rol_cf(registers: Registers, sram: SRAM):
    sram.reset()
    registers.reset()

    d1 = Bits(1, 1, 0, 0, 0, 0, 0, 1)
    register_address1 = Bits(0, 0, 1)
    registers.write(register_address1, d1)

    imd = Bits(0, 0, 0, 0, 0, 0, 0, 1)

    registers.clock_tick(True)

    rol = ROL(registers, sram.size)
    operand = Bits(register_address1 + [0] * 3 + imd)
    rol(operand)
    registers.clock_tick(True)

    assert registers.read(register_address1) == [1, 0, 0, 0, 0, 0, 1, 1]
    assert registers.cf is True
    assert registers.zf is False
