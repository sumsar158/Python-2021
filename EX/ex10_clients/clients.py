"""Client."""
from typing import Optional


class Client:
    """
    Class for clients.

    Every client has:
    a name,
    the name of the bank they are a client of,
    the age of account in days,
    the starting amount of money and
    the current amount of money.
    """

    def __init__(self, name: str, bank: str, account_age: int, starting_amount: int, current_amount: int):
        """
        Client constructor.

        :param name: name of the client
        :param bank: the bank the client belongs to
        :param account_age: age of the account in days
        :param starting_amount: the amount of money the client started with
        :param current_amount: the current amount of money
        """
        self.name = name
        self.bank = bank
        self.account_age = account_age
        self.starting_amount = starting_amount
        self.current_amount = current_amount
        self.daily_earnings = (current_amount - starting_amount) / account_age

    def __repr__(self):
        """
        Client representation.

        :return: clients name
        """
        return self.name

    def earnings_per_day(self):
        """
        Client earnings per day since the start.

        You can either calculate the value or
        save it into a new attribute and return the value.
        """
        return self.daily_earnings


def read_from_file_into_list(filename: str) -> list:
    """
    Read from the file, make client objects and add the clients into a list.

    :param filename: name of file to get info from.
    :return: list of clients.
    """
    lines = []
    clients_list = []

    with open(filename) as f:
        for line in f:
            lines.append(line.strip())

    for line in lines:
        line = line.split(',')
        new_client = Client(name=line[0], bank=line[1], account_age=int(line[2]), starting_amount=int(line[3]),
                            current_amount=int(line[4]))
        clients_list.append(new_client)

    return clients_list


def filter_by_bank(filename: str, bank: str) -> list:
    """
    Find the clients of the bank.

    :param filename: name of file to get info from.
    :param bank: to filter by.
    :return: filtered list of people.
    """
    filtered_by_bank = []

    for client in read_from_file_into_list(filename):
        if client.bank == bank:
            filtered_by_bank.append(client)

    return filtered_by_bank


def largest_earnings_per_day(filename: str) -> Optional[Client]:
    """
    Find the client that has earned the most money per day.

    If two people have earned the same amount of money per day, then return the one that has earned it in less time.
    If no-one has earned money (everyone has less or equal to wat they started with), then return None.
    :param filename: name of file to get info from.
    :return: client with largest earnings.
    """
    list_of_clients = read_from_file_into_list(filename)
    list_of_earners = []

    for client in list_of_clients:
        if client.current_amount > client.starting_amount:
            list_of_earners.append(client)
    if not list_of_earners:
        return None

    list_of_earners = sorted(list_of_earners, key=lambda clients: (clients.daily_earnings, clients.account_age),
                             reverse=True)
    list_of_earners = sorted(list_of_earners, key=lambda clients: clients.account_age)
    top_earner = list_of_earners[0]

    return top_earner


def largest_loss_per_day(filename: str) -> Optional[Client]:
    """
    Find the client that has lost the most money per day.

    If two people have lost the same amount of money per day, then return the one that has lost it in less time.
    If everyone has earned money (everyone has more or equal to what they started with), then return None.
    :param filename: name of file to get info from.
    :return: client with largest loss.
    """
    list_of_clients = read_from_file_into_list(filename)
    list_of_losers = []

    for client in list_of_clients:
        if client.current_amount < client.starting_amount:
            list_of_losers.append(client)
    if not list_of_losers:
        return None

    list_of_losers = sorted(list_of_losers, key=lambda client: client.daily_earnings)
    list_of_losers = sorted(list_of_losers, key=lambda client: client.account_age)

    return list_of_losers[0]


if __name__ == '__main__':
    print(read_from_file_into_list("clients_info.txt"))  # -> [Ann, Mark, Josh, Jonah, Franz]

    print(filter_by_bank("clients_info.txt", "Sprint"))  # -> [Ann, Mark]

    print(largest_earnings_per_day("clients_info.txt"))  # -> Josh

    print(largest_loss_per_day("clients_info.txt"))  # -> Franz
