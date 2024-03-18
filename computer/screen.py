"""
Screen module
"""
import math
import threading
import time
from typing import List

from computer.data_types import Bits
from computer.memory import Memory

class Screen(threading.Thread):
    """
    Screen class using its own thread for refresh frequency
    """
    def __init__(self, memory: Memory, resolution: int = 128, refresh_rate: int=30):
        super().__init__()

        minimum_size = (resolution * resolution) / (2 ** memory.register_size)
        if minimum_size > 2 ** memory.size:
            raise ValueError(f"Memory should at least size of {minimum_size} but is size {2 ** memory.size}"
                             f"to be able to display screen of resolution {resolution}")

        self._memory = memory
        self._resolution = resolution
        self._refresh_rate = refresh_rate

        self._screen_data: List[bool] = None

        self._stop_event = threading.Event()

    def run(self):
        while not self._stop_event.is_set():
            self.refresh()
            time.sleep(1 / self._refresh_rate)

    def _get_data(self) -> List[bool]:
        memory_register_bit_size = 2** self._memory.register_size
        resolution_size = self._resolution * self._resolution
        number_of_register = math.ceil(resolution_size / memory_register_bit_size)

        address_offset = (2 ** self._memory.size) - number_of_register

        data = []
        for i in range(number_of_register):
            address = address_offset + i
            bits = self._memory.read(Bits(address, size=memory_register_bit_size))

            number_of_bits_to_get = memory_register_bit_size
            if i == 0:
                if (number_of_register * memory_register_bit_size) % resolution_size > 0:
                    number_of_bits_to_get = (number_of_register * memory_register_bit_size) % resolution_size


            data.extend(bits[:number_of_bits_to_get])
        return data

    def refresh(self):
        """
        Screen is refreshed
        """
        self._screen_data = self._get_data()
        self._print_data()

    def _print_data(self):
        # TODO: print screen_data
        pass


    def stop(self):
        """
        Stops the thread properly
        """
        self._stop_event.set()
