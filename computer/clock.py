"""
Clock module
"""
import time
from utils.logger import logger

class Clock:
    """
    Clock class with a state (HIGH/LOW)
    """
    def __init__(self):
        self.clock_state = False
        self._tick_num = 0

    def tick(self):
        """
        Clock's tick
        """
        self._tick()
        self._log_tick()
        self._tick_num += 1

    def _tick(self):
        self.clock_state = not self.clock_state

    def _log_tick(self):
        logger.debug(f"tick n°{self._tick_num}: state={self.clock_state}")


class RealTimeClock(Clock):
    """
    Real-time clock 
    """
    def __init__(self, frequency_hz):
        super().__init__()
        self.frequency_hz = frequency_hz
        self.cycle_time = 1.0 / frequency_hz

        self._computation_time = None
        self._start_tick_time = None
        self._end_tick_time = None
        self._sleep_time = None
        self._real_cycle_time = None

    def _tick(self):
        """
        Clock's tick
        """
        self._start_tick_time = time.time()

        if self._end_tick_time:
            self._computation_time = self._start_tick_time - self._end_tick_time

            if self._computation_time > self.cycle_time:
                logger.warning(f"Cycle time is {self.cycle_time} but computation time is {self._computation_time}")
            else:
                self._sleep_time = self.cycle_time - self._computation_time
                time.sleep(self._sleep_time)

        super()._tick()

        end_time = time.time()
        if self._end_tick_time:
            self._real_cycle_time = end_time - self._end_tick_time
        self._end_tick_time = end_time

    def _log_tick(self):
        logger.debug(f"tick n°{self._tick_num}: state={self.clock_state}, start time={self._start_tick_time}, "
                     f"end time={self._end_tick_time}, elapsed time={self._computation_time}, "
                     f"sleep time={self._sleep_time}, theory cycle time={self.cycle_time}, real cycle time={self._real_cycle_time}")
