"""
Control unit module
"""
from computer.data_types import Bits, Opcode8
from computer.electronic.circuits.decoder import Decoder8To256
from computer.instructions.jump import Jump
from computer.instructions.load import LoadImd, LoadMem, LoadReg
from computer.instructions.nop import Nop
from computer.instructions.store import StoreMem, StoreReg
from computer.memory import Memory
from computer.program_counter import ProgramCounter
from computer.registers import Registers


# NOP : Aucune opération. Sert généralement à introduire des cycles d'attente ou à occuper une place dans le programme sans effet.
# LOAD REG, MEM : Charge une valeur de la mémoire dans un registre.
# LOAD REG, IMD : Charge une valeur immédiate dans un registre.
# LOAD REG, REG : Charge la valeur d'un registre dans un autre.
# STORE REG, MEM : Stocke la valeur d'un registre en mémoire.
# STORE REG, REG : Stocke la valeur d'un registre dans l'unité mémoire pointée par un autre registre.
# JMP IMD : Saute à une adresse immédiate dans le programme, modifiant le Program Counter.
# TRAN REG, REG : Transfère la valeur d'un registre à un autre. Bien que cela puisse sembler une opération simple, c'est généralement l'unité de contrôle qui gère les transferts de données internes.

class ControlUnit:
    """
    Control unit class
    """
    def __init__(self, registers: Registers, memory: Memory, program_counter: ProgramCounter):
        # self._registers = Registers(size=registers_size, register_size=register_size)
        # self._memory = SRAM(size=memory_size, register_size=register_size)
        self._registers = registers
        self._memory = memory
        self._decoder = Decoder8To256()
        self._operations = [
            Nop(),
            LoadMem(registers=self._registers, memory=self._memory),
            LoadImd(registers=self._registers, memory=self._memory),
            LoadReg(registers=self._registers, memory=self._memory),
            StoreMem(registers=self._registers, memory=self._memory),
            StoreReg(registers=self._registers, memory=self._memory),
            Jump(registers=self._registers, memory=self._memory, program_counter=program_counter),
            # Tran(self._registers, self._memory),
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
