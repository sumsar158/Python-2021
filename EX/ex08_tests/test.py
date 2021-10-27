import pytest
import solution


# def test_data_types():
#     data_types = {"int": int, "float": float, "string": str, "list": list, "tuple": tuple, "dict": dict, "set": set}
#     input_amount = 5
#     expected_len = 5
#     for key, value in data_types.items():
#         res = solution.generate_list(input_amount, key)
#         assert expected_len == len(res)
#         for element in res:
#             assert isinstance(element, value)
#

def test_part1_input_zero():
    input_amount = 0
    res = solution.generate_list(input_amount, "int")
    expected_len = 0
    assert len(res) == expected_len


def test_part1_input_hundred():
    input_amount = 100
    res = solution.generate_list(input_amount, "int")
    expected_len = 100
    assert len(res) == expected_len


def test_part1_int_correct_content_and_len():
    input_amount = 5
    res = solution.generate_list(input_amount, "int")
    expected_len = 5
    assert len(res) == expected_len
    for element in res:
        assert isinstance(element, int)


def test_part1_float_content_and_len():
    input_amount = 5
    res = solution.generate_list(input_amount, "float")
    expected_len = 5
    assert len(res) == expected_len
    for element in res:
        assert isinstance(element, float)


def test_part1_string_content_and_len():
    input_amount = 5
    res = solution.generate_list(input_amount, "string")
    expected_len = 5
    assert len(res) == expected_len
    for element in res:
        assert isinstance(element, str)


def test_part1_list_content_and_len():
    input_amount = 5
    res = solution.generate_list(input_amount, "list")
    expected_len = 5
    assert len(res) == expected_len
    for element in res:
        assert isinstance(element, list)


def test_part1_dict_content_and_len():
    input_amount = 5
    res = solution.generate_list(input_amount, "dict")
    expected_len = 5
    assert len(res) == expected_len
    for element in res:
        assert isinstance(element, dict)


def test_part1_tuple_content_and_len():
    input_amount = 5
    res = solution.generate_list(input_amount, "tuple")
    expected_len = 5
    assert len(res) == expected_len
    for element in res:
        assert isinstance(element, tuple)


def test_part1_set_content_and_len():
    input_amount = 5
    res = solution.generate_list(input_amount, "set")
    expected_len = 5
    assert len(res) == expected_len
    for element in res:
        assert isinstance(element, set)


def test_part2_len_small():
    input_amount = [(2, 'int')]
    res = solution.generate_combined_list(input_amount)
    expected_len = 2
    assert len(res) == expected_len


def test_part2_len_zero():
    input_amount = [(0, 'int')]
    res = solution.generate_combined_list(input_amount)
    expected_len = 0
    assert len(res) == expected_len

def test_part2_len_big():
    input_amount = [(100, 'int')]
    res = solution.generate_combined_list(input_amount)
    expected_len = 100
    assert len(res) == expected_len
