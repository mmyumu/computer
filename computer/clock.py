import time

class Clock:
    def __init__(self, frequency):
        self.frequency = frequency

    def wait_cycle(self):
        time.sleep(1 / self.frequency)