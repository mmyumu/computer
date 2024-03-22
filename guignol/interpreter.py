from typing import Any
from lark import Lark, Transformer

from computer.data_types import Bits
from computer.program import BinaryProgram

# Nop(),
# Jump(registers=self._registers, memory=self._memory, program_counter=self._program_counter),
# JEQ(registers=self._registers, memory=self._memory, program_counter=self._program_counter),
# JLT(registers=self._registers, memory=self._memory, program_counter=self._program_counter),
# JGE(registers=self._registers, memory=self._memory, program_counter=self._program_counter),
# LoadMem(registers=self._registers, memory=self._memory, program_counter=self._program_counter),
# LoadImd(registers=self._registers, memory=self._memory, program_counter=self._program_counter),
# LoadReg(registers=self._registers, memory=self._memory, program_counter=self._program_counter),
# StoreMem(registers=self._registers, memory=self._memory, program_counter=self._program_counter),
# StoreReg(registers=self._registers, memory=self._memory, program_counter=self._program_counter),
# Tran(registers=self._registers, memory=self._memory, program_counter=self._program_counter),
# CLC(registers=self._registers, memory=self._memory, program_counter=self._program_counter),
# STC(registers=self._registers, memory=self._memory, program_counter=self._program_counter),


# Add(registers, memory_register_size),
# Sub(registers, memory_register_size),
# Mult(registers, memory_register_size),
# Div(registers, memory_register_size),
# Inc(registers, memory_register_size),
# Dec(registers, memory_register_size),
# ANDReg(registers, memory_register_size),
# ORReg(registers, memory_register_size),
# XORReg(registers, memory_register_size),
# NOTReg(registers, memory_register_size),
# ROL(registers, memory_register_size),
# ROR(registers, memory_register_size),
# Cmp(registers, memory_register_size)

# Définir la grammaire de votre langage en EBNF
# grammar = """

# """

#pylint: disable=C0116
class InstructionToBinary(Transformer):
    """
    Transform GUIGNOL instructions to Binary instructions
    """
    def __init__(self, register_size: int, visit_tokens: bool = True) -> None:
        super().__init__(visit_tokens)
        self._register_size = register_size

    def _forge_instruction(self, opcode: int, reg1: int, reg2: int, value: int):
        opcode = Bits(opcode, size=8)
        reg1 = Bits(reg1, size=self._register_size)
        reg2 = Bits(reg2, size=self._register_size)
        value = Bits(value, size=2 ** self._register_size)
        return Bits(opcode + reg1 + reg2 + value)

    def nop(self, _):
        return self._forge_instruction(0, 0, 0, 0)

    def jmp(self, args):
        address = int(args[0].value[1:])
        return self._forge_instruction(1, 0, 0, address)

    def jeq(self, args):
        address = int(args[0].value[1:])
        return self._forge_instruction(2, 0, 0, address)

    def jlt(self, args):
        address = int(args[0].value[1:])
        return self._forge_instruction(3, 0, 0, address)

    def jge(self, args):
        address = int(args[0].value[1:])
        return self._forge_instruction(4, 0, 0, address)

    def load_mem(self, args):
        reg1 = args[0]
        address = int(args[1].value[1:])
        return self._forge_instruction(5, reg1, 0, address)

    def load_imd(self, args):
        reg1 = args[0]
        value = int(args[1].value)
        return self._forge_instruction(6, reg1, 0, value)

    def load_reg(self, args):
        reg1 = args[0]
        reg2 = args[1]
        return self._forge_instruction(7, reg1, reg2, 0)

    def store_mem(self, args):
        reg1 = args[0]
        address = int(args[1].value[1:])
        return self._forge_instruction(8, reg1, 0, address)

    def store_reg(self, args):
        reg1 = args[0]
        reg2 = args[1]
        return self._forge_instruction(9, reg1, reg2, 0)

    def tran_reg(self, args):
        reg1 = args[0]
        reg2 = args[1]
        return self._forge_instruction(10, reg1, reg2, 0)

    def clc(self, _):
        return self._forge_instruction(11, 0, 0, 0)

    def stc(self, _):
        return self._forge_instruction(12, 0, 0, 0)

    def add(self, args):
        reg1 = args[0]
        reg2 = args[1]
        return self._forge_instruction(128, reg1, reg2, 0)

    def sub(self, args):
        reg1 = args[0]
        reg2 = args[1]
        return self._forge_instruction(129, reg1, reg2, 0)

    def mult(self, args):
        reg1 = args[0]
        reg2 = args[1]
        return self._forge_instruction(130, reg1, reg2, 0)

    def div(self, args):
        reg1 = args[0]
        reg2 = args[1]
        return self._forge_instruction(131, reg1, reg2, 0)

    def inc(self, args):
        reg1 = args[0]
        return self._forge_instruction(132, reg1, 0, 0)

    def dec(self, args):
        reg1 = args[0]
        return self._forge_instruction(133, reg1, 0, 0)

    def and_reg(self, args):
        reg1 = args[0]
        reg2 = args[1]
        return self._forge_instruction(134, reg1, reg2, 0)

    def or_reg(self, args):
        reg1 = args[0]
        reg2 = args[1]
        return self._forge_instruction(135, reg1, reg2, 0)

    def xor(self, args):
        reg1 = args[0]
        reg2 = args[1]
        return self._forge_instruction(136, reg1, reg2, 0)

    def not_reg(self, args):
        reg1 = args[0]
        return self._forge_instruction(137, reg1, 0, 0)

    def rol(self, args):
        reg1 = args[0]
        value = int(args[1].value)
        return self._forge_instruction(138, reg1, 0, value)

    def ror(self, args):
        reg1 = args[0]
        value = int(args[1].value)
        return self._forge_instruction(139, reg1, 0, value)

    def cmp(self, args):
        reg1 = args[0]
        reg2 = args[1]
        return self._forge_instruction(140, reg1, reg2, 0)

    def register(self, args):
        return int(args[0].value)


class Interpreter:
    """
    Interpreter class to parse GUIGNOL program
    """
    def __init__(self, grammar: str, register_size: int = 4) -> None:
        self._parser = Lark.open(grammar, rel_to=__file__, parser="lalr", transformer=InstructionToBinary(register_size))

    def __call__(self, program: str) -> BinaryProgram:
        parsed_instructions = self._parser.parse(program)
        program = BinaryProgram()

        for parsed_instruction in parsed_instructions.children:
            program.append(parsed_instruction)
        return program








    # Ajouter les méthodes pour les autres instructions...

# Créer le parseur avec la grammaire
# parser = Lark(grammar, parser='lalr', transformer=InstructionToBinary())

# # Le programme à parser
# program = """

# """

# Parser le programme
# parsed_program = parser.parse(program)

# Imprimer les instructions en binaires
# print("\n".join(parsed_program))
