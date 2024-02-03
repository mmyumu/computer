"""
InPort module
"""
from utils.logger import logger

class InPort:
    """
    InPort class
    """
    def __init__(self):
        self.data = None

    def read_data(self, value):
        """
        Read data from the input
        """
        # Here you would have the logic to read data from an external source.
        # For simulation purposes, we'll just return a fixed value or a random value.
        self.data = value  # Placeholder for actual input data
        return self.data

if __name__ == "__main__":
    # Example usage
    in_port = InPort()
    input_data = in_port.read_data(0b00010)
    logger.info(f"Data read from InPort: {input_data}")
