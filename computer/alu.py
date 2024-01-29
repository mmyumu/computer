class ALU:
    def __init__(self):
        self.zero_flag = False

    def perform_operation(self, opcode, operand_a, operand_b=None):
        # Executes an operation based on the opcode and operands
        result = None
        if opcode == 0:  # Example for an ADD operation
            result = operand_a + (operand_b if operand_b is not None else 0)
        elif opcode == 1:  # Example for a SUBTRACT operation
            result = operand_a - (operand_b if operand_b is not None else 0)
        # ... other operations based on opcodes

        # Update the zero flag if the result is 0
        self.zero_flag = (result == 0)

        return result

    def add(self, operand_a, operand_b):
        return self.perform_operation(0, operand_a, operand_b)

    def subtract(self, operand_a, operand_b):
        return self.perform_operation(1, operand_a, operand_b)

    # ... other arithmetic and logic functions
