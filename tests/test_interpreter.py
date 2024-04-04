"""
Test for GUIGNOL interpreter module
"""

import pytest

from guignol.interpreter import BinaryProgramInterpreter, Interpreter, RequirementsInterpreter

# pylint: disable=C0116

@pytest.fixture(name="binary_interpreter_8bits")
def fixture_binary_interpreter_8bits():
    return BinaryProgramInterpreter([], register_size=3)

@pytest.fixture(name="requirement_interpreter")
def fixture_requirement_interpreter():
    return RequirementsInterpreter()

@pytest.fixture(name="interpreter")
def fixture_interpreter():
    return Interpreter()

def test_binary_interpreter(binary_interpreter_8bits: BinaryProgramInterpreter):
    with open("program/test.guignol", 'r', encoding='utf8') as f:
        guignol_program = f.read()
        binary_program = binary_interpreter_8bits(guignol_program)

    assert binary_program[0] == [0] * 22                                                                    # NOP
    assert binary_program[1] == [0, 0, 0, 0, 0, 0, 0, 1] + [0, 0, 0] + [0, 0, 0] + [0, 0, 0, 0, 1, 0, 1, 0] # JMP @10
    assert binary_program[2] == [0, 0, 0, 0, 0, 0, 1, 0] + [0, 0, 0] + [0, 0, 0] + [0, 0, 0, 0, 1, 1, 1, 1] # JEQ @15
    assert binary_program[3] == [0, 0, 0, 0, 0, 0, 1, 1] + [0, 0, 0] + [0, 0, 0] + [0, 0, 0, 1, 0, 1, 0, 0] # JLT @20
    assert binary_program[4] == [0, 0, 0, 0, 0, 1, 0, 0] + [0, 0, 0] + [0, 0, 0] + [0, 0, 0, 1, 1, 0, 0, 1] # JGE @25
    assert binary_program[5] == [0, 0, 0, 0, 0, 1, 0, 1] + [0, 0, 1] + [0, 0, 0] + [0, 0, 0, 0, 1, 0, 1, 0] # LOAD REG 1, @10
    assert binary_program[6] == [0, 0, 0, 0, 0, 1, 1, 0] + [0, 1, 0] + [0, 0, 0] + [1, 0, 0, 1, 0, 1, 1, 0] # LOAD REG 2, 150
    assert binary_program[7] == [0, 0, 0, 0, 0, 1, 1, 1] + [0, 1, 1] + [1, 0, 0] + [0, 0, 0, 0, 0, 0, 0, 0] # LOAD REG 3, REG4
    assert binary_program[8] == [0, 0, 0, 0, 1, 0, 0, 0] + [1, 0, 1] + [0, 0, 0] + [0, 0, 1, 1, 0, 0, 1, 0] # STORE REG 5, @50
    assert binary_program[9] == [0, 0, 0, 0, 1, 0, 0, 1] + [1, 1, 0] + [1, 1, 1] + [0, 0, 0, 0, 0, 0, 0, 0] # STORE REG 6, REG 7
    assert binary_program[10] == [0, 0, 0, 0, 1, 0, 1, 0] + [0, 0, 1] + [0, 1, 0] + [0, 0, 0, 0, 0, 0, 0, 0] # TRAN REG 1, REG 2
    assert binary_program[11] == [0, 0, 0, 0, 1, 0, 1, 1] + [0, 0, 0] + [0, 0, 0] + [0, 0, 0, 0, 0, 0, 0, 0] # CLC
    assert binary_program[12] == [0, 0, 0, 0, 1, 1, 0, 0] + [0, 0, 0] + [0, 0, 0] + [0, 0, 0, 0, 0, 0, 0, 0] # STC
    assert binary_program[13] == [1, 0, 0, 0, 0, 0, 0, 0] + [0, 0, 1] + [0, 1, 0] + [0, 0, 0, 0, 0, 0, 0, 0] # ADD REG 1, REG 2
    assert binary_program[14] == [1, 0, 0, 0, 0, 0, 0, 1] + [0, 1, 1] + [1, 0, 0] + [0, 0, 0, 0, 0, 0, 0, 0] # SUB REG 3, REG 4
    assert binary_program[15] == [1, 0, 0, 0, 0, 0, 1, 0] + [1, 0, 0] + [1, 1, 0] + [0, 0, 0, 0, 0, 0, 0, 0] # MULT REG 4, REG 6
    assert binary_program[16] == [1, 0, 0, 0, 0, 0, 1, 1] + [0, 0, 1] + [1, 1, 1] + [0, 0, 0, 0, 0, 0, 0, 0] # DIV REG 1, REG 7
    assert binary_program[17] == [1, 0, 0, 0, 0, 1, 0, 0] + [0, 0, 1] + [0, 0, 0] + [0, 0, 0, 0, 0, 0, 0, 0] # INC REG 1
    assert binary_program[18] == [1, 0, 0, 0, 0, 1, 0, 1] + [0, 1, 0] + [0, 0, 0] + [0, 0, 0, 0, 0, 0, 0, 0] # DEC REG 2
    assert binary_program[19] == [1, 0, 0, 0, 0, 1, 1, 0] + [0, 1, 1] + [1, 0, 0] + [0, 0, 0, 0, 0, 0, 0, 0] # AND REG 3, REG 4
    assert binary_program[20] == [1, 0, 0, 0, 0, 1, 1, 1] + [0, 0, 0] + [0, 0, 1] + [0, 0, 0, 0, 0, 0, 0, 0] # OR REG 0, REG 1
    assert binary_program[21] == [1, 0, 0, 0, 1, 0, 0, 0] + [0, 0, 1] + [0, 1, 0] + [0, 0, 0, 0, 0, 0, 0, 0] # XOR REG 1, REG 2
    assert binary_program[22] == [1, 0, 0, 0, 1, 0, 0, 1] + [0, 0, 0] + [0, 0, 0] + [0, 0, 0, 0, 0, 0, 0, 0] # NOT REG 0
    assert binary_program[23] == [1, 0, 0, 0, 1, 0, 1, 0] + [1, 0, 1] + [0, 0, 0] + [0, 0, 0, 0, 0, 0, 1, 1] # ROL REG 5, 3
    assert binary_program[24] == [1, 0, 0, 0, 1, 0, 1, 1] + [1, 1, 1] + [0, 0, 0] + [0, 0, 0, 0, 0, 0, 1, 0] # ROR REG 7, 2
    assert binary_program[25] == [1, 0, 0, 0, 1, 1, 0, 0] + [0, 0, 1] + [0, 0, 0] + [0, 0, 0, 0, 0, 0, 0, 0] # CMP REG 1, REG 0


def test_requirements_interpreter_none(requirement_interpreter: RequirementsInterpreter):
    with open("program/test.guignol", 'r', encoding='utf8') as f:
        guignol_program = f.read()
        requirements = requirement_interpreter(guignol_program)

    assert requirements.memory_size is None
    assert requirements.register_size is None
    assert requirements.screen_resolution is None

def test_requirements_interpreter(requirement_interpreter: RequirementsInterpreter):
    with open("program/test_perf.guignol", 'r', encoding='utf8') as f:
        guignol_program = f.read()
        requirements = requirement_interpreter(guignol_program)

    assert requirements.memory_size == 8
    assert requirements.register_size == 4
    assert requirements.screen_resolution is None


def test_interpreter(interpreter: Interpreter):
    with open("program/test_8bits.guignol", 'r', encoding='utf8') as f:
        guignol_program = f.read()
        program = interpreter(guignol_program)

    assert program.requirements.memory_size is None
    assert program.requirements.register_size == 3
    assert program.requirements.screen_resolution is None

    binary_program = program.binary_program

    assert binary_program[0] == [0] * 22                                                                    # NOP
    assert binary_program[1] == [0, 0, 0, 0, 0, 0, 0, 1] + [0, 0, 0] + [0, 0, 0] + [0, 0, 0, 0, 1, 0, 1, 0] # JMP @10
    assert binary_program[2] == [0, 0, 0, 0, 0, 0, 1, 0] + [0, 0, 0] + [0, 0, 0] + [0, 0, 0, 0, 1, 1, 1, 1] # JEQ @15
    assert binary_program[3] == [0, 0, 0, 0, 0, 0, 1, 1] + [0, 0, 0] + [0, 0, 0] + [0, 0, 0, 1, 0, 1, 0, 0] # JLT @20
    assert binary_program[4] == [0, 0, 0, 0, 0, 1, 0, 0] + [0, 0, 0] + [0, 0, 0] + [0, 0, 0, 1, 1, 0, 0, 1] # JGE @25
    assert binary_program[5] == [0, 0, 0, 0, 0, 1, 0, 1] + [0, 0, 1] + [0, 0, 0] + [0, 0, 0, 0, 1, 0, 1, 0] # LOAD REG 1, @10
    assert binary_program[6] == [0, 0, 0, 0, 0, 1, 1, 0] + [0, 1, 0] + [0, 0, 0] + [1, 0, 0, 1, 0, 1, 1, 0] # LOAD REG 2, 150
    assert binary_program[7] == [0, 0, 0, 0, 0, 1, 1, 1] + [0, 1, 1] + [1, 0, 0] + [0, 0, 0, 0, 0, 0, 0, 0] # LOAD REG 3, REG4
    assert binary_program[8] == [0, 0, 0, 0, 1, 0, 0, 0] + [1, 0, 1] + [0, 0, 0] + [0, 0, 1, 1, 0, 0, 1, 0] # STORE REG 5, @50
    assert binary_program[9] == [0, 0, 0, 0, 1, 0, 0, 1] + [1, 1, 0] + [1, 1, 1] + [0, 0, 0, 0, 0, 0, 0, 0] # STORE REG 6, REG 7
    assert binary_program[10] == [0, 0, 0, 0, 1, 0, 1, 0] + [0, 0, 1] + [0, 1, 0] + [0, 0, 0, 0, 0, 0, 0, 0] # TRAN REG 1, REG 2
    assert binary_program[11] == [0, 0, 0, 0, 1, 0, 1, 1] + [0, 0, 0] + [0, 0, 0] + [0, 0, 0, 0, 0, 0, 0, 0] # CLC
    assert binary_program[12] == [0, 0, 0, 0, 1, 1, 0, 0] + [0, 0, 0] + [0, 0, 0] + [0, 0, 0, 0, 0, 0, 0, 0] # STC
    assert binary_program[13] == [1, 0, 0, 0, 0, 0, 0, 0] + [0, 0, 1] + [0, 1, 0] + [0, 0, 0, 0, 0, 0, 0, 0] # ADD REG 1, REG 2
    assert binary_program[14] == [1, 0, 0, 0, 0, 0, 0, 1] + [0, 1, 1] + [1, 0, 0] + [0, 0, 0, 0, 0, 0, 0, 0] # SUB REG 3, REG 4
    assert binary_program[15] == [1, 0, 0, 0, 0, 0, 1, 0] + [1, 0, 0] + [1, 1, 0] + [0, 0, 0, 0, 0, 0, 0, 0] # MULT REG 4, REG 6
    assert binary_program[16] == [1, 0, 0, 0, 0, 0, 1, 1] + [0, 0, 1] + [1, 1, 1] + [0, 0, 0, 0, 0, 0, 0, 0] # DIV REG 1, REG 7
    assert binary_program[17] == [1, 0, 0, 0, 0, 1, 0, 0] + [0, 0, 1] + [0, 0, 0] + [0, 0, 0, 0, 0, 0, 0, 0] # INC REG 1
    assert binary_program[18] == [1, 0, 0, 0, 0, 1, 0, 1] + [0, 1, 0] + [0, 0, 0] + [0, 0, 0, 0, 0, 0, 0, 0] # DEC REG 2
    assert binary_program[19] == [1, 0, 0, 0, 0, 1, 1, 0] + [0, 1, 1] + [1, 0, 0] + [0, 0, 0, 0, 0, 0, 0, 0] # AND REG 3, REG 4
    assert binary_program[20] == [1, 0, 0, 0, 0, 1, 1, 1] + [0, 0, 0] + [0, 0, 1] + [0, 0, 0, 0, 0, 0, 0, 0] # OR REG 0, REG 1
    assert binary_program[21] == [1, 0, 0, 0, 1, 0, 0, 0] + [0, 0, 1] + [0, 1, 0] + [0, 0, 0, 0, 0, 0, 0, 0] # XOR REG 1, REG 2
    assert binary_program[22] == [1, 0, 0, 0, 1, 0, 0, 1] + [0, 0, 0] + [0, 0, 0] + [0, 0, 0, 0, 0, 0, 0, 0] # NOT REG 0
    assert binary_program[23] == [1, 0, 0, 0, 1, 0, 1, 0] + [1, 0, 1] + [0, 0, 0] + [0, 0, 0, 0, 0, 0, 1, 1] # ROL REG 5, 3
    assert binary_program[24] == [1, 0, 0, 0, 1, 0, 1, 1] + [1, 1, 1] + [0, 0, 0] + [0, 0, 0, 0, 0, 0, 1, 0] # ROR REG 7, 2
    assert binary_program[25] == [1, 0, 0, 0, 1, 1, 0, 0] + [0, 0, 1] + [0, 0, 0] + [0, 0, 0, 0, 0, 0, 0, 0] # CMP REG 1, REG 0
