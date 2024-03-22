"""
Test for GUIGNOL interpreter module
"""

import pytest

from guignol.interpreter import Interpreter

# pylint: disable=C0116

@pytest.fixture(name="interpreter_8bits")
def fixture_interpreter_8bits():
    return Interpreter("grammar/guignol.lark", register_size=3)

def test_interpreter(interpreter_8bits: Interpreter):
    with open("program/test.guignol", 'r', encoding='utf8') as f:
        guignol_program = f.read()
        binary_program = interpreter_8bits(guignol_program)

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
