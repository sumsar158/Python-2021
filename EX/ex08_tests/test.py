"""Testing ex4."""
import pytest
import solution
# def test_data_types():
#     """Test function1 with all data type inputs and correct length."""
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
    """Test function with input 0."""
    input_amount = 0
    res = solution.generate_list(input_amount, "int")
    expected_len = 0
    assert len(res) == expected_len


def test_part1_input_hundred():
    """Test function with input 100."""
    input_amount = 100
    res = solution.generate_list(input_amount, "int")
    expected_len = 100
    assert len(res) == expected_len


def test_part1_int_correct_content_and_len():
    """Test function with input integer and correct length."""
    input_amount = 5
    res = solution.generate_list(input_amount, "int")
    expected_len = 5
    assert len(res) == expected_len
    for element in res:
        assert isinstance(element, int)


def test_part1_float_content_and_len():
    """Test function with input float and correct length."""
    input_amount = 5
    res = solution.generate_list(input_amount, "float")
    expected_len = 5
    assert len(res) == expected_len
    for element in res:
        assert isinstance(element, float)


def test_part1_string_content_and_len():
    """Test function with input string and correct length."""
    input_amount = 5
    res = solution.generate_list(input_amount, "string")
    expected_len = 5
    assert len(res) == expected_len
    for element in res:
        assert isinstance(element, str)


def test_part1_list_content_and_len():
    """Test function with input list and correct length."""
    input_amount = 5
    res = solution.generate_list(input_amount, "list")
    expected_len = 5
    assert len(res) == expected_len
    for element in res:
        assert isinstance(element, list)


def test_part1_dict_content_and_len():
    """Test function with input dictionary and correct length."""
    input_amount = 5
    res = solution.generate_list(input_amount, "dict")
    expected_len = 5
    assert len(res) == expected_len
    for element in res:
        assert isinstance(element, dict)


def test_part1_tuple_content_and_len():
    """Test function with input tuple and correct length."""
    input_amount = 5
    res = solution.generate_list(input_amount, "tuple")
    expected_len = 5
    assert len(res) == expected_len
    for element in res:
        assert isinstance(element, tuple)


def test_part1_set_content_and_len():
    """Test function with input set and correct length."""
    input_amount = 5
    res = solution.generate_list(input_amount, "set")
    expected_len = 5
    assert len(res) == expected_len
    for element in res:
        assert isinstance(element, set)


def test_part2_len_small():
    """Test function with small integer."""
    input_amount = [(1, 'int')]
    res = solution.generate_combined_list(input_amount)
    expected_len = 1
    assert len(res) == expected_len


def test_part2_len_zero():
    """Test function with input 0."""
    input_amount = [(0, 'int')]
    res = solution.generate_combined_list(input_amount)
    expected_len = 0
    assert len(res) == expected_len


def test_part2_len_big():
    """Test function with big integer."""
    input_amount = [(100, 'int')]
    res = solution.generate_combined_list(input_amount)
    expected_len = 100
    assert len(res) == expected_len


def test_part2_len_float():
    """Test function2 with input float and correct length."""
    input_amount = [(5, 'float')]
    res = solution.generate_combined_list(input_amount)
    expected_len = 5
    assert len(res) == expected_len
    for element in res:
        assert isinstance(element, float)


def test_part2_len_string():
    """Test function2 with input string and correct length."""
    input_amount = [(5, 'string')]
    res = solution.generate_combined_list(input_amount)
    expected_len = 5
    assert len(res) == expected_len
    for element in res:
        assert isinstance(element, str)


def test_part2_len_list():
    """Test function2 with input list and correct length."""
    input_amount = [(5, 'list')]
    res = solution.generate_combined_list(input_amount)
    expected_len = 5
    assert len(res) == expected_len
    for element in res:
        assert isinstance(element, list)


def test_part3_len_int():
    """Test function3 with input of unique integers and correct length."""
    input_amount = [(5, 'int')]
    list_of_integers_in_list = []
    res = solution. generate_combined_list_unique(input_amount)
    expected_len = 5
    assert len(res) == expected_len
    for element in res:
        assert isinstance(element, int)
        if element not in list_of_integers_in_list:
            list_of_integers_in_list.append(element)
        if element in list_of_integers_in_list:
            assert "fount duplicate integers"


def test_part3_len_small():
    """Test function3 length with small integer."""
    input_amount = [(1, 'int')]
    res = solution.generate_combined_list_unique(input_amount)
    expected_len = 1
    assert len(res) == expected_len


def test_part3_len_zero():
    """Test function3 length with input 0."""
    input_amount = [(0, 'str')]
    res = solution.generate_combined_list_unique(input_amount)
    expected_len = 0
    assert len(res) == expected_len


def test_part3_len_big():
    """Test function3 length with big integer."""
    input_amount = [(100, 'float')]
    res = solution.generate_combined_list_unique(input_amount)
    expected_len = 100
    assert len(res) == expected_len
