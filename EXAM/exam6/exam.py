"""Eksam 6 (2022-01-21)."""


def segment_number(first_number, last_number):
    """
    Segment number.

    Return list of numbers where only numbers between first_number
    and last_number (both inclusive) which divide by 5 but do not divide by 3
    are used.

    #1

    :param first_number: the lowest possible candidate
    :param last_number: the highest possible candidate
    :return: list of numbers
    """
    new_list = []
    for i in range(first_number, last_number + 1):
        if i % 5 == 0 and i % 3 != 0:
            new_list.append(i)

    return new_list


def add_or_subtract(numbers):
    """
    Add or subtract.

    Return the sum of all numbers in a list.

    The sum is calculated according to following rules:
        -always start by adding all the numbers together.
        -if you find a 0, start subtracting all following numbers until you find another 0, then start adding again.
        -there might be more than two 0 in a list - change +/- with every 0 you find.

    For example:
        [1, 2, 0, 3, 0, 4] -> 1 + 2 - 3 + 4 = 4
        [0, 2, 1, 0, 1, 0, 2] -> -2 - 1 + 1 - 2 = -4
        [1, 2] -> 1 + 2 = 3
        [4, 0, 2, 3] = 4 - 2 - 3 = -1

    #2

    :param numbers: the list of number given.
    :return: the sum of all numbers.
    """
    sum_of_numbers = 0
    condition = True
    for num in numbers:
        if condition:
            sum_of_numbers += num
            if num == 0:
                condition = False
                continue
        if not condition:
            sum_of_numbers -= num
            if num == 0:
                condition = True
                continue

    return sum_of_numbers


def should_get_up_early(is_weekday, really_tired, first_class_is_programming):
    """
    Should get up early.

    Decide if you should get up early enough for first class.

    You should only even consider getting up early if it is a weekday, on weekends you should never get up early.
    If it is a weekday you should typically get up early, unless you are really tired.
    But if it is a weekday and you are really tired but the first class is a programming class you should still get up
    early ignoring you being tired.

    #3

    :param is_weekday: is it a weekday or not, boolean
    :param really_tired: are you really tired, boolean
    :param first_class_is_programming: is the first class a programming class, boolean
    :return: True if you should get up early, otherwise False
    """
    if not is_weekday:
        return False

    if is_weekday:
        if first_class_is_programming:
            return True
        if really_tired:
            return False
        else:
            return True


def pear_fear(pears, people):
    """
    Pear fear.

    Every 3rd person fears pears, so they won't get any.
    How many pears will each get?
    Everyone who is not afraid of pears gets equal number of pears.
    Only whole pears will be used, so some pears may remain.

    #4

    :param pears:
    :param people:
    :return:
    """
    poeple_list = []
    for i in range(people + 1):
        poeple_list.append(i)
    for i in poeple_list[::3]:
        poeple_list.remove(i)

    people = len(poeple_list)
    pears = pears // people

    return pears


def string_between_string(word1, word2):
    """
    Insert reversed word2 to the center of word1.

    word1 length is always even.

    #5

    :param word1: Initial word. String.
    :param word2: Word to reverse and insert. String.
    :return: New word as string.
    """
    half = int(len(word1) // 2)
    second_half = ""
    word2 = str(word2[::-1])
    print(second_half)
    first_half = word1[:half:]
    second_half = word1[half:]
    final_word = (str(first_half) + str(word2) + str(second_half))
    return final_word


def get_padded_string(string1, string2):
    """
    Pad the longer of two strings with the shorter one on both sides.

    If both strings are the same length, consider string1 as the longer one.
    For example when string1 is "pizza" and string2 is "bbq", this should return "bbqpizzabbq".

    #6

    :param string1: String one
    :param string2:  String two
    :return: Padded string
    """
    if len(string1) > len(string2) or len(string1) == len(string2):
        return f"{string2}{string1}{string2}"
    if len(string2) > len(string1):
        return f"{string1}{string2}{string1}"


def remove_duplicate(number_list):
    """
    Remove duplicates.

    Go though given list and remove all
    occurrences of two or more of the same
    numbers appearing after one another.
    Remove all but one of the duplicates.

    #7

    :param number_list: input list
    :return: new list
    """
    new_list = []
    duplicates = []
    last_number = int
    for number in number_list:
        if number == last_number:
            duplicates.append(number)
            last_number = number
        if number != last_number:
            new_list.append(number)
            last_number = number

    return new_list


def who_called(calls, name):
    """
    Who called.

    You are given a dictionary of calls and a name.
    Determine who called that name.
    The key of the dictionary is the caller, the value is to whom the caller called.
    If nobody called the person, return -1.

    #8

    :param calls: dictionary of all the calls
    :param name: name of the receiver
    :return: name of the caller
    """
    who_called = []
    for k, v in calls.items():
        if v == name:
            who_called.append(k)
    if not who_called:
        return -1
    else:
        return who_called[0]


def remove_lowest_digit(number):
    """
    Remove lowest digit.

    Given a non-negative integer, remove the first occurrence
    of the lowest digit and return a new number.

    123 => 23
    223 => 23
    232 => 32
    1 => 0
    :param number: non-negative integer
    :return: non-negative integer
    """
    res = ""
    number_list = list(str(number))
    inte_number_list = []
    for num in number_list:
        inte_number_list.append(num)
    if len(inte_number_list) <= 1:
        return 0
    smallest_int = min(inte_number_list)
    inte_number_list.remove(smallest_int)

    for num in inte_number_list:
        res += num
    res = int(res)

    return res


def show_highest_grade(grade1, grade2):
    """
    Show highest grade.

    Print "Highest grade: GRADE"
    where GRADE is the higher of two inputs.

    grade1, grade2 are both non-negative integers.

    3, 4 => "Highest grade: 4"

    #10

    :param grade1:
    :param grade2:
    :return:
    """
    if grade1 > grade2:
        highest_grade = grade1
    else:
        highest_grade = grade2

    print(f"Highest grade: {highest_grade}")


class Account:
    """Create Account instace for transaction ex."""

    def __init__(self, account_name):
        """create account."""
        self.name = account_name
        self.balance = 100
        self.enough_money_for_transaction = bool

    def enough_money(self, transaction_amount):
        """Return boolean value if transaction can happen."""
        if self.balance - transaction_amount < 0:
            return False


def transactions(transaction_string):
    """
    The result of transactions.

    Given a string of transactions between bank accounts
    return the amount of money on accounts A, B anc C.

    The transaction is in the following format:
    X,Y,Z
    where
    X is the account (A, B or C) the money is transferred from
    Y is the account (A, B or C) the money is transferred to
    Z is the amount transferred.

    For example:
    "A,B,100"
    The amount in account A is lowered by 100,
    the amount in account B is raised by 100.

    The transaction can take place if the starting
    account has enough money.
    Initially, every account has 100 units of money.

    Account C is credit account, meaning from
    that account the transactions can be executed even
    if there is no money left, the balance goes below 0.

    "C,A,101"
    as the first transaction yields in
    [201, 100, -1]

    "A,B,100" => [0, 200, 100]
    "A,B,10 B,C,10" => [90, 100, 110]

    "A,B,200 C,A,200" => [300, 100, -100]
    (the first transaction is cancelled)

    If the first account is 0 (zero), then
    the money is just transferred to the second account
    (like payment into the account).

    "0,A,100" => [200, 100, 100]
    "0,A,110 A,B,120" => [90, 220, 100]

    The input is always correct:
     - space separated transactions
     - transaction is in the format X,Y,Z
     - X is either '0', 'A', 'B' or 'C'
     - Y is either 'A', 'B' or 'C'
     - Z is non-negative integer

     #11

    :param transaction_string: string with transactions
    :return: list of ints (length 3)
    """
    list_of_accounts = []
    "create accounts"
    transaction_list = transaction_string.split(",")
    if transaction_list[0] not in list_of_accounts:
        a = Account(transaction_list[0])
        list_of_accounts.append(a)
    if transaction_list[1] not in list_of_accounts:
        a = Account(transaction_list[1])
        list_of_accounts.append(a)


def recursive_sum(list_of_numbers):
    """
    Recursive sum.

    Write a function that finds the sum of numbers in the given list recursively.
    Assume that the list always exists and can be empty or contain only numbers.

    #12

    @param list_of_numbers: list of integers.
    @return: sum of numbers in list
    """
    pass


class Stargate:
    """
    Class Stargate.

    Stargate can dial (connect) to another stargate and a stargate can be connected to
    (dialed to) by another stargate.
    Each stargate can only have one active connection.
    A stargate can be only connected to if it is currently disconnected.
    When a stargate connects to a stargate it means that the destination stargate is
    also connected to the stargate that initiated the connection (the one who dialed).
    When one of the stargates that is connected disconnects, the other disconnects also.
    To dial out (initiate the connection it needs to have a Dial Home
    Device (DHD). Think of the DHD of like a controller. If it doesn't have one, it can oly be dialed to by another
    stargate (it can't dial out) and it can't initiate a disconnect (remains connected until the other stargate
    initiates the disconnect).
    """

    def __init__(self, planet_name, has_dial_home_device):
        """
        Construct a new stargate.

        :param planet_name: The name of the planet the stargate is on. String
        :param has_dial_home_device: Does the stargate have a Dial Home Device. Boolean
        """
        self.has_dial_home_device = has_dial_home_device
        self.planet_name = planet_name
        self.active_connection = False
        self.connected_gate = None

    def get_planet_name(self):
        """
        Get planet name.

        :return: The name of the planet the stargate is on. String
        """
        return self.planet_name

    def is_connected(self):
        """
        Whether is connected.

        :return: Is the stargate currently connected or not. Boolean
        """
        if not self.has_dial_home_device:
            return False
        return self.active_connection

    def get_connected_stargate(self):
        """
        Get connected stargate.

        :return: The stargate this stargate is connected to. None if not connected. Stargate or None
        """
        if self.active_connection:
            return self.connected_gate
        else:
            return None

    def get_connected_planet_name(self):
        """
        Get connected planet name.

        :return: The name of the planet that the stargate that this
        stargate is connected to is on. None if not connected. String or None
        """
        connected_planet = self.connected_gate
        if self.connected_gate is None:
            return None
        else:
            return connected_planet.planet_name

    def dial(self, destination):
        """
        Dial.

        Dial out to another stargate. This can only succeed if these criteria are met:
        * this stargate is not connected
        * this stargate has a Dial Home Device
        * the destination is an instance of the Stargate class
        * the destination stargate is currently not connected
        * this stargate is not trying to connect to itself

        :param destination: The stargate that this stargate should connect to. Stargate
        :return: Did the two stargates connect successfully. Boolean
        """
        if not self.active_connection:
            if self.has_dial_home_device:
                if type(destination) == type(self):
                    if not destination.active_connection:
                        if self != destination:
                            self.active_connection = True
                            destination.active_connection = True
                            self.connected_gate = destination
                            destination.connected_gate = self
                            return True

    def disconnect(self):
        """
        Disconnect.

        Disconnect this stargate and the stargate that this stargate is connected to if this stargate is currently
        connected.
        """
        destination = self.connected_gate

        if self.active_connection and self.has_dial_home_device:
            self.active_connection = False
            self.connected_gate = None
            if destination.has_dial_home_device and destination.active_connection:
                self.active_connection = False
                self.connected_gate = None


class Student:
    """Student class."""

    def __init__(self, curriculum):
        """
        Constructor.

        :param curriculum: the students curriculum.
        """
        self.curriculum = curriculum

    def add_subject_to_curriculum(self, subject, eap):
        """
        Add the given subject to the students curriculum.

        If the subject is already in the curriculum, rewrite the EAPs.

        :param subject: the subject to be added to the curriculum.
        :param eap: how many EAPs the subject is worth.
        """
        if subject in self.curriculum.subjects:
            for s in self.curriculum.subjects:
                if s == subject:
                    s.eaps = eap
        else:
            self.curriculum.subjects.append(subject)

    def add_grade(self, subject, grade):
        """
        Add grade.

        Add the grade for the subject to students record if the subject is in the students curriculum.
        If the student already has a grade for said subject, rewrite it.
        The grade must be an integer between 0-5 (both included).

        :param subject: the subject for which the students has been given a grade.
        :param grade: the grade the student received. Must be between 0-5 (both included).
        """
        if subject in self.curriculum.subjects:
            for s in self.curriculum.subjects:
                if s == subject:
                    s.grade = grade

    def get_subject_grade(self, subject):
        """
        Get subject grade.

        Return the grade the student has received for the given subject.
        If the student has not received a grade for the subject yet return None.
        :param subject: the subject which grade to return.
        :return: the received grade or None.
        """
        for s in self.curriculum.subjects:
            if s == subject:
                return s.grade

    def get_average_grade(self):
        """
        Calculate the average of all grades on the students record.

        If a student has failed a subject (the grade is 0), don't count it.
        :return: the average grade with two decimal places.
        """
        list_of_grades = []
        for s in self.curriculum.subjects:
            if s.grade is not None and s.grade > 0:
                list_of_grades.append(s.grade)
            else:
                continue

        return sum(list_of_grades) / len(list_of_grades)

    def get_eaps(self):
        """
        Get EAP-s.

        Calculate, how many EAPs does the student currently have for passed subjects.
        A subject is passed when the student has received a grade greater than 0 for it.
        :return: the nr of EAPs.
        """
        total_eap = 0
        for s in self.curriculum.subjects:
            if s.grade and s.grade > 0:
                total_eap += s.eaps
        return total_eap

    def get_curriculum(self):
        """
        Get the students curriculum.

        :return: a Curriculum object.
        """
        return self.curriculum

    def get_subject_eaps(self, subject):
        """Retrun subjects eaps."""
        for s in self.curriculum.subjects:
            if s == subject:
                return s.eaps


class Subject:
    """Subject class."""

    def __init__(self, name: str, eaps: int):
        """
        Constructor.

        :param name: name of the subject.
        :param eaps: how many EAPs the subject is worth.
        """
        self.name = name
        self.eaps = eaps
        self.grade = None

    def get_eaps(self):
        """
        Return how many EAPs the subject is worth.

        :return: nr of EAPs
        """
        return self.eaps


class Curriculum:
    """Curriculum class."""

    def __init__(self):
        """Constructor."""
        self.subjects = []

    def get_subject(self, name):
        """
        Get a subject from the curriculum by name.

        :param name: name of the subject.
        :return: subject object.
        """
        for subject in self.subjects:
            if subject.name == name:
                return subject

    def add_subject(self, subject):
        """
        Add the subject to curriculum.

        :param subject: the subject to be added.
        """
        self.subjects.append(subject)

    def get_all_subjects(self):
        """
        Get all subjects.

        :return: al list of all the subjects in the curriculum.
        """
        return self.subjects

    def add_subject_grade(self, subject, grade):
        """
        Add subject grade.

        Add the grade for the subject to students record if the subject is in the students curriculum.
        If the student already has a grade for said subject, rewrite it.
        The grade must be an integer between 0-5 (both included).

        :param subject: the subject for which the students has been given a grade.
        :param grade: the grade the student received. Must be between 0-5 (both included).
        """
        for sub in self.subjects:
            if sub == subject:
                sub.grade = grade

    def get_grades(self) -> dict:
        """
        Return a dictionary where keys are subjects and values are grades.

        The dictionary must include all subjects in teh curriculum,
        including those the student has not received a grade for yet.
        :return: dictionary.
        """
        d = {}
        for subject in self.subjects:
            d[subject] = subject.grade
        return d


if __name__ == '__main__':
    # OOP1 - stargate

    sg1 = Stargate("Earth", True)
    sg2 = Stargate("Another planet", False)
    assert sg1.dial(sg2) is True
    assert sg1.get_connected_planet_name() == "Another planet"

    print(sg2.active_connection)
    print(sg1.active_connection)

    sg2.disconnect()

    print(sg2.get_connected_planet_name())
    print(sg1.get_connected_planet_name())
    print(sg2.active_connection)
    print(sg1.active_connection)

    assert sg2.get_connected_planet_name() == "Earth"
    sg1.disconnect()

    print(sg2.active_connection)
    print(sg1.active_connection)
    print("--------------")

    assert sg2.dial(sg1) is False
    assert sg2.get_connected_planet_name() is None
    print("--------------")
    print(sg2.active_connection)
    print(sg1.active_connection)