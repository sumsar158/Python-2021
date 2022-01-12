"""Exam 3 (2022-01-12)."""


def count_camel_case_words(text: str) -> int:
    """
    Count the words in the text.

    The text uses camel case. There are no spaces between words.
    Each new word starts with a capital letter.
    The first word can start with a small or a capital letter.

    count_camel_case_words("hello") => 1
    count_camel_case_words("") => 0
    count_camel_case_words("helloWorld") => 2
    count_camel_case_words("HelloWorld") => 2
    count_camel_case_words("aBC") => 3
    count_camel_case_words("ABC") => 3
    count_camel_case_words("a") => 1
    count_camel_case_words("What") => 1
    """
    if text == "":
        return 0

    if text[0].isupper():
        x = 0
    else:
        x = 1

    for letter in text:
        if letter.isupper():
            x += 1
    return x


def odd_index_sum(nums: list) -> int:
    """
    Find sum of elements with odd indices.

    odd_index_sum([1, 2, 3]) => 2
    odd_index_sum([]) => 0
    odd_index_sum([1]) => 0
    odd_index_sum([2, 3]) => 3
    odd_index_sum([0, -1, -4, -3]) => -4
    """
    if len(nums) < 2:
        return 0

    return sum(nums[1::2])


def encode_string_with_hex_key(input_str: str, key: str) -> str:
    """
    Encode string using key.

    :param input_str - string to encode. Non-alphabetic characters are left as is.
    Caps are encoded into caps.
    :param key - hex key in which n-th number tells how much should n-th char in input_str be shifted.
    Works as round buffer, eg. if z is reached start from a again.
    The input_str and key are always the same length.

    encode_string("a", "1") -> "b"
    encode_string("z", "1") -> "a"
    encode_string("abc", "101") -> "bbd"
    encode_string("z.z.z", "fffff") -> "o.o.o"

    :return Encoded string
    """
    hex = (1, 2, 3, 4, 5, 6, 7, 8, 9, "a", "b", "c", "d", "e", "f")
    encoded_string = ""
    pass


def who_gets_gingerbread(students: dict, total_gingerbreads: int) -> dict:
    """
    How many gingerbread students get.

    Given a dictionary of students with their average score and amount of gingerbreads that shows
    how many gingerbreads elves are about to share between students. However, elves have some conditions how to
    they are sharing gingerbreads - students with average score with or below 2.0 don't get any and should not appear in
    result dictionary and student with the highest average starts getting gingerbreads first.

    Return the dictionary of students with amount of gingerbreads they got from elves.

    Examples:
    students = {
        'Mart': 4.0,
        'Kristi': 4.5,
        'Kevin': 3.2,
        'Markus': 2.0
    }
    total_gingerbreads = 11

    The order of the students: Kristi, Mart, Kevin. Markus is left out due to the average grade 2.0.

    result =>
    {
        'Kristi': 4
        'Mart': 4
        'Kevin': 3
    }

    :param students: dict of students with their aberage score
    :param total_gingerbreads: number of gingerbreads that elves have
    :return: dict of students with amount of gingerbreads they got
    """
    for k, v in students.items():
        if v <= 2.0:
            del k
            print(students)
    return students
    pass


def fuel_calculator(fuel: int) -> int:
    """
    Find needed amount of fuel for a given mass.

    Amount of fuel needed = mass divided by three, rounded down, subtract two
    + fuel needed for the fuel itself
    + fuel needed for the fuel's fuel + etc.

    Negative fuel rounds to zero.

    Examples:
    fuel_calculator(10) -> 1 + 0 = 1
    fuel_calculator(151) -> 48 + 14 + 2 + 0 = 64
    """
    pass


def make_table(n: int) -> str:
    r"""
    Given an odd integer n, return a n*n table like shown in the examples.

    The given n is more or equal to 7.

    Example 1:
    n=15
    result:

    \#####/|\#####/
    #\###/#|#\###/#
    ##\#/##|##\#/##
    ###X###|###X###
    ##/#\##|##/#\##
    #/###\#|#/###\#
    /#####\|/#####\
    -------+-------
    \#####/|\#####/
    #\###/#|#\###/#
    ##\#/##|##\#/##
    ###X###|###X###
    ##/#\##|##/#\##
    #/###\#|#/###\#
    /#####\|/#####\

    Example 2:
    n=7
    result:

    \#/|\#/
    #X#|#X#
    /#\|/#\
    ---+---
    \#/|\#/
    #X#|#X#
    /#\|/#\

    Example 3:
    n=9
    result:

    \##/|\##/
    #\/#|#\/#
    #/\#|#/\#
    /##\|/##\
    ----+----
    \##/|\##/
    #\/#|#\/#
    #/\#|#/\#
    /##\|/##\

    """
    pass


STUDENTS = []


class Student:
    """Represent student model."""

    def __init__(self, name: str, gpa: float, age: int):
        """
        Class constructor.

        Each student has name and gpa (Grade Point Average).

        :type name: object
        :param name: student's name
        :param gpa: student's gpa
        :param age: student's age
        """
        self.age = age
        self.gpa = gpa
        self.name = name

    def __repr__(self):
        return self.name


class University:
    """Represent university model."""

    def __init__(self, name: str, gpa_required: float):
        """
        Class constructor.

        Each university has name and gpa_required.

        University should also have a database to keep and track all students.
        :param name: university name
        :param gpa_required: university required gpa
        """
        self.gpa_required = gpa_required
        self.name = name
        self.ENROLLED_STUDENTS = []

    def can_enroll_student(self, student: Student) -> bool:
        """
        Check if student can be enrolled to university.

        Student can be successfully enrolled if:
            * he/she has required gpa (>=)
            * he/she is not already enrolled to this university
            * he/she is at least 16 years old
            * additionally, if student's name characters length is
            exactly 13 -> student can be added to university despite gpa (though still should not be
            already present in university and be younger)
        If the student cannot be enrolled, returns False. Otherwise returns True.

        :return: bool
        """
        if student.gpa >= self.gpa_required:
            if student not in self.ENROLLED_STUDENTS:
                if student.age >= 16:
                    return True

        if len(student.name) == 13:
            if student not in self.ENROLLED_STUDENTS:
                if student.age >= 16:
                    return True

        return False

    def enroll_student(self, student: Student):
        """
        Enroll new student to university if possible.

        Before enrolling, you have to check whether student can be enrolled.

        :param student: Student
        Function does not return anything
        """
        if self.can_enroll_student(student=student):
            self.ENROLLED_STUDENTS.append(student)

    def can_unenroll_student(self, student: Student) -> bool:
        """
        Check if student can leave from university.

        Student can be successfully leave if he/she actually studies in this university.

        Returns True, if the student can be unenrolled, False otherwise.

        :return: bool
        """
        return student in self.ENROLLED_STUDENTS

    def unenroll_student(self, student: Student):
        """
        Unenroll student from University if possible.

        Before unenrolling, you have to make sure the student can be unenrolled.
        Function does not return anything
        """
        if self.can_unenroll_student(student):
            self.ENROLLED_STUDENTS.remove(student)

    def get_students(self) -> list:
        """
        Return a list of all students in current university.

        :return: list of Student objects
        """
        return self.ENROLLED_STUDENTS

    def get_student_highest_gpa(self) -> list:
        """
        Return a list of students (student) with the highest gpa.

        :return: list of Student objects
        """
        highest_gpa = []
        x = 0
        for student in self.ENROLLED_STUDENTS:
            if student.gpa > x:
                x = student.gpa
        for student in self.ENROLLED_STUDENTS:
            if student.gpa == x:
                highest_gpa.append(student)

        if len(highest_gpa) < 1:
            return None
        return highest_gpa


class Accessory:
    """Accessory."""

    def __init__(self, name: str, value: int):
        """Constructor."""
        pass

    def __repr__(self):
        """
        String representation of accessory.

        Returns string in form "{name}, value : {value}."
        """
        pass


class Car:
    """Car."""

    def __init__(self, name: str, color: str):
        """Constructor."""
        pass

    def add_accessory(self, accessory: Accessory):
        """Add accessory to the car."""
        pass

    def get_value(self) -> int:
        """
        Get the value of the car.

        Regular car base price is 9500, for premium car its 42 500.
        All the values of accessories are summed up.
        """
        pass

    def get_fuel_left(self):
        """Return how much fuel is left in percentage."""
        pass

    def get_accessories_by_value(self):
        """Return accessories sorted by value (descending i.e. higher to lower)."""
        pass

    def __repr__(self):
        """
        String representation of the car.

        Should return "This {color} {name} contains {accessory_amount} accessories and has {fuel}% fuel left."
        """
        pass


class Customer:
    """Customer."""

    def __init__(self, name: str, wish: str):
        """
        Constructor.

        The wish consists of two words.
        The first word is either "Cheap" or "Expensive".
        In case of "Cheap", the customer wants to get the car with the lowest value.
        In case of "Expensive", the customer wants to get the car with the highest value.
        The second word is the color. Customer does not want a car with another color.
        For premium customer a car with the given color is searched for from the premium cars.
        If there is no such car with the wished color, the cheapest car is taken from the premium cars.

        For example: "Cheap Red", "Expensive Yellow".
        """
        pass

    def get_garage(self):
        """
        Return all the cars of the customer sorted by the value (ascending i.e. from lower to higher).

        Both regular and premium cars are kept in garage.
        """
        pass

    def make_premium(self):
        """Make customer a premium customer, premium cars can be sold to the customer now."""
        pass

    def drive_with_car(self, driving_style: str):
        """
        Go for a drive.

        A car with the highest fuel percentage should be taken.
        If several cars have the same percentage, use the most expensive one.

        If the driving_style is "Rally", the customer takes the cheapest car instead.
        Regular driving takes 15 percentage points of fuel, "Rally" takes 35 percentage points (85% - 35% => 50%).
        If the fuel gets to zero during the drive, the car is left behind (it is no longer part of garage).
        """
        pass


class Dealership:
    """Dealership."""

    def __init__(self, name: str):
        """Constructor."""
        pass

    def add_car(self, car: Car):
        """Car is added to dealership."""
        pass

    def get_all_regular_cars(self):
        """Return all the regular cars sorted by value (ascending, lower to higher)."""
        pass

    def make_car_premium(self, car: Car):
        """Make a car premium, which can can be sold only to premium customers."""
        pass

    def get_all_premium_cars(self):
        """Return all the premium cars sorted by value (ascending, lower to higher)."""
        pass

    def sell_car_to_customer(self, customer: Customer):
        """
        Sell a car to customer depending on his/her wishes.

        After selling, the car is removed from the dealership and moved into customer's garage.
        In the given exercise, there is always a matching car.
        """
        pass


if __name__ == '__main__':
    assert count_camel_case_words("") == 0
    assert count_camel_case_words("helloWorld") == 2
    assert count_camel_case_words("ABC") == 3

    assert odd_index_sum([]) == 0
    assert odd_index_sum([1]) == 0
    assert odd_index_sum([1, 2]) == 2
    assert odd_index_sum([1, 2, 4, 3]) == 5

    # assert encode_string_with_hex_key("hello", "01234") == "hfnos"
    # assert encode_string_with_hex_key("a", "f") == "p"

#     assert who_gets_gingerbread(
#         {
#             'Mart': 4.0,
#             'Kristi': 4.5,
#             'Kevin': 3.2,
#             'Kfffevin': 1.5,
#         },
#         11
#     ) == {
#         "Kristi": 4,
#         "Mart": 4,
#         "Kevin": 3
#     }
#
#     assert fuel_calculator(151) == 64
#
#     print(make_table(9))
#     r"""
# \##/|\##/
# #\/#|#\/#
# #/\#|#/\#
# /##\|/##\
# ----+----
# \##/|\##/
# #\/#|#\/#
# #/\#|#/\#
# /##\|/##\
#     """
#     table = make_table(9).split("\n")
#     assert table[0] == r"\##/|\##/"
#     assert table[4] == r"----+----"
#     assert table[6] == r"#\/#|#\/#"
#     assert table[8] == "/##\\|/##\\"
#     assert table[-1] != "\n"  # no new-line in the end
#
#     table = make_table(7)
#     assert table[8:15] == "#X#|#X#"

    # university

    university = University("taltech", 60)
    student = Student("Bob", 61, 18)
    print(university.can_enroll_student(student))  # True
    print(university.can_unenroll_student(student))  # False; student is not yet in university

    university.enroll_student(student)
    print(university.get_students())  # [student]
    print(university.get_student_highest_gpa())  # [student]; since this student is the only one

    print(university.can_unenroll_student(student))  # True
    university.unenroll_student(student)
    print(university.get_students())  # []

    # # dealership
    #
    # blue_car = Car("Audi R4", "blue")
    # green_car = Car("Ford", "green")
    # wheel = Accessory("Sport wheel", 100)
    # blue_car.add_accessory(wheel)
    # car_dealer = Dealership("Ago Carfriend")
    # car_dealer.add_car(blue_car)
    # car_dealer.add_car(green_car)
    #
    # print(car_dealer.get_all_regular_cars())
    # # [This green Ford contains 0 accessories and has 100% fuel left.,
    # # This blue Audi R4 contains 1 accessories and has 100% fuel left.]
    # print(car_dealer.get_all_premium_cars())  # []
    #
    # customer = Customer("Ago", "Cheap green")
    # car_dealer.sell_car_to_customer(customer)
    # print(customer.get_garage())  # [This green Ford contains 0 accessories and has 100% fuel left.]
    # customer.drive_with_car("Rally")
    # print(customer.get_garage())  # [This green Ford contains 0 accessories and has 65% fuel left.]
    # customer.drive_with_car("Rally")
    # customer.drive_with_car("Rally")
    # print(customer.get_garage())  # []]
    #
    # car_dealer.make_car_premium(blue_car)
    # print(car_dealer.get_all_premium_cars())  # [This blue Audi R4 contains 1 accessories and has 100% fuel left.]
    #
    # customer_premium = Customer("Ago", "Expensive black")
    # customer_premium.make_premium()
    # car_dealer.sell_car_to_customer(customer_premium)
    # print(customer_premium.get_garage())  # [This blue Audi R4 contains 1 accessories and has 100% fuel left.]

