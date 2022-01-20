"""Exam 5 (2022-01-17)."""
from typing import Optional


def double_letters(text: str) -> str:
    """
    Double every letter in text.

    Latin letters (a-z and A-Z) have to be doubled for the output.
    All other symbols should remain the same.

    double_letters("abc") => "aabbcc"
    double_letters("hello world") => "hheelllloo wwoorrlldd"
    double_letters("Hi!?") => "HHii!?"
    """
    doubled_letters = ""
    for letter in text:
        if letter.isalpha():
            doubled_letters += letter
            doubled_letters += letter
        else:
            doubled_letters += letter
    return doubled_letters


def odds_sum(nums: list) -> int:
    """
    Find the sum of all odd numbers in given list.

    odds_sum([]) -> 0
    odds_sum([1, 2, 3]) -> 4
    odds_sum([2, 8, 10, 22]) -> 0
    """
    sum_of_odds = 0

    if not nums:
        return sum_of_odds

    for number in nums:
        if number % 2 != 0:
            sum_of_odds += number
    return sum_of_odds


def reverse_subword(s: str, subword: str) -> str:
    """
    If sub-word exists in s, reverse the first occurrence of s and return the modified string.

    Otherwise return original s.

    reverse_subword("abcde", "bc") => "acbde"
    reverse_subword("abcabc", "bc") => "acbabc"
    reverse_subword("abcabc", "ac") => "abcabc"

    :param s: original string
    :param subword: len(subword) > 0
    :return:
    """
    start = s.find(subword)
    print(start)
    end = len(subword)
    print(end)
    list_s = list(s)
    list_s[start:end+start] = list_s[start:start+end][::-1]
    list_s = "".join(list_s)
    return list_s


def sum_of_multipliers(first_num: int, second_num: int, limit: int) -> int:
    """
    Sum all unique multipliers for two numbers.

    The task is to find all the multipliers of two given numbers within the limit.
    Then, find the sum of those multipliers where duplicates are removed.

    All the numbers are positive integers.

    sum_of_multipliers(3, 5, 20) => 98
    We get: [3, 6, 9, 12, 15, 18] (21 is over the limit)
    and [5, 10, 15, 20]
    15 is in both lists, we only use it once, sum is 98

    sum_of_multipliers(3, 3, 20) => 63
    sum_of_multipliers(3, 1, 20) => 210

    :param first_num: first number
    :param second_num: second number
    :param limit: limit
    :return: sum of multiplies
    """
    first_num_multipliers = []
    second_num_multipliers = []
    final_list = []

    # S= n(2a + (n-1)d)/2

    pass


def recursive_max(numbers: list) -> int:
    """
    Find max value from the list using recursion.

    No loops allowed.
    You have to find the maximum value of integers in the list.

    recursive_max([]) => 0
    recursive_max([8]) => 8
    recursive_max([8, 9, 10]) => 10
    """
    pass


def make_cupboard(total_width: int, total_height: int, levels: int, sections_on_levels: list) -> str:
    """
    Given measurements of a cupboard, make a cupboard's string representation.

    Variable total_width determines the width of the cupboard,
    total_height determines the height and levels determines how many levels the cupboard has.
    Variable sections_on_levels shows how many sections there are on each level (bottom up).

     The final result should be cupboard's string representation, where sections and levels are separated by '#' and
     also the walls, roof and bottom should be made of '#'.
     The levels should all be of equal height, but the total height should be met.
     The sections on each level should also be of equal width, the total width should again be met.

     If such cupboard can't be made, return a message saying "Can't make cupboard."

     There is not new line in the end of the string.

    Example:
    make_cupboard(42, 10, 2, [3, 2]) =>
    Can't make cupboard.

    Example:
    make_cupboard(43, 11, 2, [3, 2]) =>
    ###########################################
    #                    #                    #
    #                    #                    #
    #                    #                    #
    #                    #                    #
    ###########################################
    #             #             #             #
    #             #             #             #
    #             #             #             #
    #             #             #             #
    ###########################################
    """
    sections_on_levels.reverse()
    shelf = ""
    for section in sections_on_levels:
        for i in range(total_height+1):
            if i == 0:
                shelf += total_width * "#" + '\n'

    print(shelf)

class Book:
    """Represent book model."""

    def __init__(self, title: str, author: str, price: float, rating: float):
        """
        Class constructor.

        Each book has title, author and price.
        :param title: book's title
        :param author: book's author
        :param price: book's price
        """
        self.title = title
        self.author = author
        self.price = price
        self.rating = rating

    def __repr__(self):
        """Represent book by title."""
        return self.title


class Store:
    """Represent book store model."""

    def __init__(self, name: str, rating: float):
        """
        Class constructor.

        Each book store has name.
        There also should be an overview of all books present in store

        :param name: book store name
        """
        self.rating = rating
        self.name = name
        self.books_in_store = []

    def can_add_book(self, book: Book) -> bool:
        """
        Check if book can be added.

        It is possible to add book to book store if:
        1. The book with the same author and title is not yet present in this book store
        2. book's own rating is >= than store's rating
        :return: bool
        """
        for b in self.books_in_store:
            if b.title == book.title and b.author == book.author:
                return False
        if book.rating >= self.rating:
            return True
        else:
            return False

    def add_book(self, book: Book):
        """
        Add new book to book store if possible.

        :param book: Book
        Function does not return anything
        """
        if self.can_add_book(book):
            self.books_in_store.append(book)

    def can_remove_book(self, book: Book) -> bool:
        """
        Check if book can be removed from store.

        Book can be successfully removed if it is actually present in store

        :return: bool
        """
        for b in self.books_in_store:
            if b.title == book.title and b.author == book.author:
                return True
        else:
            return False

    def remove_book(self, book: Book):
        """
        Remove book from store if possible.

        Function does not return anything
        """
        if self.can_remove_book(book):
            self.books_in_store.remove(book)

    def get_all_books(self) -> list:
        """
        Return a list of all books in current store.

        :return: list of Book objects
        """
        return self.books_in_store

    def get_books_by_price(self) -> list:
        """
        Return a list of books ordered by price (from cheapest).

        :return: list of Book objects
        """
        return sorted(self.books_in_store, key=lambda p: p.price)

    def get_most_popular_book(self) -> list:
        """
        Return a list of book (books) with the highest rating.

        :return: list of Book objects
        """
        return sorted(self.books_in_store, key=lambda r: r.rating, reverse=True)


class ComputerPart:
    """A computer part."""

    def __init__(self, name: str, cost: float):
        """
        ComputerPart constructor.

        Each computer part has a name and a cost.
        """
        self.cost = cost
        self.name = name

    def get_cost(self) -> float:
        """Return the cost of the computer part."""
        return self.cost

    def __repr__(self) -> str:
        """Return the name of the computer part."""
        return self.name


class Computer:
    """A computer at an internet cafe."""

    def __init__(self, name: str, total_parts_needed: int):
        """
        Computer constructor.

        Each computer has name and the amount of parts required for it to function.

        A computer should also keep track of all the parts that are in it.
        :param name: computer name
        :param total_parts_needed: the amount of parts needed for the computer to function
        """
        self.total_parts_needed = total_parts_needed
        self.name = name
        self.price = 0.0
        self.parts = []
        self.working = bool

    def add_part(self, part: ComputerPart):
        """
        Add a part to the computer.

        The parts cost is also added to the computers cost.

        The part is not added if the computer is already working.
        """
        if not self.is_working():
            self.parts.append(part)
            self.total_parts_needed -= 1
            self.price += part.cost

    def get_parts_needed(self) -> int:
        """
        Return the amount of parts that is needed to fully build this computer.

        If the computer needs a total of 3 parts and currently has 1 part, this should return 2.
        """
        return self.total_parts_needed - len(self.parts)

    def is_working(self) -> bool:
        """Return if the computer has the correct amount of parts."""
        return self.total_parts_needed == 0

    def get_parts(self) -> list[ComputerPart]:
        """
        Return a list of all parts that are in the computer.

        Parts should be in the same order as they were added.
        """
        return self.parts

    def get_cost(self) -> float:
        """Return the cost of the computer."""
        return self.price

    def __repr__(self) -> str:
        """
        String representation of Computer.

        Returns string in form "A {name} for {cost}€ with {parts}"

        All the parts should be seperated with ", ".
        Parts should be in the same order as they were added.
        If there are no parts in the computer, there should be "nothing".
        Cost is always shown with 2 decimal places.

        Examples:
        "A hardcore gaming computer for 540.30€ with gtx1070, r5 2600, CX650F, EV860"
        "A pc for 0.00€ with nothing"
        """
        parts_string = ""
        for part in self.parts:
            parts_string += str(part)
            if part != self.parts[-1]:
                parts_string += ", "
        if not self.parts:
            parts_string = "nothing"
        return f"A {self.name} for {format(float(self.price), '.2f')}€ with {parts_string}"


class Customer:
    """A customer at an internet cafe."""

    def __init__(self, name: str, money: float):
        """
        Constructor.

        Each customer must have a name, money and it should also keep track of owned computers.
        """
        self.money = money
        self.name = name
        self.owned_computers = []

    def can_buy_computer(self, computer: Computer) -> bool:
        """Return if this customer has enough money to buy a computer."""
        return self.money >= computer.price

    def buy_computer(self, computer: Computer) -> bool:
        """
        Buy a computer if it can be done.

        This customer loses money equal to the cost of the computer.

        Returns True or False whether the computer was bought.
        """
        if self.can_buy_computer(computer):
            self.money -= computer.price
            self.owned_computers.append(computer)
            return True
        else:
            return False

    def get_computers(self) -> list[Computer]:
        """Return all computers owned by this customer."""
        return self.owned_computers

    def __repr__(self) -> str:
        """
        String representation of a customer.

        Should be in format:
        "{name} with {money}€
        {computer1}
        {computer2}
        {computer3}
        ..."

        The money is always shown with 2 decimal places.

        example1:
        "Laura with 666.00€
        A hardcore gaming computer for 540.30€ with gtx1070, r5 2600, CX650F, EV860
        A pc for 0.00€ with nothing"

        example2:
        "Karl with 0.00€"
        """
        nl = "\n"
        customer_representation = ""
        customer_representation += f"{self.name} with {format(float(self.money), '.2f')}€"
        for comp in self.owned_computers:
            customer_representation += f"{nl}{str(comp)}"
        return customer_representation


class ComputerStore:
    """A store where people can buy computers."""

    def __init__(self):
        """Constructor."""
        self.computers = []
        self.computer_parts = []
        self.working_computer = []

    def add_computer(self, computer: Computer):
        """Add a computer to the store."""
        self.computers.append(computer)

    def add_part(self, part: ComputerPart):
        """Add a computer part to the storage of the store."""
        self.computer_parts.append(part)

    def get_computers(self) -> list[Computer]:
        """Return all computers in the stores as a list."""
        return self.computers

    def get_parts(self) -> list[ComputerPart]:
        """Return all unused computer parts in the store."""
        return self.computer_parts

    def get_working_computers(self) -> list[Computer]:
        """Return all computers which are working."""
        working_computers = []
        for computer in self.computers:
            if computer.is_working():
                working_computers.append(computer)
        return working_computers

    def build_computer(self) -> Optional[Computer]:
        """
        Make the store build a computer.

        If the store has no non-functioning computers, return None.

        The store looks at the computer which have the least amount of parts missing.
        If two computers have the same amount of parts missing, then the store picks the one that is cheaper.
        (there aren't any cases where computers parts missing and costs are equal)

        example:
        computer1 costs 100 and 3 parts missing
        computer2 costs 300 and 3 parts missing
        computer3 costs 50 and 4 parts missing
        computer4 costs 10 and 0 parts missing (it is already functional)
        The store chooses to build computer1!

        If the store doesnt have enough spare parts to build a computer, return None.

        The store adds the cheapest available parts to the computer until it is built.

        If the computer is built successfully, return the built computer. Else return None.
        """
        computer_parts = sorted(self.computer_parts, key=lambda p: p.cost)
        computers = sorted(self.computers, key=lambda c: (c.total_parts_needed, c.price))
        cheapest_pc = None
        for pc in computers:
            if not pc.is_working():
                cheapest_pc = pc
                break

        if not self.get_working_computers():
            return None

        if not computer_parts:
            return None
        if len(computer_parts) >= cheapest_pc.get_parts_needed():
            for part in computer_parts:
                if not cheapest_pc.is_working():
                    cheapest_pc.add_part(part)
                    computer_parts.remove(part)
                    if cheapest_pc.is_working():
                        return cheapest_pc
        else:
            return None

    def sell_customer_computer(self, customer: Customer):
        """
        A customer walks into the store and wants the most expensive working computer that can be bought with their money.

        Note that the sold computer must work.

        If there are no such computers, the store tries to build a new computer.

        If a computer is successfully built and it is cheap enough to buy, then the customer buys that computer.
        """
        built_computer = self.build_computer()

        working_computers = sorted(self.get_working_computers(), key=lambda p: p.price, reverse=True)
        if working_computers:
            for computer in working_computers:
                if customer.can_buy_computer(computer):
                    customer.buy_computer(computer)
                    self.computers.remove(computer)
                    break
                else:
                    continue

        if self.build_computer() is not None:
            if customer.can_buy_computer(built_computer):
                customer.buy_computer(built_computer)


if __name__ == '__main__':


    print(reverse_subword('tere', 're'))


