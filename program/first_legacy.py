from computer_legacy.cpu import CPU
from computer_legacy.instructions.bitwise_and import BitwiseAnd
from computer_legacy.instructions.load import Load


cpu = CPU(frequency=10)
instructions = [
    Load(0, 0b10101010),
    Load(1, 0b11110000),
    BitwiseAnd(2, 0, 1),
]

for instruction in instructions:
    cpu.execute(instruction)
    cpu.print_registries()