"""
Arithmetic logic unit (ALU) module
"""
from computer.data_types import Bits, Opcode8
from computer.electronic.circuits.decoder import Decoder8To256
from computer.instructions.load import LoadImd, LoadMem
from computer.instructions.nop import Nop
from computer.memory import SRAM
from computer.registers import Registers


class ALU:
    """
    Arithmetic logic unit class
    """
    def __init__(self, memory_size=16, registers_size=4, register_size=4):
        self._registers = Registers(size=registers_size, register_size=register_size)
        self._memory = SRAM(size=memory_size, register_size=register_size)
        self._decoder = Decoder8To256()
        self._operations = [
            Nop(),
            LoadMem(self._registers, self._memory),
            LoadImd(self._registers, self._memory),
            # LoadReg(registers),
            # StoreMem(registers, memory),
            # StoreReg(registers),
            # self._jump,
            # self._tran,
            # self._and,
            # self._or,
            # self._xor,
            # self._not,
            # self._add,
            # self._sub,
            # self._mult,
            # self._div,
            # self._inc,
            # self._dec
        ]
        # self._instructions = Instructions(self._registers, self._memory)

    def execute(self, opcode: Opcode8, operand: Bits):
        """
        Execute the operation defined with the opcode and with operand as parameter
        """
        operand_check_size = self._memory.size + (self._registers.size * 2)
        if len(operand) != operand_check_size:
            raise ValueError(f"Length of operand should be {operand_check_size} but is {len(operand)}")

        bits = self._decoder(*opcode, True)
        for i, bit in enumerate(bits[::-1]):
            if bit:
                self._operations[i](operand)
                break

    # def _load_mem(self, operand: Operand18):
    #     self._instructions.load_mem(operand)

    # def _load_imd(self, operand: Operand18):
    #     self._instructions.load_mem(operand)

    # def _load_reg(operand: Operand18):
    #     pass

    # @staticmethod
    # def _store_mem(operand: Operand18):
    #     pass

    # @staticmethod
    # def _store_reg(operand: Operand18):
    #     pass

    # @staticmethod
    # def _jump(operand: Operand18):
    #     pass

    # @staticmethod
    # def _tran(operand: Operand18):
    #     pass

    # @staticmethod
    # def _and(operand: Operand18):
    #     pass

    # @staticmethod
    # def _or(operand: Operand18):
    #     pass

    # @staticmethod
    # def _xor(operand: Operand18):
    #     pass

    # @staticmethod
    # def _not(operand: Operand18):
    #     pass

    # @staticmethod
    # def _add(operand: Operand18):
    #     pass

    # @staticmethod
    # def _sub(operand: Operand18):
    #     pass

    # @staticmethod
    # def _mult(operand: Operand18):
    #     pass

    # @staticmethod
    # def _div(operand: Operand18):
    #     pass

    # @staticmethod
    # def _inc(operand: Operand18):
    #     pass

    # @staticmethod
    # def _dec(operand: Operand18):
    #     pass
