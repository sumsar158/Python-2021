"""Testing solutions part 2."""
import pytest
from solution import students_study, lottery


def test_part1_must_sleep_min_without_coffee():
    """Test function 1 must be sleep between 1 and 5, with coffee."""
    time = range(1, 5)
    coffee_needed = False
    for t in time:
        res = students_study(t, coffee_needed)
    studying = False
    assert studying == res


def test_part1_must_sleep_with_coffee():
    """Test function 1 must be sleep between 1 and 5, without coffee."""
    time = range(1, 5)
    coffee_needed = True
    for t in time:
        res = students_study(t, coffee_needed)
    studying = False
    assert studying == res


def test_part1_must_study_with_coffee():
    """Test function 1 must be studying between 18 and 25, without coffee."""
    time = range(18, 25)
    coffee_needed = True
    for t in time:
        res = students_study(t, coffee_needed)
    studying = True
    assert studying == res


def test_part1_must_study_without_coffee():
    """Test function 1 must be studying between 18 and 25, without coffee."""
    time = range(18, 25)
    coffee_needed = False
    for t in time:
        res = students_study(t, coffee_needed)
    studying = True
    assert studying == res


def test_part1_must_be_studying_day_with_coffee():
    """Test function 1 must be studying between 5 and 18, with coffee."""
    time = range(5, 18)
    coffee_needed = True
    for t in time:
        res = students_study(t, coffee_needed)
    studying = True
    assert studying == res


def test_part1_not_studying_day_without_coffee():
    """Test function 1 not studying between 5 and 18, without coffee."""
    time = range(5, 18)
    coffee_needed = False
    for t in time:
        res = students_study(t, coffee_needed)
    studying = False
    assert studying == res


def test_part2_all_numbers_5():
    """Winning must be 10 with all numbers being 5."""
    a, b, c = 5, 5, 5
    winnings = 10
    res = lottery(a, b, c)
    assert res == winnings


def test_part2_all_numbers_equal_positive():
    """Winning must be 5 with all numbers being same positive integers."""
    a, b, c = 8, 8, 8
    winnings = 5
    res = lottery(a, b, c)
    assert res == winnings


def test_part2_all_numbers_equal_negative():
    """Winning must be 5 with all numbers being same negative integers."""
    a, b, c = -2, -2, -2
    winnings = 5
    res = lottery(a, b, c)
    assert res == winnings


def test_part2_all_numbers_zero():
    """Winning must be 5 with all numbers being zero."""
    a, b, c = 0, 0, 0
    winnings = 5
    res = lottery(a, b, c)
    assert res == winnings


def test_part2_a_b_same_c_different():
    """Winning must be 0 with a and b being same and c different."""
    a, b, c = 3, 3, 7
    winnings = 0
    res = lottery(a, b, c)
    assert res == winnings


def test_part2_a_c_same_b_different():
    """Winning must be 0 with a and c being same and b different."""
    a, b, c = 4, 9, 4
    winnings = 0
    res = lottery(a, b, c)
    assert res == winnings


def test_part2_b_c_are_not_a():
    """Winning must be 1 with b and c being different from a."""
    a, b, c = 4, 5, 2
    winnings = 1
    res = lottery(a, b, c)
    assert res == winnings


def test_part2_b_c_same_a_different():
    """Winning must be 1 with b and c being different from a."""
    a, b, c = 4, 2, 2
    winnings = 1
    res = lottery(a, b, c)
    assert res == winnings


def test_part2_all_numbers_different():
    """Winning must be 0 while all numbers different."""
    a, b, c = 2, 7, 9
    winnings = 1
    res = lottery(a, b, c)
    assert res == winnings
