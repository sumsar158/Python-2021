# -*- coding: utf-8 -*-
"""ID code."""


def find_id_code(text: str) -> str:
    """
    Find ID-code from given text.

    Given string may include any number of numbers, characters and other symbols mixed together.
    The numbers of ID-code may be between other symbols - they must be found and concatenated.
    ID-code contains of exactly 11 numbers. If there are not enough numbers, return 'Not enough numbers!',
    if there are too many numbers, return 'Too many numbers!' If ID-code can be found, return that code.

    :param text: string
    :return: string
    """
    list_of_numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    id_code = []

    for letter in text:
        if letter in list_of_numbers:
            id_code.append(letter)
        else:
            continue

    if len(id_code) < 11:
        return "Not enough numbers!"
    elif len(id_code) > 11:
        return "Too many numbers!"

    return "".join(id_code)


def is_valid_gender_number(number: int) -> bool:
    """
    Check if given value is correct for gender number in ID code.

    :param number: int
    :return: boolean
    """
    if 0 < number < 7:
        return True
    else:
        return False


def get_gender(number: int) -> str:
    """
    Return id code persons gender based on input number.

    :param number: int
    :return: string 'female' or 'male'
    """
    female = [2, 4, 6]

    if is_valid_gender_number(number):
        if number in female:
            return "female"
        else:
            return "male"


def is_valid_year_number(year_number: int) -> bool:
    """
    Check if given value is correct for year number in ID code.

    :param year_number: int
    :return: boolean
    """
    if 100 > year_number > 0:
        return True
    else:
        return False


def is_valid_month_number(month_number: int) -> bool:
    """
    Check if given value is correct for month number in ID code.

    :param month_number: int
    :return: boolean
    """
    if 0 < month_number < 13:
        return True
    else:
        return False


def is_valid_birth_number(birth_number: int):
    """
    Check if given value is correct for birth number in ID code.

    :param birth_number: int
    :return: boolean
    """
    if 0 < birth_number < 1000:
        return True
    else:
        return False


def is_leap_year(year: int) -> bool:
    """
    Check if given value is a leap year.

    :param year: int
    :return: boolean
    """
    if year % 4 == 0 and year % 100 != 0:
        return True
    elif year % 400 == 0:
        return True
    else:
        return False


def get_birth_place(birth_number: int) -> str:
    """
    Find the place where the person was born.

    Possible locations are following: Kuressaare, Tartu, Tallinn, Kohtla-Järve, Narva, Pärnu,
    and undefined. Lastly if the number is incorrect the function must return
    the following 'Wrong input!'
    :param birth_number: int
    :return: str
    """
    if 0 < birth_number < 11:
        return "Kuressaare"
    elif 10 < birth_number < 21:
        return "Tartu"
    elif 20 < birth_number < 221:
        return "Tallinn"
    elif 220 < birth_number < 271:
        return "Kohtla-Järve"
    elif 270 < birth_number < 371:
        return "Tartu"
    elif 370 < birth_number < 421:
        return "Narva"
    elif 420 < birth_number < 471:
        return "Pärnu"
    elif 470 < birth_number < 711:
        return "Tallinn"
    elif 710 < birth_number < 1000:
        return "undefined"
    else:
        return 'Wrong input!'


def get_full_year(gender_number: int, year_number: int) -> int:
    """
    Define the 4-digit year when given person was born.

    Person gender and year numbers from ID code must help.
    Given year has only two last digits.

    :param gender_number: int
    :param year_number: int
    :return: int
    """
    year = ""

    if is_valid_year_number(year_number):
        if is_valid_gender_number(gender_number):
            if gender_number == 1 or gender_number == 2:
                year = "18"
            elif gender_number == 3 or gender_number == 4:
                year = "19"
            elif gender_number == 5 or gender_number == 6:
                year = "20"

    year_number = str(year_number)
    if len(year_number) < 2:
        year_number = "0" + year_number

    full_year = year + year_number
    full_year = int(full_year)

    return full_year


def is_valid_control_number(id_code: str) -> bool:
    """
    Check if given value is correct for control number in ID code.

    Use algorithm made for creating this number.

    :param id_code: string
    :return: boolean
    """
    pass


def is_valid_day_number(gender_number: int, year_number: int, month_number: int, day_number: int) -> bool:
    """
    Check if given value is correct for day number in ID code.

    Also, consider leap year and which month has 30 or 31 days.

    :param gender_number: int
    :param year_number: int
    :param month_number: int
    :param day_number: int
    :return: boolean
    """
    pass


def is_id_valid(id_code: str) -> bool:
    """
    Check if given ID code is valid and return the result (True or False).

    Complete other functions before starting to code this one.
    You should use the functions you wrote before in this function.
    :param id_code: str
    :return: boolean
    """
    pass


def get_data_from_id(id_code: str) -> str:
    """
    Get possible information about the person.

    Use given ID code and return a short message.
    Follow the template - This is a <gender> born on <DD.MM.YYYY> in <location>.
    :param id_code: str
    :return: str
    """
    pass


if __name__ == '__main__':

    print("\nYear number:")
    print(is_valid_year_number(100))  # -> False
    print(is_valid_year_number(50))  # -> true
    print(is_valid_year_number(1))  # -> true

    print("\nMonth number:")
    print(is_valid_month_number(2))  # -> True
    print(is_valid_month_number(15))  # -> False

    print("\nBorn order number:")
    print(is_valid_birth_number(0))  # -> False
    print(is_valid_birth_number(1))  # -> True
    print(is_valid_birth_number(850))  # -> True
