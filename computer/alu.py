"""
Arithmetic logic unit (ALU) module
"""
from computer.data_types import Opcode8, Operand24
from computer.electronic.circuits.decoder import Decoder8To256


class ALU:
    """
    Arithmetic logic unit class
    """
    def __init__(self):
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

    def execute(self, opcode: Opcode8, operand: Operand24):
        """
        Execute the operation defined with the opcode and with operand as parameter
        """
        bits = self._decoder(*opcode, True)

        for i, bit in enumerate(bits[::-1]):
            if bit:
                self._operations[i](operand)
                break

    @staticmethod
    def _load_mem(operand: Operand24):
        pass

    @staticmethod
    def _load_imd(operand: Operand24):
        pass

    @staticmethod
    def _load_reg(operand: Operand24):
        pass

    @staticmethod
    def _store_mem(operand: Operand24):
        pass

    @staticmethod
    def _store_reg(operand: Operand24):
        pass

    @staticmethod
    def _jump(operand: Operand24):
        pass

    @staticmethod
    def _tran(operand: Operand24):
        pass

    @staticmethod
    def _and(operand: Operand24):
        pass

    @staticmethod
    def _or(operand: Operand24):
        pass

    @staticmethod
    def _xor(operand: Operand24):
        pass

    @staticmethod
    def _not(operand: Operand24):
        pass

    @staticmethod
    def _add(operand: Operand24):
        pass

    @staticmethod
    def _sub(operand: Operand24):
        pass

    @staticmethod
    def _mult(operand: Operand24):
        pass

    @staticmethod
    def _div(operand: Operand24):
        pass

    @staticmethod
    def _inc(operand: Operand24):
        pass

    @staticmethod
    def _dec(operand: Operand24):
        pass
