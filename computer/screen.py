"""
Screen module
"""
import math
import threading
import time
from typing import List, Optional, Tuple

from rich.console import Console
from rich.table import Table
from rich.live import Live
from rich import box
from rich.layout import Layout

from computer.data_types import Bits
from computer.memory import Memory

class Screen(threading.Thread):
    """
    Screen class
    """
    def __init__(self, memory: Memory, resolution: int = 128, refresh_rate: int = 1):
        super().__init__()
        minimum_size = (resolution * resolution) / (2 ** memory.register_size)
        if minimum_size > 2 ** memory.size:
            raise ValueError(f"Memory should at least be the size of {minimum_size}, but is {2 ** memory.size} "
                             f"to be able to display a screen of resolution {resolution}")
        self._memory = memory
        self._resolution = resolution
        self._refresh_rate = refresh_rate
        self._screen_data: Optional[List[Bits]] = None
        self._stop_event = threading.Event()
        self.console = Console()
        self.live = Live(console=self.console, refresh_per_second=self._refresh_rate)
        self._number_of_frames = 0
        self._start_time = None
        self._last_time = None

    def run(self):
        self._start_time = time.time()
        with self.live:
            while not self._stop_event.is_set():
                self.refresh()
                self._number_of_frames += 1

                time_to_wait = 1 / self._refresh_rate
                if self._last_time:
                    elapsed_time = time.time() - self._last_time
                    time_to_wait -= elapsed_time
                    time_to_wait = max(time_to_wait, 0)
                time.sleep(time_to_wait)
                self._last_time = time.time()

    def _get_data(self) -> List[bool]:
        resolution_size = self._resolution * self._resolution
        address_offset = (2 ** self._memory.size) - resolution_size

        screen_data = []
        for i in range(resolution_size):
            address = address_offset + i
            datum = self._memory.read(Bits(address, size=self._memory.size))
            screen_data.append(datum)
        return screen_data

    def refresh(self):
        """
        Screen is refreshed.
        """
        self._screen_data = self._get_data()
        self._print_data()

    def _create_screen(self) -> Layout:
        layout = Layout()

        infos = self._create_infos()
        table = self._create_table()

        layout.split_column(
            Layout(infos, name="infos", size=1),
            Layout(table, name="screen", size=self._resolution + 2),
        )

        return layout

    def _create_infos(self) -> str:
        elapsed_time = time.time() - self._start_time
        return f"Screen freq.: [#0087d7]{self._number_of_frames / elapsed_time:.2f}Hz[/] ({self._refresh_rate}Hz)"

    def _create_table(self) -> Table:
        table = Table(box=box.SQUARE, show_header=False, show_edge=True, padding=0)
        for _ in range(self._resolution):
            table.add_column()
        for row in range(self._resolution):
            cells = []
            for col in range(self._resolution):
                pixel_data = self._screen_data[row * self._resolution + col]

                r8, g8, b8 = Screen.rgbxxx_to_rgb888(pixel_data)
                color_as_str = f"#{r8:02x}{g8:02x}{b8:02x}"
                if pixel_data.to_int() > 0:
                    cells.append(f"[black on {color_as_str}]  [/]")
                else:
                    cells.append("[black on black]  [/]")
            table.add_row(*cells)
        return table

    def _print_data(self):
        new_screen = self._create_screen()
        self.live.update(new_screen)

    @staticmethod
    def rgbxxx_to_rgb888(pixel_data: Bits) -> Tuple[int, int, int]:
        """
        Convert pixel data to RGB888

        Args:
            pixel_data (Bits): pixel data (either 8 or 16 bits)

        Raises:
            NotImplementedError: raised if data are not 8 or 16 bits

        Returns:
            Tuple[int, int, int]: RGB (8 bits, 8 bits, 8 bits)
        """
        if len(pixel_data) == 8:
            red = pixel_data[:3]
            green = pixel_data[3:6]
            blue = pixel_data[6:]
            return Screen.rgb332_to_rgb888(red.to_int(), green.to_int(), blue.to_int())

        if len(pixel_data) == 16:
            red = pixel_data[:5]
            green = pixel_data[5:11]
            blue = pixel_data[11:]
            return Screen.rgb565_to_rgb888(red.to_int(), green.to_int(), blue.to_int())

        raise NotImplementedError(f"Screen cannot convert pixel data of size {len(pixel_data)} to RGB888")


    @staticmethod
    def rgb565_to_rgb888(red: int, green: int, blue: int) -> Tuple[float, float, float]:
        """
        Convert RGB565 to RGB888

        Args:
            red (int): red value as integer (5 bits)
            green (int): green value as integer (6 bits)
            blue (int): blue value as integer (5 bits)

        Returns:
            Tuple[int, int, int]: RGB (8 bits, 8 bits, 8 bits)
        """
        r = math.floor((red * 255 + 15) / 31)
        g = math.floor((green * 255 + 31) / 63)
        b = math.floor((blue * 255 + 15) / 31)

        return r, g, b

    @staticmethod
    def rgb332_to_rgb888(red: int, green: int, blue: int) -> Tuple[float, float, float]:
        """
        Convert RGB332 to RGB888

        Args:
            red (int): red value as integer (3 bits)
            green (int): green value as integer (3 bits)
            blue (int): blue value as integer (2 bits)

        Returns:
            Tuple[int, int, int]: RGB (8 bits, 8 bits, 8 bits)
        """
        r = math.floor((red * 255 + 3) / 7)
        g = math.floor((green * 255 + 3) / 7)
        b = math.floor((blue * 255 + 1) / 3)

        return r, g, b

    def stop(self):
        """
        Stops the thread properly.
        """
        self._stop_event.set()
