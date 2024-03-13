"""
Control unit module
"""
from computer.alu import ALU
from computer.data_types import Bits
from computer.electronic.circuits.demux import DEMUX1To2
from computer.instruction_executor import InstructionExecutor
from computer.instructions.flags import CLC, STC
from computer.instructions.jump import JEQ, JGE, JLT, Jump
from computer.instructions.load import LoadImd, LoadMem, LoadReg
from computer.instructions.nop import Nop
from computer.instructions.store import StoreMem, StoreReg
from computer.instructions.tran import Tran
from computer.memory import Memory
from computer.program_counter import ProgramCounter
from computer.registers import Registers


class ControlUnit(InstructionExecutor):
    """
    Control unit class
    """
    def __init__(self, registers: Registers, memory: Memory, program_counter: ProgramCounter):
        self._registers = registers
        self._memory = memory
        self._program_counter = program_counter

        self._alu = ALU(self._registers, memory.size)
        self._demux = DEMUX1To2()

        instructions = [
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

        super().__init__(instructions)

        self._units = [self, self._alu]

    def execute(self, opcode: Bits, operand: Bits):
        """
        Execute the operation defined with the opcode and with operand as parameter

        Args:
            opcode (Bits): the opcode of the instruction to execute. 
                            8 bits.
            operand (Bits): the operand to pass to the instruction
        """
        if len(opcode) != 8:
            raise ValueError(f"Length of operand should be {8} but is {len(opcode)}")

        operand_check_size = (2 ** self._memory.register_size) + (self._registers.size * 2)
        if len(operand) != operand_check_size:
            raise ValueError(f"Length of operand should be {operand_check_size} but is {len(operand)}")

        bits = self._demux(True, opcode[0])
        for i, bit in enumerate(bits[::-1]):
            if bit:
                self._units[i].execute_instruction(opcode[1:], operand)
                break
