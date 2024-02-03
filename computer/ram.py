"""
RAM module
"""
from utils.logger import logger

class RAM:
    """
    RAM class
    """
    def __init__(self, size):
        self.memory = [0] * size  # Initialize the RAM with zeros

    def read(self, address):
        """
        Read data from the specified address
        """
        if address < 0 or address >= len(self.memory):
            raise IndexError("Address out of bounds")
        return self.memory[address]

    def write(self, address, value):
        """
        Write data to the specified address
        """
        if address < 0 or address >= len(self.memory):
            raise IndexError("Address out of bounds")
        self.memory[address] = value & 0xFF  # Ensure the value is within byte limits

    def print(self):
        """
        Print the RAM status
        """
        for address, memory in enumerate(self.memory):
            logger.info(f"Address {address}: {memory}")

if __name__ == "__main__":
    # Example usage
    ram = RAM(1024)  # Create a RAM of 1024 bytes

    # Writing and reading data
    ram.write(10, 255)  # Write 255 at address 10
    logger.info(f"Value at address 10: {ram.read(10)}")  # Read the value at address 10
