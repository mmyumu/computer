"""
Data types module.
It contains several data types used in simulation for code clarity.
"""
class Bits(list):
    """
    Class to store bits values of given size
    """
    BITS_NUMBER = 2

    def __init__(self, *bits):
        if len(bits) == 1 and isinstance(bits[0], int):
            bool_list = self._int_to_bool(bits[0])
        elif isinstance(bits, (list, tuple)):
            bool_list = bits
        super().__init__(bool_list)

    @classmethod
    def from_bin(cls, binary: int):
        """
        Create Opcode from binary value
        """
        bool_list = cls._int_to_bool(binary)
        return cls(*bool_list)

    @classmethod
    def _int_to_bool(cls, binary: int):
        if binary >= 2 ** cls.BITS_NUMBER:
            raise ValueError(f"Binary value {binary} cannot be represented with {cls.BITS_NUMBER} bits.")
        return [(binary >> i) & 1 == 1 for i in range(cls.BITS_NUMBER - 1, -1, -1)]

    def _bits_to_int(self):
        return sum(val * (2 ** idx) for idx, val in enumerate(reversed(self)))

    def __str__(self) -> str:
        list_str = super().__str__()
        as_int = self._bits_to_int()
        return f"{list_str}: (int: {as_int}), (bin: {bin(as_int)})"


class Address2(Bits):
    """
    Class to store an address of 2 bits
    """
    BITS_NUMBER = 2


class Address10(Bits):
    """
    Class to store an address of 10 bits
    """
    BITS_NUMBER = 10


class Address16(Bits):
    """
    Class to store an address of 16 bits
    """
    BITS_NUMBER = 16


class Data4(Bits):
    """
    Class to store a data of 4 bits
    """
    BITS_NUMBER = 4


class Opcode8(Bits):
    """
    Class to store opcode on 8 bits
    """
    BITS_NUMBER = 8


class Operand18(Bits):
    """
    Class to store operand on 24 bits
    """
    BITS_NUMBER = 18


class Operand24(Bits):
    """
    Class to store operand on 24 bits
    """
    BITS_NUMBER = 24
