"""
Clock module (legacy)
"""
import time

class Clock:
    """
    Clock class (legacy)
    """
    def __init__(self, frequency):
        self.frequency = frequency

    def wait_cycle(self):
        """
        Wait one clock cycle (clock tick)
        """
        time.sleep(1 / self.frequency)
