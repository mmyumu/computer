"""
Test for Logic instructions
"""
from computer.data_types import Bits
from computer.instructions.logic import ANDReg, NOTReg, ORReg, XORReg
from computer.memory import SRAM
from computer.registers import Registers



# pylint: disable=C0116
def test_and(registers: Registers, sram: SRAM):
    sram.reset()
    registers.reset()

    d1 = Bits(1, 0, 1, 0, 1, 0, 1, 0)
    register_address1 = Bits(0, 0, 1)
    registers.write(register_address1, d1)

    d2 = Bits(1, 1, 1, 1, 0, 0, 0, 0)
    register_address2 = Bits(0, 1, 0)
    registers.write(register_address2, d2)

    registers.clock_tick(True)

    and_reg = ANDReg(registers, sram.size)
    operand = Bits(register_address1 + register_address2 + [0] * 8)
    and_reg(operand)
    registers.clock_tick(True)

    assert registers.read(register_address1) == [1, 0, 1, 0, 0, 0, 0, 0]

def test_or(registers: Registers, sram: SRAM):
    sram.reset()
    registers.reset()

    d1 = Bits(1, 0, 1, 0, 1, 0, 1, 0)
    register_address1 = Bits(0, 0, 1)
    registers.write(register_address1, d1)

    d2 = Bits(1, 1, 1, 1, 0, 0, 0, 0)
    register_address2 = Bits(0, 1, 0)
    registers.write(register_address2, d2)

    registers.clock_tick(True)

    and_reg = ORReg(registers, sram.size)
    operand = Bits(register_address1 + register_address2 + [0] * 8)
    and_reg(operand)
    registers.clock_tick(True)

    assert registers.read(register_address1) == [1, 1, 1, 1, 1, 0, 1, 0]

def test_xor(registers: Registers, sram: SRAM):
    sram.reset()
    registers.reset()

    d1 = Bits(1, 0, 1, 0, 1, 0, 1, 0)
    register_address1 = Bits(0, 0, 1)
    registers.write(register_address1, d1)

    d2 = Bits(1, 1, 1, 1, 0, 0, 0, 0)
    register_address2 = Bits(0, 1, 0)
    registers.write(register_address2, d2)

    registers.clock_tick(True)

    and_reg = XORReg(registers, sram.size)
    operand = Bits(register_address1 + register_address2 + [0] * 8)
    and_reg(operand)
    registers.clock_tick(True)

    assert registers.read(register_address1) == [0, 1, 0, 1, 1, 0, 1, 0]

def test_not(registers: Registers, sram: SRAM):
    sram.reset()
    registers.reset()

    d1 = Bits(1, 0, 1, 0, 1, 0, 1, 0)
    register_address1 = Bits(0, 0, 1)
    registers.write(register_address1, d1)
    registers.clock_tick(True)

    and_reg = NOTReg(registers, sram.size)
    operand = Bits(register_address1 + [0] * 3 + [0] * 8)
    and_reg(operand)
    registers.clock_tick(True)

    assert registers.read(register_address1) == [0, 1, 0, 1, 0, 1, 0, 1]
