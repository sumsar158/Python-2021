"""EX08 - Testimine (2)."""


def students_study(time: int, coffee_needed: bool) -> bool:
    """
    Return True if students study in given circumstances.

    (19, False) -> True
    (1, True) -> False.
    """
    studying = False

    if time in range(18, 25):
        studying = True
    if time in range(5, 18) and coffee_needed:
        studying = True
    if time in range(5, 18) and coffee_needed is False:
        studying = False
    if time in range(1, 5):
        studying = False

    return studying


def lottery(a: int, b: int, c: int) -> int:
    """
    Return Lottery victory result 10, 5, 1, or 0 according to input values.

    (5, 5, 5) -> 10
    (2, 2, 1) -> 0
    (2, 3, 1) -> 1
    """
    if a == 5 and b == a and c == b:
        return 10
    if a == b and b == c and c != 5:
        return 5
    if b != a and c != a and a != b:
        return 1
    if c == a or b == a:
        return 0


def fruit_order(small_baskets: int, big_baskets: int, ordered_amount: int) -> int:
    """
    Return number of small fruit baskets if it's possible to finish the order, otherwise return -1.

    (4, 1, 9) -> 4
    (3, 1, 10) -> -1
    """
    pass


if __name__ == '__main__':
    print(lottery(2, 7, 9))
    print(lottery(2, 2, 1))
    print(lottery(5, 5, 5))


"""
test_solve_test[lottery__all_same_positive]
AssertionError: assert ( == 0) == False	
FAILED

84	2
test_solve_test[lottery__all_same_negative]
AssertionError: assert ( == 0) == False	
FAILED

81	2
test_solve_test[lottery__all_same_zero]
AssertionError: assert ( == 0) == False	
FAILED

81	2
test_solve_test[lottery__a_b_same_c_diff]
AssertionError: assert ( == 0) == False	
FAILED

80	2
test_solve_test[lottery__a_c_same_b_diff]
AssertionError: assert ( == 0) == False	
FAILED

80	2
test_solve_test[lottery__b_c_same_a_diff]
AssertionError: assert ( == 0) == False	
FAILED

136	2
test_solve_test[lottery__all_diff]
AssertionError: assert ( == 0) == False
"""