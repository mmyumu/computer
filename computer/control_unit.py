"""
Control unit module
"""
from computer.alu import ALU
from computer.data_types import Bits, Opcode8
from computer.electronic.circuits.decoder import Decoder2To4, Decoder8To256
from computer.electronic.circuits.demux import DEMUX1To2
from computer.instructions.flags import CLC, STC
from computer.instructions.jump import JEQ, JGE, JLT, Jump
from computer.instructions.load import LoadImd, LoadMem, LoadReg
from computer.instructions.nop import Nop
from computer.instructions.store import StoreMem, StoreReg
from computer.instructions.tran import Tran
from computer.memory import Memory
from computer.program_counter import ProgramCounter
from computer.registers import Registers


class ControlUnit:
    """
    Control unit class
    """
    def __init__(self, registers: Registers, memory: Memory, program_counter: ProgramCounter):
        self._registers = registers
        self._memory = memory
        self._program_counter = program_counter

        self._alu = ALU(self._registers, memory.size)
        self._demux = DEMUX1To2()
        self._decoder = Decoder8To256()
        
        self._operations = [
            Nop(),
            Jump(registers=self._registers, memory=self._memory, program_counter=program_counter),
            JEQ(registers=self._registers, memory=self._memory, program_counter=program_counter),
            JLT(registers=self._registers, memory=self._memory, program_counter=program_counter),
            JGE(registers=self._registers, memory=self._memory, program_counter=program_counter),
            LoadMem(registers=self._registers, memory=self._memory, program_counter=program_counter),
            LoadImd(registers=self._registers, memory=self._memory, program_counter=program_counter),
            LoadReg(registers=self._registers, memory=self._memory, program_counter=program_counter),
            StoreMem(registers=self._registers, memory=self._memory, program_counter=program_counter),
            StoreReg(registers=self._registers, memory=self._memory, program_counter=program_counter),
            Tran(registers=self._registers, memory=self._memory, program_counter=program_counter),
            CLC(registers=self._registers, memory=self._memory, program_counter=program_counter),
            STC(registers=self._registers, memory=self._memory, program_counter=program_counter),
        ]

    def execute(self, opcode: Bits, operand: Bits):
        """
        Execute the operation defined with the opcode and with operand as parameter
        """
        if len(opcode) != 8:
            raise ValueError(f"Length of operand should be {8} but is {len(opcode)}")
        
        operand_check_size = self._memory.size + (self._registers.size * 2)
        if len(operand) != operand_check_size:
            raise ValueError(f"Length of operand should be {operand_check_size} but is {len(operand)}")

        demux_result = self._demux(opcode[0], True)

        if demux_result == 0:
            self.execute_instruction(opcode[1:], operand)
        else:
            self._alu.execute_instruction(opcode[1:], operand)

    def execute_instruction(self, opcode: Bits, operand: Bits):
        bits = self._decoder(*opcode, True)
        for i, bit in enumerate(bits[::-1]):
            if bit:
                self._operations[i](operand)
                break
