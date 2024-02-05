"""
Clock module
"""
import time

class Clock:
    """
    Clock class with a state (HIGH/LOW)
    """
    def __init__(self):
        self.clock_state = False

    def tick(self):
        """
        Clock's tick
        """
        # Simulate the clock's rising and falling edges
        self.clock_state = not self.clock_state


class RealTimeClock(Clock):
    """
    Real-time clock 
    """
    def __init__(self, frequency_hz):
        super().__init__()
        self.frequency_hz = frequency_hz
        self.cycle_time = 1.0 / frequency_hz

    def tick(self):
        """
        Clock's tick
        """
        super().tick()

        # Simulate the time taken by one clock cycle
        time.sleep(self.cycle_time)
