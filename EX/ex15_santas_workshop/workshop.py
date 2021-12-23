"""Santa's workshop."""
import csv

LIST_OF_PEOPLE = []


def get_data_from_wishlist_excel_file(file_path: str) -> dict:
    """
    Get wishlist data from local excel file.

    :param file_path: path of excel file.
    :return: dictionary of peoples names (k) and their wishes (v).
    """
    wishlist_dict = {}

    with open(file_path, encoding="utf8") as excel_file:
        reader = csv.reader(excel_file)
        for row in reader:
            wishlist_dict[row[0]] = row[1:]

    return wishlist_dict


def get_names_and_location_from_excel_file(file_path: str, nice: bool) -> dict:
    """
    Get people from naughty or nice list from local excel.

    :param file_path: path of csv file.
    :param nice: does excel file contain people who have been nice boolean value.
    :return: dictionary k, v = name, country
    """
    dict_people = {}

    with open(file_path, encoding="utf8") as excel_file:
        reader = csv.reader(excel_file)
        for row in reader:
            dict_people[row[0]] = row[1]

    return dict_people


class Person:
    """Creates a person."""

    def __init__(self, name: str, country: str, nice: bool, wish_list: list):
        """
        Constructor that creates a person.

        :param name: name of the child.
        :param country: country or origins.
        """
        self.name = name
        self.country = country
        self.nice = nice
        self.wish_list = wish_list

    def __repr__(self) -> str:
        """Returns person name"""
        return self.name


def add_to_list_of_people(person: Person):

    LIST_OF_PEOPLE.append(person)
    return LIST_OF_PEOPLE


if __name__ == '__main__':

    nice_people = get_names_and_location_from_excel_file("C:\\Users\\rasmu\\Documents\\ex15_nice_list.csv", True)
    naughty_people = get_names_and_location_from_excel_file("C:\\Users\\rasmu\\Documents\\ex15_naughty_list.csv", False)
    wishlist = get_data_from_wishlist_excel_file("C:\\Users\\rasmu\\Documents\\ex15_wish_list.csv")

    for k, v in naughty_people.items():
        for key, value in wishlist.items():
            if k == key:
                f = Person(name=k, country=v, nice=False, wish_list=value)
                add_to_list_of_people(person=f)

    for k, v in nice_people.items():
        for key, value in wishlist.items():
            if k == key:
                f = Person(name=k, country=v, nice=True, wish_list=value)
                add_to_list_of_people(person=f)

    print(LIST_OF_PEOPLE)

