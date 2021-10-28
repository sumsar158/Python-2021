"""Testing solutions part 2."""
import pytest
from solution import students_study


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
