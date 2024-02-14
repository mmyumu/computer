"""
Arithmetic logic unit (ALU) module
"""
from computer.data_types import Bits, Opcode8
from computer.electronic.circuits.decoder import Decoder8To256
from computer.instructions.logic import ANDReg
from computer.registers import Registers

# AND : Opération logique ET entre deux registres.
# OR : Opération logique OU entre deux registres.
# XOR : Opération logique OU exclusif entre deux registres.
# NOT : Inversion logique des bits d'un registre.
# ADD : Addition de deux registres.
# SUB : Soustraction de deux registres.
# MULT : Multiplication de deux registres.
# DIV : Division de deux registres.
# INC : Incrémentation d'un registre.
# DEC : Décrémentation d'un registre.

class ALU:
    """
    Arithmetic logic unit class
    """
    def __init__(self, registers: Registers, memory_size: int):
        self._decoder = Decoder8To256()
        self._operations = {
            8: ANDReg(registers, memory_size)
        }

    def execute(self, opcode: Opcode8, operand: Bits):
        """
        Execute the operation defined with the opcode and with operand as parameter
        """
        bits = self._decoder(*opcode, True)
        for i, bit in enumerate(bits[::-1]):
            if bit:
                self._operations[i](operand)
                break
