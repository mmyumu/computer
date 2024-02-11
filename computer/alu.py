"""
Arithmetic logic unit (ALU) module
"""
from computer.data_types import Opcode8, Operand18
from computer.electronic.circuits.decoder import Decoder8To256
from computer.memory import SRAM
from computer.registers import Registers


class ALU:
    """
    Arithmetic logic unit class
    """
    def __init__(self):
        self._registers = Registers()
        self._memory = SRAM(size=8)
        self._decoder = Decoder8To256()
        self._operations = [
            self._load_mem,
            self._load_imd,
            self._load_reg,
            self._store_mem,
            self._store_reg,
            self._jump,
            self._tran,
            self._and,
            self._or,
            self._xor,
            self._not,
            self._add,
            self._sub,
            self._mult,
            self._div,
            self._inc,
            self._dec
        ]

    def execute(self, opcode: Opcode8, operand: Operand18):
        """
        Execute the operation defined with the opcode and with operand as parameter
        """
        bits = self._decoder(*opcode, True)

        for i, bit in enumerate(bits[::-1]):
            if bit:
                self._operations[i](operand)
                break

    @staticmethod
    def _load_mem(operand: Operand18):
        pass

    @staticmethod
    def _load_imd(operand: Operand18):
        pass

    @staticmethod
    def _load_reg(operand: Operand18):
        pass

    @staticmethod
    def _store_mem(operand: Operand18):
        pass

    @staticmethod
    def _store_reg(operand: Operand18):
        pass

    @staticmethod
    def _jump(operand: Operand18):
        pass

    @staticmethod
    def _tran(operand: Operand18):
        pass

    @staticmethod
    def _and(operand: Operand18):
        pass

    @staticmethod
    def _or(operand: Operand18):
        pass

    @staticmethod
    def _xor(operand: Operand18):
        pass

    @staticmethod
    def _not(operand: Operand18):
        pass

    @staticmethod
    def _add(operand: Operand18):
        pass

    @staticmethod
    def _sub(operand: Operand18):
        pass

    @staticmethod
    def _mult(operand: Operand18):
        pass

    @staticmethod
    def _div(operand: Operand18):
        pass

    @staticmethod
    def _inc(operand: Operand18):
        pass

    @staticmethod
    def _dec(operand: Operand18):
        pass
