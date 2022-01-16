"""Santa's workshop."""
import csv
import json
import urllib.request
import urllib.parse
import urllib.error

LIST_OF_PEOPLE = []
DICT_OF_PEOPLE = {}
WISHLIST_PATH = "C:\\Users\\rasmu\\Documents\\ex15_wish_list.csv"
NICE_PEOPLE_PATH = "C:\\Users\\rasmu\\Documents\\ex15_nice_list.csv"
NAUGHTY_PEOPLE_PATH = "C:\\Users\\rasmu\\Documents\\ex15_naughty_list.csv"
API_URL = "http://api.game-scheduler.com:8089/gift?"


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
    Create person objects using Person class and adds said objects to global DICT_OF_PEOPLE.

    :param people_dict: dictionary of peoples names(key) and their location(value).
    :param wishlist: dictionary of peoples names(key) and their wishes(value).
    :param nice: boolean value is dict about naughty or nice people.
    :return: confirmation string.
    """
    for name, country in people_dict.items():
        for name_in_wishlist, wished_items in wishlist.items():
            if name == name_in_wishlist:
                p = Person(name=name, country=country, nice=nice, wishlist=wished_items)
                DICT_OF_PEOPLE[name] = p
                LIST_OF_PEOPLE.append(p)

    return print(f"Instances of people created, nice : {nice}")


class Person:
    """Creates a person."""

    def __init__(self, name="", country="", nice=True, wishlist=None):
        """
        Constructor that creates a person.

        :param name: name of the child.
        :param country: country or origins
        """
        if wishlist is None:
            wishlist = []
        self.name = name
        self.country = country
        self.nice = nice
        self.wish_list = wishlist

    def __repr__(self) -> str:
        """Return person name."""
        return self.name


class Product:
    """Creates a product."""

    def __init__(self, name, price, production_time, weight):
        """Create product parameters."""
        self.name = name
        self.price = price
        self.production_time = production_time
        self.weight = weight

    def __repr__(self):
        """Represent product class."""
        return f"Product ({self.name}, {self.weight} g)"


class Warehouse:
    """Creates a warehouse."""

    def __init__(self):
        """Make product dict for warehouse class."""
        self.products = {}

    def get_product_from_factory(self, name: str) -> Product | None:
        """Return product object from factory."""
        qs = urllib.parse.urlencode({"name": name})
        try:
            with urllib.request.urlopen(API_URL + qs) as f:
                # read all
                contents = f.read()

                # to convert into regular string
                contents.decode("utf-8")

                # read json to python object
                data = json.loads(contents.decode('utf-8'))

                product = Product(name=data['gift'],
                                  price=data['material_cost'],
                                  production_time=data['production_time'],
                                  weight=data['weight_in_grams'])

                if data['gift'] not in self.products:
                    self.products[data['gift']] = []
                self.products[data['gift']].append(product)

                return product

        except urllib.error.HTTPError:
            return None

    def get_product(self, name):
        """Return product name."""
        return self.products.get(name)


if __name__ == '__main__':
    nice_people_dict = get_data_from_local_csv_file(NICE_PEOPLE_PATH)
    naughty_people_dict = get_data_from_local_csv_file(NAUGHTY_PEOPLE_PATH)
    wish_list = get_data_from_local_csv_file(WISHLIST_PATH)

    create_person_instance(nice_people_dict, wish_list, True)
    create_person_instance(naughty_people_dict, wish_list, False)

    print(len(DICT_OF_PEOPLE))

    warehouse = Warehouse()
    print(warehouse.get_product_from_factory("swimming flippers"))
    print(warehouse.get_product_from_factory("Small watering can"))
    print(warehouse.get_product_from_factory("VHS player"))
    print(warehouse.products.get("VHS player"))
    print(warehouse.get_product("VHS player"))
