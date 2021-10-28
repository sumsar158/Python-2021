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
