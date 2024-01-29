from utils.logger import logger

class AluBuffer:
    def __init__(self):
        self.buffer = 0  # Initializes the buffer with a value of 0

    def load(self, value):
        # Loads a value into the buffer
        self.buffer = value

    def read(self):
        # Returns the current value of the buffer
        return self.buffer

    def write(self, value):
        # Updates the buffer with the given value
        self.load(value)  # Same as load for simplicity

    def clear(self):
        # Resets the buffer to 0
        self.buffer = 0

if __name__ == "__main__":
    alu_buffer = AluBuffer()
    alu_buffer.load(5)  # Loads the value 5 into the buffer
    logger.info(f"ALU Buffer value: {alu_buffer.read()}")  # Outputs the current value of the buffer
    alu_buffer.clear()  # Resets the buffer
    logger.info(f"ALU Buffer value after clear: {alu_buffer.read()}")  # Outputs the reset value of the buffer
