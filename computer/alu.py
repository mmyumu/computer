from utils.logger import logger

class ALU:
    def __init__(self):
        self.zero_flag = False

    def add(self, operand_a, operand_b):
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
        self.zero_flag = (result == 0)

        return result

    def subtract(self, operand_a, operand_b):
        # Soustraction en utilisant l'addition avec le complément à deux
        return self.add(operand_a, self.twos_complement(operand_b))

    def and_operation(self, operand_a, operand_b):
        # Opération logique AND
        return operand_a & operand_b

    def or_operation(self, operand_a, operand_b):
        # Opération logique OR
        return operand_a | operand_b

    def xor_operation(self, operand_a, operand_b):
        # Opération logique XOR
        return operand_a ^ operand_b

    def shift_left(self, operand, n):
        # Décalage des bits vers la gauche
        return operand << n

    def shift_right(self, operand, n):
        # Décalage des bits vers la droite
        return operand >> n

    def twos_complement(self, operand):
        # Calcul du complément à deux pour la soustraction
        return self.add(~operand, 1)

if __name__ == "__main__":
    alu = ALU()

    res = alu.add(0b1111, 0b10100)
    logger.info(f"Addition: {bin(res)} -> {res}")               # 15 + 20

    res = alu.subtract(0b11110, 0b1010)
    logger.info(f"Subtraction: {bin(res)} -> {res}")       # 30 - 10

    res = alu.and_operation(0b1100, 0b110)
    logger.info(f"AND operation: {bin(res)} -> {res}")  # 12 & 6

    res = alu.or_operation(0b1100, 0b110)
    logger.info(f"OR operation: {bin(res)} -> {res}")    # 12 | 6

    res = alu.xor_operation(0b1100, 0b110)
    logger.info(f"XOR operation: {bin(res)} -> {res}")  # 12 ^ 6

    res = alu.shift_left(0b1100, 2)
    logger.info(f"Shift left: {bin(res)} -> {res}")            # 12 << 2

    res = alu.shift_right(0b1100, 2)
    logger.info(f"Shift right: {bin(res)} -> {res}")          # 12 >> 2
