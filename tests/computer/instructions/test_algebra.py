"""
Test for Logic instructions
"""
from computer.data_types import Bits
from computer.instructions.algebra import Add, Cmp, Dec, Div, Inc, Mult, Sub
from computer.memory import SRAM
from computer.registers import Registers



# pylint: disable=C0116,R0801
def test_add(registers: Registers, sram: SRAM):
    sram.reset()
    registers.reset()

    d1 = Bits(1, 0, 0, 0, 0, 0, 0, 1)
    register_address1 = Bits(0, 0, 1)
    registers.write(register_address1, d1)

    d2 = Bits(0, 0, 0, 0, 0, 1, 1, 1)
    register_address2 = Bits(0, 1, 0)
    registers.write(register_address2, d2)

    registers.clock_tick(True)

    add = Add(registers, sram.register_size)
    operand = Bits(register_address1 + register_address2 + [0] * 8)
    add(operand)
    registers.clock_tick(True)

    assert registers.read(register_address1) == [1, 0, 0, 0, 1, 0, 0, 0]
    assert registers.cf is False
    assert registers.zf is False


def test_add_carry_in(registers: Registers, sram: SRAM):
    sram.reset()
    registers.reset()

    d1 = Bits(1, 0, 0, 0, 0, 0, 0, 1)
    register_address1 = Bits(0, 0, 1)
    registers.write(register_address1, d1)

    d2 = Bits(0, 0, 0, 0, 0, 1, 1, 1)
    register_address2 = Bits(0, 1, 0)
    registers.write(register_address2, d2)

    registers.cf = 1

    registers.clock_tick(True)

    add = Add(registers, sram.register_size)
    operand = Bits(register_address1 + register_address2 + [0] * 8)
    add(operand)
    registers.clock_tick(True)

    assert registers.read(register_address1) == [1, 0, 0, 0, 1, 0, 0, 1]
    assert registers.cf is False
    assert registers.zf is False


def test_add_overflow(registers: Registers, sram: SRAM):
    sram.reset()
    registers.reset()

    d1 = Bits(1, 0, 0, 0, 0, 0, 0, 1)
    register_address1 = Bits(0, 0, 1)
    registers.write(register_address1, d1)

    d2 = Bits(1, 0, 0, 0, 0, 0, 1, 1)
    register_address2 = Bits(0, 1, 0)
    registers.write(register_address2, d2)

    registers.clock_tick(True)

    add = Add(registers, sram.register_size)
    operand = Bits(register_address1 + register_address2 + [0] * 8)
    add(operand)
    registers.clock_tick(True)

    assert registers.read(register_address1) == [0, 0, 0, 0, 0, 1, 0, 0]
    assert registers.cf is True
    assert registers.zf is False


def test_add_zf(registers: Registers, sram: SRAM):
    sram.reset()
    registers.reset()

    d1 = Bits(1, 1, 1, 1, 1, 1, 1, 1)
    register_address1 = Bits(0, 0, 1)
    registers.write(register_address1, d1)

    d2 = Bits(0, 0, 0, 0, 0, 0, 0, 1)
    register_address2 = Bits(0, 1, 0)
    registers.write(register_address2, d2)

    registers.cf = 0

    registers.clock_tick(True)

    add = Add(registers, sram.register_size)
    operand = Bits(register_address1 + register_address2 + [0] * 8)
    add(operand)
    registers.clock_tick(True)

    assert registers.read(register_address1) == [0, 0, 0, 0, 0, 0, 0, 0]
    assert registers.cf is True
    assert registers.zf is True


def test_sub_easy(registers: Registers, sram: SRAM):
    """
    An easy one so I can debug it with my weak brain    
    """
    sram.reset()
    registers.reset()

    d1 = Bits(0, 0, 0, 0, 0, 0, 1, 1)
    register_address1 = Bits(0, 0, 1)
    registers.write(register_address1, d1)

    d2 = Bits(0, 0, 0, 0, 0, 0, 0, 1)
    register_address2 = Bits(0, 1, 0)
    registers.write(register_address2, d2)

    registers.clock_tick(True)

    sub = Sub(registers, sram.register_size)
    operand = Bits(register_address1 + register_address2 + [0] * 8)
    sub(operand)
    registers.clock_tick(True)

    assert registers.read(register_address1) == [0, 0, 0, 0, 0, 0, 1, 0]
    assert registers.cf is False
    assert registers.zf is False


def test_sub(registers: Registers, sram: SRAM):
    sram.reset()
    registers.reset()

    d1 = Bits(1, 0, 0, 1, 1, 0, 0, 0)
    register_address1 = Bits(0, 0, 1)
    registers.write(register_address1, d1)

    d2 = Bits(1, 0, 0, 1, 0, 0, 1, 0)
    register_address2 = Bits(0, 1, 0)
    registers.write(register_address2, d2)

    registers.clock_tick(True)

    sub = Sub(registers, sram.register_size)
    operand = Bits(register_address1 + register_address2 + [0] * 8)
    sub(operand)
    registers.clock_tick(True)

    assert registers.read(register_address1) == [0, 0, 0, 0, 0, 1, 1, 0]
    assert registers.cf is False
    assert registers.zf is False


def test_sub_cf(registers: Registers, sram: SRAM):
    sram.reset()
    registers.reset()

    d1 = Bits(1, 0, 0, 1, 1, 0, 0, 0)
    register_address1 = Bits(0, 0, 1)
    registers.write(register_address1, d1)

    d2 = Bits(1, 0, 0, 1, 0, 0, 1, 0)
    register_address2 = Bits(0, 1, 0)
    registers.write(register_address2, d2)

    registers.cf = 1

    registers.clock_tick(True)

    sub = Sub(registers, sram.register_size)
    operand = Bits(register_address1 + register_address2 + [0] * 8)
    sub(operand)
    registers.clock_tick(True)

    assert registers.read(register_address1) == [0, 0, 0, 0, 0, 1, 0, 1]
    assert registers.cf is False
    assert registers.zf is False


def test_sub_borrow_out(registers: Registers, sram: SRAM):
    sram.reset()
    registers.reset()

    d1 = Bits(0, 0, 0, 0, 1, 0, 1, 0)
    register_address1 = Bits(0, 0, 1)
    registers.write(register_address1, d1)

    d2 = Bits(0, 0, 0, 1, 0, 0, 0, 0)
    register_address2 = Bits(0, 1, 0)
    registers.write(register_address2, d2)

    registers.clock_tick(True)

    sub = Sub(registers, sram.register_size)
    operand = Bits(register_address1 + register_address2 + [0] * 8)
    sub(operand)
    registers.clock_tick(True)

    assert registers.read(register_address1) == [1, 1, 1, 1, 1, 0, 1, 0]
    assert registers.cf is True
    assert registers.zf is False


def test_sub_zf(registers: Registers, sram: SRAM):
    sram.reset()
    registers.reset()

    d1 = Bits(0, 0, 0, 0, 1, 0, 1, 0)
    register_address1 = Bits(0, 0, 1)
    registers.write(register_address1, d1)

    d2 = Bits(0, 0, 0, 0, 1, 0, 1, 0)
    register_address2 = Bits(0, 1, 0)
    registers.write(register_address2, d2)

    registers.clock_tick(True)

    sub = Sub(registers, sram.register_size)
    operand = Bits(register_address1 + register_address2 + [0] * 8)
    sub(operand)
    registers.clock_tick(True)

    assert registers.read(register_address1) == [0, 0, 0, 0, 0, 0, 0, 0]
    assert registers.cf is False
    assert registers.zf is True


def test_mult_easy(registers: Registers, sram: SRAM):
    sram.reset()
    registers.reset()

    d1 = Bits(0, 0, 0, 0, 1, 1, 1, 1)
    register_address1 = Bits(0, 0, 1)
    registers.write(register_address1, d1)

    d2 = Bits(0, 0, 0, 0, 0, 0, 1, 0)
    register_address2 = Bits(0, 1, 0)
    registers.write(register_address2, d2)

    registers.clock_tick(True)

    mult = Mult(registers, sram.register_size)
    operand = Bits(register_address1 + register_address2 + [0] * 8)
    mult(operand)
    registers.clock_tick(True)

    assert registers.read(register_address1) == [0, 0, 0, 1, 1, 1, 1, 0]
    assert registers.read(register_address2) == [0, 0, 0, 0, 0, 0, 0, 0]
    assert registers.cf is False
    assert registers.zf is False


def test_mult(registers: Registers, sram: SRAM):
    sram.reset()
    registers.reset()

    d1 = Bits(1, 0, 0, 0, 1, 1, 1, 1)
    register_address1 = Bits(0, 0, 1)
    registers.write(register_address1, d1)

    d2 = Bits(1, 0, 0, 1, 0, 0, 1, 0)
    register_address2 = Bits(0, 1, 0)
    registers.write(register_address2, d2)

    registers.clock_tick(True)

    mult = Mult(registers, sram.register_size)
    operand = Bits(register_address1 + register_address2 + [0] * 8)
    mult(operand)
    registers.clock_tick(True)

    assert registers.read(register_address1) == [1, 0, 0, 0, 1, 1, 1, 0]
    assert registers.read(register_address2) == [0, 1, 0, 1, 0, 0, 0, 1]
    assert registers.cf is False
    assert registers.zf is False


def test_mult_zf(registers: Registers, sram: SRAM):
    sram.reset()
    registers.reset()

    d1 = Bits(0, 0, 0, 0, 1, 1, 1, 1)
    register_address1 = Bits(0, 0, 1)
    registers.write(register_address1, d1)

    d2 = Bits(0, 0, 0, 0, 0, 0, 0, 0)
    register_address2 = Bits(0, 1, 0)
    registers.write(register_address2, d2)

    registers.clock_tick(True)

    mult = Mult(registers, sram.register_size)
    operand = Bits(register_address1 + register_address2 + [0] * 8)
    mult(operand)
    registers.clock_tick(True)

    assert registers.read(register_address1) == [0, 0, 0, 0, 0, 0, 0, 0]
    assert registers.read(register_address2) == [0, 0, 0, 0, 0, 0, 0, 0]
    assert registers.cf is False
    assert registers.zf is True


def test_div(registers: Registers, sram: SRAM):
    sram.reset()
    registers.reset()

    d1 = Bits(0, 0, 1, 1, 1, 1, 1, 1)
    register_address1 = Bits(0, 0, 1)
    registers.write(register_address1, d1)

    d2 = Bits(0, 0, 0, 0, 0, 1, 1, 0)
    register_address2 = Bits(0, 1, 0)
    registers.write(register_address2, d2)

    registers.clock_tick(True)

    div = Div(registers, sram.register_size)
    operand = Bits(register_address1 + register_address2 + [0] * 8)
    div(operand)
    registers.clock_tick(True)

    assert registers.read(register_address1) == [0, 0, 0, 0, 1, 0, 1, 0]
    assert registers.read(register_address2) == [0, 0, 0, 0, 0, 0, 1, 1]
    assert registers.cf is False
    assert registers.zf is False


def test_div_zf(registers: Registers, sram: SRAM):
    sram.reset()
    registers.reset()

    d1 = Bits(0, 0, 0, 0, 0, 0, 0, 0)
    register_address1 = Bits(0, 0, 1)
    registers.write(register_address1, d1)

    d2 = Bits(0, 0, 0, 0, 0, 1, 1, 0)
    register_address2 = Bits(0, 1, 0)
    registers.write(register_address2, d2)

    registers.clock_tick(True)

    div = Div(registers, sram.register_size)
    operand = Bits(register_address1 + register_address2 + [0] * 8)
    div(operand)
    registers.clock_tick(True)

    assert registers.read(register_address1) == [0, 0, 0, 0, 0, 0, 0, 0]
    assert registers.read(register_address2) == [0, 0, 0, 0, 0, 0, 0, 0]
    assert registers.cf is False
    assert registers.zf is True


def test_inc(registers: Registers, sram: SRAM):
    sram.reset()
    registers.reset()

    d1 = Bits(0, 0, 1, 1, 1, 1, 1, 1)
    register_address1 = Bits(0, 0, 1)
    registers.write(register_address1, d1)

    registers.clock_tick(True)

    inc = Inc(registers, sram.register_size)
    operand = Bits(register_address1 + [0] * 3 + [0] * 8)
    inc(operand)
    registers.clock_tick(True)

    assert registers.read(register_address1) == [0, 1, 0, 0, 0, 0, 0, 0]
    assert registers.cf is False
    assert registers.zf is False


def test_inc_zf(registers: Registers, sram: SRAM):
    sram.reset()
    registers.reset()

    d1 = Bits(1, 1, 1, 1, 1, 1, 1, 1)
    register_address1 = Bits(0, 0, 1)
    registers.write(register_address1, d1)

    registers.clock_tick(True)

    inc = Inc(registers, sram.register_size)
    operand = Bits(register_address1 + [0] * 3 + [0] * 8)
    inc(operand)
    registers.clock_tick(True)

    assert registers.read(register_address1) == [0, 0, 0, 0, 0, 0, 0, 0]
    assert registers.cf is False
    assert registers.zf is True


def test_dec(registers: Registers, sram: SRAM):
    sram.reset()
    registers.reset()

    d1 = Bits(0, 0, 1, 1, 1, 1, 1, 1)
    register_address1 = Bits(0, 0, 1)
    registers.write(register_address1, d1)

    registers.clock_tick(True)

    dec = Dec(registers, sram.register_size)
    operand = Bits(register_address1 + [0] * 3 + [0] * 8)
    dec(operand)
    registers.clock_tick(True)

    assert registers.read(register_address1) == [0, 0, 1, 1, 1, 1, 1, 0]
    assert registers.cf is False
    assert registers.zf is False


def test_dec_zf(registers: Registers, sram: SRAM):
    sram.reset()
    registers.reset()

    d1 = Bits(0, 0, 0, 0, 0, 0, 0, 1)
    register_address1 = Bits(0, 0, 1)
    registers.write(register_address1, d1)

    registers.clock_tick(True)

    dec = Dec(registers, sram.register_size)
    operand = Bits(register_address1 + [0] * 3 + [0] * 8)
    dec(operand)
    registers.clock_tick(True)

    assert registers.read(register_address1) == [0, 0, 0, 0, 0, 0, 0, 0]
    assert registers.cf is False
    assert registers.zf is True


def test_cmp_false(registers: Registers, sram: SRAM):
    sram.reset()
    registers.reset()

    d1 = Bits(1, 0, 0, 1, 1, 0, 0, 0)
    register_address1 = Bits(0, 0, 1)
    registers.write(register_address1, d1)

    d2 = Bits(1, 0, 0, 1, 0, 0, 1, 0)
    register_address2 = Bits(0, 1, 0)
    registers.write(register_address2, d2)

    registers.clock_tick(True)

    cmp = Cmp(registers, sram.register_size)
    operand = Bits(register_address1 + register_address2 + [0] * 8)
    cmp(operand)
    registers.clock_tick(True)

    assert registers.read(register_address1) == d1
    assert registers.read(register_address2) == d2
    assert registers.cf is False
    assert registers.zf is False

def test_cmp_true(registers: Registers, sram: SRAM):
    sram.reset()
    registers.reset()

    d1 = Bits(1, 0, 0, 1, 1, 0, 0, 0)
    register_address1 = Bits(0, 0, 1)
    registers.write(register_address1, d1)

    d2 = Bits(1, 0, 0, 1, 1, 0, 0, 0)
    register_address2 = Bits(0, 1, 0)
    registers.write(register_address2, d2)

    registers.clock_tick(True)

    cmp = Cmp(registers, sram.register_size)
    operand = Bits(register_address1 + register_address2 + [0] * 8)
    cmp(operand)
    registers.clock_tick(True)

    assert registers.read(register_address1) == d1
    assert registers.read(register_address2) == d2
    assert registers.cf is False
    assert registers.zf is True
