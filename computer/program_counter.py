"""
ProgramCounter (PC) module
"""
from utils.logger import logger

class ProgramCounter:
    """
    ProgramCounter (PC) class
    """
    def __init__(self):
        self.counter = 0

    def get(self):
        """
        Get the current counter
        """
        return self.counter

    def set(self, value):
        """
        Set the input tothe counter
        """
        self.counter = value

    def increment(self):
        """
        Increment the counter
        """
        self.counter += 1

if __name__ == "__main__":
    # Exemple d'utilisation
    pc = ProgramCounter()
    logger.info(pc.get())  # Affiche 0
    pc.increment()
    logger.info(pc.get())  # Affiche 1
    pc.set(10)
    logger.info(pc.get())  # Affiche 10
