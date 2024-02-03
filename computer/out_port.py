"""
OutPort module
"""
from utils.logger import logger

class OutPort:
    """
    OutPort class
    """
    def __init__(self):
        self.data = None

    def write_data(self, data):
        """
        Write the input to the OutPort
        """
        # Here you would have the logic to send data to an external destination.
        # For simulation purposes, we'll just print the data to the console.
        self.data = data
        logger.info(f"Data written to OutPort: {self.data}")

if __name__ == "__main__":
    # Example usage
    out_port = OutPort()
    out_port.write_data(42)  # Send the data previously read from InPort
