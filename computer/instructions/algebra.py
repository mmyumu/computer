"""
Algebra instructions module
"""
from computer.data_types import Bits
from computer.electronic.circuits.adder import FullAdder, HalfAdder
from computer.electronic.circuits.cmos import NOTGate
from computer.instructions.instruction import ALUInstruction
from computer.registers import Registers

# pylint: disable=R0903

class Add(ALUInstruction):
    """
    Add between 2 registers
    ADD REG REG	; REGA + REGB + CF, result stored in REGA
    """
    def __init__(self, registers: Registers, memory_size: int) -> None:
        super().__init__(registers, memory_size)
        self._adders = [FullAdder() for _ in range(2 ** self._registers.register_size)]

    def compute(self, reg1: Bits, reg2: Bits, value: Bits):
        data1 = self._registers.read(reg1)
        data2 = self._registers.read(reg2)

        carry_in = self._registers.cf
        data = []
        for bit1, bit2, adder in zip(data1[::-1], data2[::-1], self._adders):
            result_bit, carry_out = adder(bit1, bit2, carry_in)
            carry_in = carry_out
            data.append(result_bit)
        data = data[::-1]

        self._registers.cf = carry_out
        self._registers.write(reg1, data)


class Sub(ALUInstruction):
    """
    Sub between 2 registers
    SUB REG REG	; (REGA - REGB) - CF, result stored in REGA
    """
    def __init__(self, registers: Registers, memory_size: int) -> None:
        super().__init__(registers, memory_size)
        self._not_gates1 = [NOTGate() for _ in range(2 ** self._registers.register_size)]
        self._not_gates2 = [NOTGate() for _ in range(2 ** self._registers.register_size)]
        self._adders1 = [HalfAdder() for _ in range(2 ** self._registers.register_size)]
        self._adders2 = [FullAdder() for _ in range(2 ** self._registers.register_size)]
        self._adders3 = [HalfAdder() for _ in range(2 ** self._registers.register_size)]
        self._adders4 = [FullAdder() for _ in range(2 ** self._registers.register_size)]


        # self._not_gate = NOTGate()
        # self._adder = HalfAdder()

    def compute(self, reg1: Bits, reg2: Bits, value: Bits):
        data1 = self._registers.read(reg1)
        data2 = self._registers.read(reg2)

        not_data2 = []
        for bit2, not_gate in zip(data2, self._not_gates1):
            not_data2.append(not_gate(bit2))

        complement_data2 = []
        carry_in = True
        for bit2, adder in zip(not_data2[::-1], self._adders1):
            complement_bit, carry_out = adder(bit2, carry_in)
            carry_in = carry_out
            complement_data2.append(complement_bit)
        complement_data2 = complement_data2[::-1]

        sub_data = []
        carry_in = False
        for bit1, bit2, adder in zip(data1[::-1], complement_data2[::-1], self._adders2):
            result_bit, carry_out = adder(bit1, bit2, carry_in)
            carry_in = carry_out
            sub_data.append(result_bit)
        sub_data = sub_data[::-1]


        cf = [0] * 7 + [self._registers.cf]
        not_cf = []
        for bit2, not_gate in zip(cf, self._not_gates2):
            not_cf.append(not_gate(bit2))

        complement_cf = []
        carry_in = True
        for bit1, adder in zip(not_cf[::-1], self._adders3):
            result_bit, carry_out = adder(bit1, carry_in)
            complement_cf.append(result_bit)
            carry_in = carry_out
        complement_cf = complement_cf[::-1]

        # not_cf = self._not_gate(self._registers.cf)
        # complement_cf, carry_out = self._adder(not_cf, True)

        sub_data_cf = []
        carry_in = False
        for bit1, bit2, adder in zip(sub_data[::-1], complement_cf[::-1], self._adders4):
            result_bit, carry_out = adder(bit1, bit2, carry_in)
            carry_in = carry_out
            sub_data_cf.append(result_bit)
        sub_data_cf = sub_data_cf[::-1]

        self._registers.cf = False
        self._registers.write(reg1, sub_data_cf)
# class ORReg(BitwiseALUInstruction):
#     """
#     OR between 2 registers
#     OR REG REG		; REGA OR REGB, result stored in REGA
#     """
#     def _build_gates(self):
#         or_gates = []
#         for _ in range(2 ** self._registers.register_size):
#             or_gates.append(ORGate())
#         return or_gates


# class XORReg(BitwiseALUInstruction):
#     """
#     XOR between 2 registers
#     XOR REG REG	; REGA XOR REGB, result stored in REGA
#     """
#     def _build_gates(self):
#         xor_gates = []
#         for _ in range(2 ** self._registers.register_size):
#             xor_gates.append(XORGate())
#         return xor_gates

# class NOTReg(ALUInstruction):
#     """
#     NOT on register and store it
#     NOT REG 		; NOT REGA, result stored in REGA
#     """
#     def __init__(self, registers: Registers, memory_size: int) -> None:
#         super().__init__(registers, memory_size)
#         self._gates = []
#         for _ in range(2 ** self._registers.register_size):
#             self._gates.append(NOTGate())

#     def compute(self, reg1: Bits, reg2: Bits, value: Bits):
#         data1 = self._registers.read(reg1)

#         data = []
#         for bit1, gate in zip(data1, self._gates):
#             data.append(gate(bit1))

#         self._registers.write(reg1, data)
