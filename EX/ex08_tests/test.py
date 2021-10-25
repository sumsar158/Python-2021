import pytest
import solution


def test_data_types():
    data_types = {"int": int, "float": float, "string": str, "list": list, "tuple": tuple, "dict": dict, "set": set}
    for key, value in data_types.items():
        res = solution.generate_list(5, key)
        for element in res:
            assert isinstance(element, value)


def test_part1_input_zero():
    input_amount = 0
    res = solution.generate_list(input_amount, "int")
    expected_len = 0
    assert len(res) == expected_len
