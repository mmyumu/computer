"""
Algebra instructions module
"""
from computer.data_types import Bits
from computer.electronic.circuits.bitwise import BitwiseAdd, BitwiseDiv, BitwiseMult, BitwiseSub
from computer.electronic.circuits.cmos import ORGate
from computer.instructions.instruction import ALUInstruction
from computer.registers import Registers

# pylint: disable=R0903

class Add(ALUInstruction):
    """
    Add between 2 registers
    ADD REG REG	; REGA + REGB + CF, result stored in REGA
    """
    def __init__(self, registers: Registers, memory_register_size: int) -> None:
        super().__init__(registers, memory_register_size)
        self._adder = BitwiseAdd(2 ** self._registers.register_size)

    def compute(self, reg1: Bits, reg2: Bits, value: Bits):
        data1 = self._registers.read(reg1)
        data2 = self._registers.read(reg2)

        data, carry_out = self._adder(data1, data2, carry=self._registers.cf)

        self._registers.cf = carry_out
        self._registers.write(reg1, data)

        self.update_zf(data)


class Sub(ALUInstruction):
    """
    Sub between 2 registers
    SUB REG REG	; (REGA - REGB) - CF, result stored in REGA
    """
    def __init__(self, registers: Registers, memory_register_size: int) -> None:
        super().__init__(registers, memory_register_size)
        self._sub1 = BitwiseSub(2 ** self._registers.size)
        self._sub2 = BitwiseSub(2 ** self._registers.size)

    def compute(self, reg1: Bits, reg2: Bits, value: Bits):
        data1 = self._registers.read(reg1)
        data2 = self._registers.read(reg2)

        sub1, borrow_out = self._sub1(data1, data2, False)

        number_of_bits_to_fill = (2 ** self._registers_size) - 1
        cf = [0] * number_of_bits_to_fill + [self._registers.cf]
        sub2, _ = self._sub2(sub1, cf, False)

        self._registers.cf = borrow_out
        self._registers.write(reg1, sub2)

        self.update_zf(sub2)


class Mult(ALUInstruction):
    """
    Multiply 2 registers
    MULT REG REG	; REGA * REGB, low 16-bit result stored in REGA, high 16-bit result stored in REGB
    """
    def __init__(self, registers: Registers, memory_register_size: int) -> None:
        super().__init__(registers, memory_register_size)
        self._mult = BitwiseMult(2 ** self._registers.size)
        self._zf_or_gates = [ORGate() for _ in range(2 ** (self._registers.size + 1))]

    def compute(self, reg1: Bits, reg2: Bits, value: Bits):
        data1 = self._registers.read(reg1)
        data2 = self._registers.read(reg2)

        mult = self._mult(data1, data2)

        self._registers.write(reg1, mult[2 ** self._registers.size:])
        self._registers.write(reg2, mult[:2 ** self._registers.size])

        self.update_zf(mult)


class Div(ALUInstruction):
    """
    Divide 2 registers
    DIV REG REG	; REGA / REGB result stored in REGA, REGA MOD REGB stored in REGB
    """
    def __init__(self, registers: Registers, memory_register_size: int) -> None:
        super().__init__(registers, memory_register_size)
        self._div = BitwiseDiv(2 ** self._registers.size)

    def compute(self, reg1: Bits, reg2: Bits, value: Bits):
        data1 = self._registers.read(reg1)
        data2 = self._registers.read(reg2)

        quotient, remainder = self._div(data1, data2)

        self._registers.write(reg1, quotient)
        self._registers.write(reg2, remainder)

        self.update_zf(quotient + remainder)


class Inc(ALUInstruction):
    """
    Increment register
    INC REG	; REGA++, CF not affected
    """
    def __init__(self, registers: Registers, memory_register_size: int) -> None:
        super().__init__(registers, memory_register_size)
        self._adder = BitwiseAdd(2 ** self._registers.size)

    def compute(self, reg1: Bits, reg2: Bits, value: Bits):
        data1 = self._registers.read(reg1)

        inc_data, _ = self._adder(data1, [0] * len(data1), carry=True)

        self._registers.write(reg1, inc_data)

        self.update_zf(inc_data)


class Dec(ALUInstruction):
    """
    Decrement register
    DEC REG	; REGA--, CF not affected
    """
    def __init__(self, registers: Registers, memory_register_size: int) -> None:
        super().__init__(registers, memory_register_size)
        self._subtractor = BitwiseSub(2 ** self._registers.size)

    def compute(self, reg1: Bits, reg2: Bits, value: Bits):
        data1 = self._registers.read(reg1)

        dec_data, _ = self._subtractor(data1, [0] * len(data1), True)

        self._registers.write(reg1, dec_data)

        self.update_zf(dec_data)


class Cmp(ALUInstruction):
    """
    Comparison between 2 registers
    CMP REG REG	; (REGA - REGB), only flags are changed
    """
    def __init__(self, registers: Registers, memory_register_size: int) -> None:
        super().__init__(registers, memory_register_size)
        self._sub1 = BitwiseSub(2 ** self._registers.size)
        self._sub2 = BitwiseSub(2 ** self._registers.size)

    def compute(self, reg1: Bits, reg2: Bits, value: Bits):
        data1 = self._registers.read(reg1)
        data2 = self._registers.read(reg2)

        sub1, borrow_out = self._sub1(data1, data2, False)

        self._registers.cf = borrow_out
        self.update_zf(sub1)
