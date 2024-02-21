"""
Test for Bitwise operations
"""
import pytest
from computer.data_types import Bits
from computer.electronic.circuits.bitwise import BitwiseAdd, BitwiseDiv, BitwiseMult, BitwiseSub

# pylint: disable=C0116

@pytest.fixture(name="bitwise_add")
def fixture_bitwise_add():
    return BitwiseAdd(4)

@pytest.fixture(name="bitwise_sub")
def fixture_bitwise_sub():
    return BitwiseSub(4)

# @pytest.fixture(name="bitwise_sub_restore")
# def fixture_bitwise_sub_restore():
#     return BitwiseSubRestore(4)

@pytest.fixture(name="bitwise_mult")
def fixture_bitwise_mult():
    return BitwiseMult(4)

@pytest.fixture(name="bitwise_div")
def fixture_bitwise_div():
    return BitwiseDiv(4)


def test_bitwise_add(bitwise_add: BitwiseAdd):
    for d1 in range(2 ** 2):
        for d2 in range(2 ** 2):
            for carry in [False, True]:
                data1 = Bits(d1, size=2 ** 2)
                data2 = Bits(d2, size=2 ** 2)
                add_result, carry_out = bitwise_add(data1, data2, carry)

                assert add_result.to_int() == d1 + d2 + carry
                assert carry_out is False

def test_bitwise_sub(bitwise_sub: BitwiseSub):
    for d1 in range(2 ** 2):
        for d2 in range(2 ** 2):
            data1 = Bits(d1, size=2 ** 2)
            data2 = Bits(d2, size=2 ** 2)
            difference_result, borrow_out = bitwise_sub(data1, data2)

            if d1 < d2:
                assert difference_result.to_int() == (d1 - d2) + 2 ** 4, f"Inputs: d1={d1}, d2={d2}"
                assert borrow_out is True, f"Inputs: d1={d1}, d2={d2}"
            else:
                assert difference_result.to_int() == d1 - d2, f"Inputs: d1={d1}, d2={d2}"
                assert borrow_out is False, f"Inputs: d1={d1}, d2={d2}"

# def test_bitwise_sub_restore(bitwise_sub_restore: BitwiseSubRestore):
#     for d1 in range(2 ** 2):
#         for d2 in range(2 ** 2):
#             data1 = Bits(d1, size=2 ** 2)
#             data2 = Bits(d2, size=2 ** 2)
#             difference_result, carry_out = bitwise_sub_restore(data1, data2)

#             if d1 < d2:
#                 assert difference_result.to_int() == (d1 - d2) + 2 ** 4, f"Inputs: d1={d1}, d2={d2}"
#                 assert carry_out is False, f"Inputs: d1={d1}, d2={d2}"
#             else:
#                 assert difference_result.to_int() == d1 - d2, f"Inputs: d1={d1}, d2={d2}"
#                 assert carry_out is True, f"Inputs: d1={d1}, d2={d2}"
#             print(f"d1={d1}, d2={d2}, carry_out={carry_out}")

def test_bitwise_mult(bitwise_mult: BitwiseMult):
    for d1 in range(2 ** 2):
        for d2 in range(2 ** 2):
            data1 = Bits(d1, size=2 ** 2)
            data2 = Bits(d2, size=2 ** 2)
            mult_result = bitwise_mult(data1, data2)

            assert mult_result.to_int() == d1 * d2

def test_bitwise_div(bitwise_div: BitwiseDiv):
    for d1 in range(2 ** 2):
        for d2 in range(2 ** 2):
            data = Bits(d1, size=2 ** 2)
            divider = Bits(d2, size=2 ** 2)

            if d2 == 0:
                with pytest.raises(ValueError):
                    quotient, remainder = bitwise_div(data, divider)
            else:
                quotient, remainder = bitwise_div(data, divider)

                assert quotient.to_int() == (d1 // d2)
                assert remainder.to_int() == d1 % d2
