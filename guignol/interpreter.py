"""
Interpreter module
"""
from abc import abstractmethod
from typing import Dict, Generic, List, TypeVar
from lark import Lark, Transformer

from computer.data_types import Bits
from computer.program import BinaryProgram, Program, Requirements

GRAMMAR_PATH = "grammar/guignol.lark"
T = TypeVar("T")

#pylint: disable=C0116,R0904


class Label:
    """
    Class representing a label in the interpreter
    """
    def __init__(self, name) -> None:
        self.name = name
        self.pc = None

    def set_pc(self, pc: int):
        self.pc = pc


class LabelTransformer(Transformer):
    """
    Transform labels when interpreting
    """
    def label(self, args):
        return Label(args[0].value)


class InstructionToBinary(Transformer):
    """
    Transform GUIGNOL instructions to Binary instructions
    """
    def __init__(self, register_size: int, labels: List[Label], visit_tokens: bool = True) -> None:
        super().__init__(visit_tokens)
        self._register_size = register_size
        self._value_size = 2 ** self._register_size
        self._labels = labels

    def _forge_instruction(self, opcode: int, reg1: int, reg2: int, value: int):
        opcode = Bits(opcode, size=8)
        reg1 = Bits(reg1, size=self._register_size)
        reg2 = Bits(reg2, size=self._register_size)
        value = Bits(value, size=self._value_size)
        return Bits(opcode + reg1 + reg2 + value)

    def nop(self, _):
        return self._forge_instruction(0, 0, 0, 0)

    def jmp(self, args):
        address = int(args[0].value[1:])
        return self._forge_instruction(1, 0, 0, address)

    def jmp_label(self, args):
        label_name = args[0].children[0].value
        address = self._labels[label_name].pc
        return self._forge_instruction(1, 0, 0, address)

    def jeq(self, args):
        address = int(args[0].value[1:])
        return self._forge_instruction(2, 0, 0, address)

    def jeq_label(self, args):
        label_name = args[0].children[0].value
        address = self._labels[label_name].pc
        return self._forge_instruction(2, 0, 0, address)

    def jlt(self, args):
        address = int(args[0].value[1:])
        return self._forge_instruction(3, 0, 0, address)

    def jlt_label(self, args):
        label_name = args[0].children[0].value
        address = self._labels[label_name].pc
        return self._forge_instruction(3, 0, 0, address)

    def jge(self, args):
        address = int(args[0].value[1:])
        return self._forge_instruction(4, 0, 0, address)

    def jge_label(self, args):
        label_name = args[0].children[0].value
        address = self._labels[label_name].pc
        return self._forge_instruction(4, 0, 0, address)

    def load_mem(self, args):
        reg1 = args[0]
        address = int(args[1].value[1:])
        return self._forge_instruction(5, reg1, 0, address)

    def load_imd(self, args):
        reg1 = args[0]
        value = int(args[1].value)
        return self._forge_instruction(6, reg1, 0, value)

    def load_reg(self, args):
        reg1 = args[0]
        reg2 = args[1]
        return self._forge_instruction(7, reg1, reg2, 0)

    def store_mem(self, args):
        reg1 = args[0]
        address = int(args[1].value[1:])
        return self._forge_instruction(8, reg1, 0, address)

    def store_reg(self, args):
        reg1 = args[0]
        reg2 = args[1]
        return self._forge_instruction(9, reg1, reg2, 0)

    def tran_reg(self, args):
        reg1 = args[0]
        reg2 = args[1]
        return self._forge_instruction(10, reg1, reg2, 0)

    def clc(self, _):
        return self._forge_instruction(11, 0, 0, 0)

    def stc(self, _):
        return self._forge_instruction(12, 0, 0, 0)

    def add(self, args):
        reg1 = args[0]
        reg2 = args[1]
        return self._forge_instruction(128, reg1, reg2, 0)

    def sub(self, args):
        reg1 = args[0]
        reg2 = args[1]
        return self._forge_instruction(129, reg1, reg2, 0)

    def mult(self, args):
        reg1 = args[0]
        reg2 = args[1]
        return self._forge_instruction(130, reg1, reg2, 0)

    def div(self, args):
        reg1 = args[0]
        reg2 = args[1]
        return self._forge_instruction(131, reg1, reg2, 0)

    def inc(self, args):
        reg1 = args[0]
        return self._forge_instruction(132, reg1, 0, 0)

    def dec(self, args):
        reg1 = args[0]
        return self._forge_instruction(133, reg1, 0, 0)

    def and_reg(self, args):
        reg1 = args[0]
        reg2 = args[1]
        return self._forge_instruction(134, reg1, reg2, 0)

    def or_reg(self, args):
        reg1 = args[0]
        reg2 = args[1]
        return self._forge_instruction(135, reg1, reg2, 0)

    def xor(self, args):
        reg1 = args[0]
        reg2 = args[1]
        return self._forge_instruction(136, reg1, reg2, 0)

    def not_reg(self, args):
        reg1 = args[0]
        return self._forge_instruction(137, reg1, 0, 0)

    def rol(self, args):
        reg1 = args[0]
        value = int(args[1].value)
        return self._forge_instruction(138, reg1, 0, value)

    def ror(self, args):
        reg1 = args[0]
        value = int(args[1].value)
        return self._forge_instruction(139, reg1, 0, value)

    def cmp(self, args):
        reg1 = args[0]
        reg2 = args[1]
        return self._forge_instruction(140, reg1, reg2, 0)

    def halt(self, _):
        max_register = 2 ** self._register_size -1
        max_value = 2 ** self._value_size -1
        return self._forge_instruction(255, max_register, max_register, max_value)

    def register(self, args):
        return int(args[0].value)


class Requirement(Transformer):
    """
    Transform requirements to tuple values
    """
    def memory_size(self, args):
        memory_size = int(args[0].value)
        return "memory size", memory_size

    def register_size(self, args):
        register_size = int(args[0].value)
        return "register size", register_size

    def screen_resolution(self, args):
        screen_resolution = int(args[0].value)
        return "screen resolution", screen_resolution


class BaseInterpreter(Generic[T]):
    """
    Base class for interpreter    
    """
    def __call__(self, program: str, from_file=False) -> T:
        if from_file:
            with open(program, 'r', encoding='utf8') as f:
                program = f.read()
        return self._interpret(program)

    @abstractmethod
    def _interpret(self, program: str) -> T:
        pass


class LabelsInterpreter(BaseInterpreter[dict]):
    """
    Interpreter class to parse the labels
    """
    def __init__(self) -> None:
        super().__init__()
        self._parser = Lark.open(GRAMMAR_PATH, rel_to=__file__, parser="lalr", transformer=LabelTransformer())

    def _interpret(self, program: str) -> Dict[str, Label]:
        parsed_program = self._parser.parse(program)

        labels = {}

        instruction_number = 0
        parsed_instructions_or_labels = parsed_program.children[1].children
        for parsed_instruction_or_label in parsed_instructions_or_labels:
            if isinstance(parsed_instruction_or_label, Label):
                parsed_instruction_or_label.set_pc(instruction_number)
                labels[parsed_instruction_or_label.name] = parsed_instruction_or_label
            else:
                instruction_number += 1
        return labels


class BinaryProgramInterpreter(BaseInterpreter[BinaryProgram]):
    """
    Interpreter class to parse the binary part of GUIGNOL program
    """
    def __init__(self, labels: List[Label], register_size: int = 4) -> None:
        super().__init__()
        self._parser = Lark.open(GRAMMAR_PATH, rel_to=__file__, parser="lalr", transformer=InstructionToBinary(register_size, labels))

    def _interpret(self, program: str) -> BinaryProgram:
        parsed_program = self._parser.parse(program)
        program = BinaryProgram()

        parsed_instructions = parsed_program.children[1].children
        for parsed_instruction in parsed_instructions:
            if isinstance(parsed_instruction, Bits):
                program.append(parsed_instruction)
        return program


class RequirementsInterpreter(BaseInterpreter[Requirements]):
    """
    Interpreter class to parse the requirements part of GUIGNOL program
    """
    def __init__(self) -> None:
        super().__init__()
        self._parser = Lark.open(GRAMMAR_PATH, rel_to=__file__, parser="lalr", transformer=Requirement())

    def _interpret(self, program: str) -> Requirements:
        parsed_program = self._parser.parse(program)

        parsed_requirements = parsed_program.children[0].children

        requirements = Requirements()
        for parsed_requirement in parsed_requirements:
            req_name, req_value = parsed_requirement
            if req_name == "memory size":
                requirements.memory_size = req_value
            elif req_name == "register size":
                requirements.register_size = req_value
            elif req_name == "screen resolution":
                requirements.screen_resolution = req_value

        return requirements


class Interpreter(BaseInterpreter[Program]):
    """
    GUIGNOL program interpreter
    """
    def __init__(self) -> None:
        # self._parser = Lark.open(GRAMMAR_PATH, rel_to=__file__, parser="lalr", transformer=Labels())
        self._labels_interpreter = LabelsInterpreter()
        self._requirements_interpreter = RequirementsInterpreter()

    def _interpret(self, program: str) -> Program:
        # tree = self._parser.parse(program)
        labels = self._labels_interpreter(program, from_file=False)
        # self.collect_labels(tree)

        requirements_interpreter = RequirementsInterpreter()
        requirements = requirements_interpreter(program, from_file=False)

        kwargs = {}
        if requirements.register_size:
            kwargs['register_size'] = requirements.register_size

        binary_program_interpreter = BinaryProgramInterpreter(labels=labels, **kwargs)
        binary_program = binary_program_interpreter(program, from_file=False)

        return Program(requirements, binary_program)

    # def collect_labels(self, tree: ParseTree):
    #     label_addresses = {}
    #     pc = 0
    #     for child in tree.children:
    #         # if isinstance(child, Label):
    #         if isinstance(child, str):
    #             label_addresses[child.name] = pc
    #         else:
    #             pc += 1
    #     return label_addresses