"""
Main module to run simulation
"""
import argparse

from computer.system import System
from guignol.interpreter import Interpreter
from utils.logger import logger


def main():
    """
    Main function to run the simulation
    """
    parser = argparse.ArgumentParser()
    parser.add_argument("program", type=str, help="the path of the program to run")
    parser.add_argument("--embedded-screen", action='store_true', help="starts the embedded screen with the system")
    parser.add_argument("--screen-refresh-rate", type=int, help="refresh rate of the embedded screen")

    args = parser.parse_args()

    if args.embedded_screen:
        logger.disabled = True

    interpreter = Interpreter()
    program = interpreter(args.program, from_file=True)

    system = System(embedded_screen=args.embedded_screen, screen_refresh_rate=args.screen_refresh_rate, **program.requirements.get_kwargs_dict())
    system.load_rom(program.binary_program)
    system.turn_on()

if __name__ == "__main__":
    main()
