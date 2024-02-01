from computer_legacy.alu import ALU
from computer_legacy.clock import Clock
from utils.logger import logger


class CPU:
    def __init__(self, register_size=8, frequency=1):
        self.registers = [0] * 4
        self.clock = Clock(frequency)
        self.alu = ALU(register_size)

    def execute(self, instruction):
        self.clock.wait_cycle()
        instruction.execute(self)

    def print_registries(self):
        logger.info([bin(reg) for reg in self.registers])