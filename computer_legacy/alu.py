"""
ALU module (legacy)
"""
class ALU:
    """
    ALU class (legacy)
    """
    def __init__(self, register_size):
        self.register_size = register_size

    def load(self, registers, register_index, value):
        """
        Load operation
        """
        registers[register_index] = value & ((1 << self.register_size) - 1)

    def bitwise_and(self, registers, dest_reg, src_reg1, src_reg2):
        """
        Bitwise AND operation
        """
        registers[dest_reg] = registers[src_reg1] & registers[src_reg2]

    def bitwise_or(self, registers, dest_reg, src_reg1, src_reg2):
        """
        Bitwise OR operation
        """
        registers[dest_reg] = registers[src_reg1] | registers[src_reg2]

    def shift_left(self, registers, register_index, n):
        """
        Shift left operation
        """
        registers[register_index] = (registers[register_index] << n) & ((1 << self.register_size) - 1)

    def shift_right(self, registers, register_index, n):
        """
        Shift right operation
        """
        registers[register_index] = (registers[register_index] >> n) & ((1 << self.register_size) - 1)

    def add(self, registers, dest_reg, src_reg1, src_reg2):
        """
        Add operation
        """
        registers[dest_reg] = (registers[src_reg1] + registers[src_reg2]) & ((1 << self.register_size) - 1)
