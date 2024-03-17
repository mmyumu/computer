"""
Test for Control Unit module.
"""
import pytest
from computer.clock import RealTimeClock

from computer.cpu import CPU
from computer.data_types import Bits
from computer.memory import SRAM
from computer.rom import ROM
from program.program import BinaryProgram


# pylint: disable=C0116,W0212

@pytest.fixture(name="rom")
def fixture_rom():
    return ROM(size=8, register_size=22)

@pytest.fixture(name="cpu")
def fixture_cpu(real_time_clock: RealTimeClock, rom: ROM):
    memory = SRAM(size=8, register_size=3)
    memory.reset()
    cpu = CPU(real_time_clock, memory, rom, registers_size=3, register_size=3)
    cpu.reset()
    return cpu

def create_binary_instruction(opcode: int, reg_a: int, reg_b: int, value: int):
    opcode = Bits(opcode, size=8)
    reg_a = Bits(reg_a, size=3)
    reg_b = Bits(reg_b, size=3)
    value = Bits(value, size=8)

    return Bits(opcode + reg_a + reg_b + value)

def test_program_nop_halt(cpu: CPU, rom: ROM):
    program = BinaryProgram()

    # Initialize
    program.append(create_binary_instruction(0, 0, 0, 0))       # LOAD 10 -> REG 0 (start loop value)
    program.append(create_binary_instruction(255, 0, 0, 0))     # HALT

    rom.set(program)
    rom.clock_tick(True)
    cpu.run()

def test_program_initialize_registers(cpu: CPU, rom: ROM):
    program = BinaryProgram()

    # Initialize
    program.append(create_binary_instruction(6, 0, 0, 10))      # LOAD 10 -> REG 0 (start loop value)
    program.append(create_binary_instruction(6, 1, 0, 20))      # LOAD 20 -> REG 1 (end loop value)
    program.append(create_binary_instruction(6, 2, 0, 15))      # LOAD 15 -> REG 2 (value to check)
    program.append(create_binary_instruction(6, 3, 0, 100))     # LOAD 100 -> REG 3 (memory address to store 15)
    program.append(create_binary_instruction(255, 0, 0, 0))     # HALT

    rom.set(program)
    rom.clock_tick(True)
    cpu.run()

    assert cpu._registers.read(Bits(0, size=3)).to_int() == 10
    assert cpu._registers.read(Bits(1, size=3)).to_int() == 20
    assert cpu._registers.read(Bits(2, size=3)).to_int() == 15
    assert cpu._registers.read(Bits(3, size=3)).to_int() == 100

def test_program_loop_if(cpu: CPU, rom: ROM):
    program = BinaryProgram()

    # Initialize
    program.append(create_binary_instruction(6, 0, 0, 10))      # LOAD 10 -> REG 0 (start loop value)
    program.append(create_binary_instruction(6, 1, 0, 20))      # LOAD 20 -> REG 1 (end loop value)
    program.append(create_binary_instruction(6, 2, 0, 15))      # LOAD 15 -> REG 2 (value to check)
    program.append(create_binary_instruction(6, 3, 0, 100))     # LOAD 100 -> REG 3 (memory address to store 15)

    # Start loop
    program.append(create_binary_instruction(0, 0, 0, 0))       # Start loop
    program.append(create_binary_instruction(140, 1, 0, 0))     # CMP REG0, REG1
    program.append(create_binary_instruction(4, 0, 0, 15))      # JGE end loop (15)

    # Check 15
    program.append(create_binary_instruction(140, 0, 2, 0))     # CMP REG0, REG1
    program.append(create_binary_instruction(2, 0, 0, 11))      # JEQ Store value (11)

    program.append(create_binary_instruction(132, 0, 0, 0))     # INC REGA
    program.append(create_binary_instruction(1, 0, 0, 4))       # JMP start loop (4)

    program.append(create_binary_instruction(0, 0, 0, 0))       # Store value
    program.append(create_binary_instruction(9, 2, 3, 0))       # STORE REG2 (15) -> MEM (REG3=100)
    program.append(create_binary_instruction(132, 0, 0, 0))     # INC REGA
    program.append(create_binary_instruction(1, 0, 0, 4))       # JMP start loop (4)

    program.append(create_binary_instruction(0, 0, 0, 0))       # End loop

    program.append(create_binary_instruction(255, 0, 0, 0))     # HALT


    rom.set(program)
    rom.clock_tick(True)
    cpu.run()

    assert cpu._registers.read(Bits(0, size=3)).to_int() == 20
    assert cpu._registers.read(Bits(1, size=3)).to_int() == 20
    assert cpu._registers.read(Bits(2, size=3)).to_int() == 15
    assert cpu._registers.read(Bits(3, size=3)).to_int() == 100
    assert cpu._registers.read(Bits(3, size=3)).to_int() == 100

    assert cpu._memory.read(Bits(100, size=8)).to_int() == 15
#
#  ; Initialisation
# MOV REGA, 10    ; Commencez avec la valeur 10
# MOV REGB, 20    ; Valeur finale de la boucle
# MOV REGC, 15    ; Valeur à vérifier
# MOV REGD, 100   ; Adresse en mémoire où stocker 15

# ; Début de la boucle
# START_LOOP:

# CMP REGA, REGB  ; Comparez la valeur actuelle avec la valeur finale de la boucle
# JGE END_LOOP    ; Si REGA >= REGB, sortez de la boucle

# ; Vérifiez si REGA est égal à 15
# CMP REGA, REGC  ; Comparez la valeur actuelle avec 15
# JEQ STORE_VALUE ; Si égal, sautez à l'étiquette STORE_VALUE

# ; Incrémentation pour la prochaine itération de la boucle
# INC REGA        ; Incrémentez la valeur
# JMP START_LOOP  ; Sautez au début de la boucle

# ; Stockage de la valeur 15
# STORE_VALUE:
# STORE REGD, REGA ; Stockez la valeur 15 à l'adresse en mémoire spécifiée dans REGD
# INC REGA         ; Continuez la boucle
# JMP START_LOOP   ; Sautez au début de la boucle

# ; Fin de la boucle
# END_LOOP:
# NOP             ; Fin du programme, opération non nécessaire