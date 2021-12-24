"""Santa's workshop."""
import csv

LIST_OF_PEOPLE = []
WISHLIST_PATH = "C:\\Users\\rasmu\\Documents\\ex15_wish_list.csv"
NICE_PEOPLE_PATH = "C:\\Users\\rasmu\\Documents\\ex15_nice_list.csv"
NAUGHTY_PEOPLE_PATH = "C:\\Users\\rasmu\\Documents\\ex15_naughty_list.csv"


def get_data_from_local_csv_file(file_path: str) -> dict:
    """
    Function extracts data from csv file.

    :param file_path: local absolute path to csv file.
    :return: dictionary of data where first row is key and rest is value.
    """
    data = {}
    with open(file_path, encoding="utf8") as csv_file:
        reader = csv.reader(csv_file)
        for row in reader:
            data[row[0]] = row[1:]

    return data


def create_person_instance(people_dict: dict, wishlist: dict, nice: bool):
    """
    Creates person objects using Person class and adds said objects to global LIST_OF_PEOPLE.

    :param people_dict: dictionary of peoples names(key) and their location(value).
    :param wishlist: dictionary of peoples names(key) and their wishes(value).
    :param nice: boolean value is dict about naughty or nice people.
    :return: confirmation string
    """
    for name, country in people_dict.items():
        for name_in_wishlist, wished_items in wishlist.items():
            if name == name_in_wishlist:
                p = Person(name=name, country=country, nice=nice, wishlist=wished_items)
                LIST_OF_PEOPLE.append(p)

    return print("Instances of people created")


class Person:
    """Creates a person."""

    def __init__(self, name: str, country: str, nice: bool, wishlist: list):
        """
        Constructor that creates a person.

        :param name: name of the child.
        :param country: country or origins.
        """
        self.name = name
        self.country = country
        self.nice = nice
        self.wish_list = wishlist

    def __repr__(self) -> str:
        """Returns person name"""
        return self.name


if __name__ == '__main__':
    nice_people_dict = get_data_from_local_csv_file(NICE_PEOPLE_PATH)
    naughty_people_dict = get_data_from_local_csv_file(NAUGHTY_PEOPLE_PATH)
    wish_list = get_data_from_local_csv_file(WISHLIST_PATH)

    create_person_instance(nice_people_dict, wish_list, True)
    create_person_instance(naughty_people_dict, wish_list, False)

    print(len(LIST_OF_PEOPLE))
