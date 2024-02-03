"""
ROM module
"""
from utils.logger import logger

class ROM:
    """
    ROM class
    """
    def __init__(self, size):
        # Initialize the ROM with a defined size and fill it with zeros
        self.memory = [0] * size

    def load_program(self, program):
        """
        Load a program (a list of binary instructions) into the ROM
        """
        # Ensuring the program doesn't exceed the ROM size
        if len(program) > len(self.memory):
            raise ValueError("Program size exceeds ROM capacity")
        self.memory[:len(program)] = program

    def read_instruction(self, address):
        """
        Return the instruction at the specified address
        """
        if address >= len(self.memory):
            raise IndexError("Attempted to read outside ROM bounds")
        return self.memory[address]

if __name__ == "__main__":
    rom = ROM(64)  # Create a ROM with 64 slots
    program_instructions = [0b11001010, 0b00101111, 0b10101010]  # An example program (list of binary instructions)
    rom.load_program(program_instructions)

    # Reading instructions at different addresses
    logger.info(format(rom.read_instruction(0), '#010b'))  # Outputs the first instruction
    logger.info(format(rom.read_instruction(1), '#010b'))  # Outputs the second instruction
    # ...
