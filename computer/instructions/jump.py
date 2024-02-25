"""
Jump instructions module
"""
from computer.data_types import Bits
from computer.electronic.circuits.bitwise import BitwiseMux
from computer.electronic.circuits.cmos import ORGate
from computer.instructions.instruction import ControlInstruction
from computer.memory import SRAM
from computer.program_counter import ProgramCounter
from computer.registers import Registers

# pylint: disable=R0903
class Jump(ControlInstruction):
    """
    Set the Program Counter to the immediate value
    JMP IMD		; sets PC to the immediate 16-bit value
    """
    def compute(self, reg1: Bits, reg2: Bits, value: Bits):
        self._program_counter.set(value)


class JEQ(ControlInstruction):
    """
    Set the Program Counter to the immediate value if ZF = 1
    JEQ IMD		; if ZF = 1, sets PC to the immediate 16-bit value
    """
    def __init__(self, registers: Registers, memory: SRAM, program_counter: ProgramCounter) -> None:
        super().__init__(registers, memory, program_counter)
        self._mux = BitwiseMux(2 ** self._registers.size)

    def compute(self, reg1: Bits, reg2: Bits, value: Bits):
        current_address = self._program_counter.value

        new_address = self._mux(current_address, value, self._registers.zf)
        self._program_counter.set(new_address)


class JLT(ControlInstruction):
    """
    Set the Program Counter to the immediate value if CF = 0
    JLT IMD		; if CF = 0, sets PC to the immediate 16-bit value 
    """
    def __init__(self, registers: Registers, memory: SRAM, program_counter: ProgramCounter) -> None:
        super().__init__(registers, memory, program_counter)
        self._mux = BitwiseMux(2 ** self._registers.size)

    def compute(self, reg1: Bits, reg2: Bits, value: Bits):
        current_address = self._program_counter.value

        new_address = self._mux(value, current_address, self._registers.cf)
        self._program_counter.set(new_address)


class JGE(ControlInstruction):
    """
    Set the Program Counter to the immediate value if CF = 1 or ZF = 1
    JGE IMD		; if CF = 1 or ZF = 1, sets PC to the immediate 16-bit value 
    """
    def __init__(self, registers: Registers, memory: SRAM, program_counter: ProgramCounter) -> None:
        super().__init__(registers, memory, program_counter)
        self._or = ORGate()
        self._mux = BitwiseMux(2 ** self._registers.size)

    def compute(self, reg1: Bits, reg2: Bits, value: Bits):
        current_address = self._program_counter.value

        or_result = self._or(self._registers.cf, self._registers.zf)

        new_address = self._mux(current_address, value, or_result)
        self._program_counter.set(new_address)
