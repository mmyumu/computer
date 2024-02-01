from computer.accumulator import Accumulator
from computer.alu import ALU
from computer.alu_buffer import AluBuffer
from computer.clock import Clock
from computer.control_unit import ControlUnit
from computer.in_port import InPort
from computer.out_port import OutPort
from computer.program_counter import ProgramCounter
from computer.ram import RAM
from computer.rom import ROM


class CPU:
    def __init__(self, memory_size, clock_frequency):
        self.program_counter = ProgramCounter()
        self.rom = ROM(memory_size)
        self.ram = RAM(memory_size)
        self.control_unit = ControlUnit()
        self.alu = ALU()
        self.accumulator = Accumulator()
        self.alu_buffer = AluBuffer()
        self.in_port = InPort()
        self.out_port = OutPort()
        self.clock = Clock(clock_frequency)

    def load_program(self, program):
        self.rom.load_program(program)

    def run(self):
        try:
            while True:  # Continue until a HALT instruction is encountered or end of program is reached
                self.clock.wait_cycle()

                # Fetch instruction
                self.control_unit.fetch_instruction(self.rom, self.program_counter)
                opcode, operand = self.control_unit.decode_instruction()
                
                # Execute instruction
                if opcode == 0b000:  # Example opcode for a HALT instruction
                    break  # Exit the loop, stopping the program
                elif opcode == 0b001:  # LOAD from RAM
                    address = operand  # Assuming the operand is an address in RAM
                    value = self.ram.read(address)
                    self.accumulator.load(value)
                elif opcode == 0b010:  # Example opcode for an ADD instruction
                    self.alu_buffer.load(self.accumulator.read())
                    result = self.alu.add(self.alu_buffer.read(), operand)
                    self.accumulator.write(result)
                elif opcode == 0b011:  # WRITE to RAM
                    address = operand  # Assuming the operand is an address in RAM
                    self.ram.write(address, self.accumulator.read())
                if opcode == 0b100:  # READ from InPort
                    value = operand
                    data = self.in_port.read_data(value)
                    self.accumulator.load(data)
                elif opcode == 0b101:  # WRITE to OutPort
                    data = self.accumulator.read()
                    self.out_port.write_data(data)
                # ... other opcodes and instructions
                
                # Increment the program counter
                self.program_counter.increment()
        
        except IndexError:
            # Handle the exception if trying to read instruction outside ROM bounds
            print("Attempted to execute instruction outside program memory.")

    def print_ram(self):
        self.ram.print()

if __name__ == "__main__":
    # Example usage
    cpu = CPU(memory_size=64, clock_frequency=10)  # Create a CPU with a ROM size of 64 and clock frequency of 1Hz
    # program = [0b00100000, 0b01000001, 0b01100000, 0b00000000]  # Programme avec LOAD, ADD, OutPort, HALT
    program = [
        0b10000010, # Read 2 from InPort
        0b01101000, # Write to RAM in Address 8
        0b10000100, # Read 4 from InPort
        0b01110000, # Write to RAM in Address 16
        0b00101000, # Load from RAM in Address 8
        0b01000001, # ADD 1
        0b01100001, # Write to RAM in Address 1
        0b10100000, # Write to OutPort

    ]
    cpu.load_program(program)
    cpu.run()
    cpu.print_ram()
