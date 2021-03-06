"""KT4."""


def two_digits_into_list(nr: int) -> list:
    """
    Return list of digits of 2-digit number.

    two_digits_into_list(11) => [1, 1]
    two_digits_into_list(71) => [7, 1]

    :param nr: 2-digit number
    :return: list of length 2
    """
    nr = str(nr)
    nr = list(nr)
    list_len_two = []
    for n in nr:
        n = int(n)
        list_len_two.append(n)
    return list_len_two


def sum_elements_around_last_three(nums: list) -> int:
    """
    Find sum of elements before and after last 3 in the list.

    If there is no 3 in the list or list is too short
    or there is no element before or after last 3 return 0.

    Note if 3 is last element in the list you must return
    sum of elements before and after 3 which is before last.

    sum_before_and_after_last_three([1, 3, 7]) -> 8
    sum_before_and_after_last_three([1, 2, 3, 4, 6, 4, 3, 4, 5, 3, 4, 5, 6]) -> 9
    sum_before_and_after_last_three([1, 2, 3, 4, 6, 4, 3, 4, 5, 3, 3, 2, 3]) -> 5
    sum_before_and_after_last_three([1, 2, 3]) -> 0

    :param nums: given list of ints
    :return: sum of elements before and after last 3
    """
    if 3 not in nums or len(nums) < 3:
        return 0
    if 3 == nums[-1] and 3 not in nums[0:-2]:
        return 0
    nums.reverse()
    for num in nums:
        if num == 3 and nums.index(num) != 0:
            print(nums.index(num))
            number_3_index = nums.index(num)
            print(nums[1])
            print(number_3_index - 1)
            return nums[number_3_index - 1] + nums[number_3_index + 1]
        else:
            continue
    return 0


def max_block(s: str) -> int:
    """
    Given a string, return the length of the largest "block" in the string.

    A block is a run of adjacent chars that are the same.

    max_block("hoopla") => 2
    max_block("abbCCCddBBBxx") => 3
    max_block("") => 0
    """
    temp_string = ""
    count = 0
    len_longest_string = 0

    if s == temp_string:
        return 0

    for letter in s:
        if letter == temp_string:
            count += 1
        else:
            count = 1
            temp_string = letter
        len_longest_string = max(count, len_longest_string)

    return len_longest_string


def create_dictionary_from_directed_string_pairs(pairs: list) -> dict:
    """
    Create dictionary from directed string pairs.

    One pair consists of two strings and "direction" symbol ("<" or ">").
    The key is the string which is on the "larger" side,
    the value is the string which is on the "smaller" side.

    For example:
    ab>cd => "ab" is the key, "cd" is the value
    kl<mn => "mn" is the key, "kl" is the value

    The input consists of list of such strings.
    The output is a dictionary, where values are lists.
    Each key cannot contain duplicate elements.
    The order of the elements in the values should be
    the same as they appear in the input list.

    create_dictionary_from_directed_string_pairs([]) => {}

    create_dictionary_from_directed_string_pairs(["a>b", "a>c"]) =>
    {"a": ["b", "c"]}

    create_dictionary_from_directed_string_pairs(["a>b", "a<b"]) =>
    {"a": ["b"], "b": ["a"]}

    create_dictionary_from_directed_string_pairs(["1>1", "1>2", "1>1"]) =>
    {"1": ["1", "2"]}
    """
    pass


if __name__ == '__main__':
    print(max_block("hoopla"))
    print(max_block("abbCCCddBBBxx"))
    print(max_block(""))
