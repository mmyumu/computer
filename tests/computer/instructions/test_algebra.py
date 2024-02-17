"""
Test for Logic instructions
"""
from computer.data_types import Bits, Data16
from computer.instructions.algebra import Add, Mult, Sub
from computer.memory import SRAM
from computer.registers import Registers



# pylint: disable=C0116
def test_add(registers: Registers, sram: SRAM):
    sram.reset()
    registers.reset()

    d1 = Data16(1, 0, 0, 0, 0, 0, 0, 1)
    register_address1 = Bits(0, 0, 1)
    registers.write(register_address1, d1)

    d2 = Data16(0, 0, 0, 0, 0, 1, 1, 1)
    register_address2 = Bits(0, 1, 0)
    registers.write(register_address2, d2)

    registers.clock_tick(True)

    and_reg = Add(registers, sram.size)
    operand = Bits(register_address1 + register_address2 + [0] * 8)
    and_reg(operand)
    registers.clock_tick(True)

    assert registers.read(register_address1) == tuple((1, 0, 0, 0, 1, 0, 0, 0))
    assert registers.cf is False


def test_add_carry_in(registers: Registers, sram: SRAM):
    sram.reset()
    registers.reset()

    d1 = Data16(1, 0, 0, 0, 0, 0, 0, 1)
    register_address1 = Bits(0, 0, 1)
    registers.write(register_address1, d1)

    d2 = Data16(0, 0, 0, 0, 0, 1, 1, 1)
    register_address2 = Bits(0, 1, 0)
    registers.write(register_address2, d2)

    registers.cf = 1

    registers.clock_tick(True)

    and_reg = Add(registers, sram.size)
    operand = Bits(register_address1 + register_address2 + [0] * 8)
    and_reg(operand)
    registers.clock_tick(True)

    assert registers.read(register_address1) == tuple((1, 0, 0, 0, 1, 0, 0, 1))
    assert registers.cf is False


def test_add_overflow(registers: Registers, sram: SRAM):
    sram.reset()
    registers.reset()

    d1 = Data16(1, 0, 0, 0, 0, 0, 0, 1)
    register_address1 = Bits(0, 0, 1)
    registers.write(register_address1, d1)

    d2 = Data16(1, 0, 0, 0, 0, 0, 1, 1)
    register_address2 = Bits(0, 1, 0)
    registers.write(register_address2, d2)

    registers.clock_tick(True)

    add = Add(registers, sram.size)
    operand = Bits(register_address1 + register_address2 + [0] * 8)
    add(operand)
    registers.clock_tick(True)

    assert registers.read(register_address1) == tuple((0, 0, 0, 0, 0, 1, 0, 0))
    assert registers.cf is True

def test_sub_easy(registers: Registers, sram: SRAM):
    """
    An easy one so I can debug it with my weak brain    
    """
    sram.reset()
    registers.reset()

    d1 = Data16(0, 0, 0, 0, 0, 0, 1, 1)
    register_address1 = Bits(0, 0, 1)
    registers.write(register_address1, d1)

    d2 = Data16(0, 0, 0, 0, 0, 0, 0, 1)
    register_address2 = Bits(0, 1, 0)
    registers.write(register_address2, d2)

    registers.clock_tick(True)

    sub = Sub(registers, sram.size)
    operand = Bits(register_address1 + register_address2 + [0] * 8)
    sub(operand)
    registers.clock_tick(True)

    assert registers.read(register_address1) == tuple((0, 0, 0, 0, 0, 0, 1, 0))
    assert registers.cf is False


def test_sub(registers: Registers, sram: SRAM):
    sram.reset()
    registers.reset()

    d1 = Data16(1, 0, 0, 1, 1, 0, 0, 0)
    register_address1 = Bits(0, 0, 1)
    registers.write(register_address1, d1)

    d2 = Data16(1, 0, 0, 1, 0, 0, 1, 0)
    register_address2 = Bits(0, 1, 0)
    registers.write(register_address2, d2)

    registers.clock_tick(True)

    sub = Sub(registers, sram.size)
    operand = Bits(register_address1 + register_address2 + [0] * 8)
    sub(operand)
    registers.clock_tick(True)

    assert registers.read(register_address1) == tuple((0, 0, 0, 0, 0, 1, 1, 0))
    assert registers.cf is False


def test_sub_cf(registers: Registers, sram: SRAM):
    sram.reset()
    registers.reset()

    d1 = Data16(1, 0, 0, 1, 1, 0, 0, 0)
    register_address1 = Bits(0, 0, 1)
    registers.write(register_address1, d1)

    d2 = Data16(1, 0, 0, 1, 0, 0, 1, 0)
    register_address2 = Bits(0, 1, 0)
    registers.write(register_address2, d2)

    registers.cf = 1

    registers.clock_tick(True)

    sub = Sub(registers, sram.size)
    operand = Bits(register_address1 + register_address2 + [0] * 8)
    sub(operand)
    registers.clock_tick(True)

    assert registers.read(register_address1) == tuple((0, 0, 0, 0, 0, 1, 0, 1))
    assert registers.cf is False


def test_mult_easy(registers: Registers, sram: SRAM):
    sram.reset()
    registers.reset()

    d1 = Data16(0, 0, 0, 0, 1, 1, 1, 1)
    register_address1 = Bits(0, 0, 1)
    registers.write(register_address1, d1)

    d2 = Data16(0, 0, 0, 0, 0, 0, 1, 0)
    register_address2 = Bits(0, 1, 0)
    registers.write(register_address2, d2)

    registers.clock_tick(True)

    mult = Mult(registers, sram.size)
    operand = Bits(register_address1 + register_address2 + [0] * 8)
    mult(operand)
    registers.clock_tick(True)

    assert registers.read(register_address1) == tuple((0, 0, 0, 1, 1, 1, 1, 0))
    assert registers.read(register_address2) == tuple((0, 0, 0, 0, 0, 0, 0, 0))
    assert registers.cf is False


def test_mult(registers: Registers, sram: SRAM):
    sram.reset()
    registers.reset()

    d1 = Data16(1, 0, 0, 0, 1, 1, 1, 1)
    register_address1 = Bits(0, 0, 1)
    registers.write(register_address1, d1)

    d2 = Data16(1, 0, 0, 1, 0, 0, 1, 0)
    register_address2 = Bits(0, 1, 0)
    registers.write(register_address2, d2)

    registers.clock_tick(True)

    mult = Mult(registers, sram.size)
    operand = Bits(register_address1 + register_address2 + [0] * 8)
    mult(operand)
    registers.clock_tick(True)

    assert registers.read(register_address1) == tuple((1, 0, 0, 0, 1, 1, 1, 0))
    assert registers.read(register_address2) == tuple((0, 1, 0, 1, 0, 0, 0, 1))
    assert registers.cf is False
