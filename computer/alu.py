"""
ALU (Arithmetic Lgic Unit) module
"""
from utils.logger import logger

class ALU:
    """
    ALU (Arithmetic Logic Unit) class: performs arithmetic operations
    """
    def __init__(self):
        self.zero_flag = False

    def add(self, operand_a, operand_b):
        """
        Add operand A and B
        """
        # Initialisation du résultat et de la retenue
        result = 0
        carry = 0
        for i in range(32):  # Assumons un CPU 32 bits pour cet exemple
            a = (operand_a >> i) & 1
            b = (operand_b >> i) & 1

            # Opération de l'additionneur complet
            sum_bit = a ^ b ^ carry
            carry = (a & b) | (b & carry) | (carry & a)

            # Ajout du bit calculé au résultat
            result |= sum_bit << i

        # Mise à jour du zero flag
        self.zero_flag = result == 0

        return result

    def subtract(self, operand_a, operand_b):
        """
        Substract operand A and B
        """
        return self.add(operand_a, self.twos_complement(operand_b))

    def and_operation(self, operand_a, operand_b):
        """
        AND between A and B
        """
        return operand_a & operand_b

    def or_operation(self, operand_a, operand_b):
        """
        OR between A and B
        """
        return operand_a | operand_b

    def xor_operation(self, operand_a, operand_b):
        """
        XOR operation between A and B
        """
        return operand_a ^ operand_b

    def shift_left(self, operand, n):
        """
        Shift left n bits the input
        """
        return operand << n

    def shift_right(self, operand, n):
        """
        Shift right n bits the input
        """
        # Décalage des bits vers la droite
        return operand >> n

    def twos_complement(self, operand):
        """
        Two complement of input
        """
        return self.add(~operand, 1)

if __name__ == "__main__":
    alu = ALU()

    RES = alu.add(0b1111, 0b10100)
    logger.info(f"Addition: {bin(RES)} -> {RES}")               # 15 + 20

    RES = alu.subtract(0b11110, 0b1010)
    logger.info(f"Subtraction: {bin(RES)} -> {RES}")       # 30 - 10

    RES = alu.and_operation(0b1100, 0b110)
    logger.info(f"AND operation: {bin(RES)} -> {RES}")  # 12 & 6

    RES = alu.or_operation(0b1100, 0b110)
    logger.info(f"OR operation: {bin(RES)} -> {RES}")    # 12 | 6

    RES = alu.xor_operation(0b1100, 0b110)
    logger.info(f"XOR operation: {bin(RES)} -> {RES}")  # 12 ^ 6

    RES = alu.shift_left(0b1100, 2)
    logger.info(f"Shift left: {bin(RES)} -> {RES}")            # 12 << 2

    RES = alu.shift_right(0b1100, 2)
    logger.info(f"Shift right: {bin(RES)} -> {RES}")          # 12 >> 2
