"""Petrol Station."""
import copy
from abc import ABC, abstractmethod
from datetime import date
from enum import Enum, auto


class ClientType(Enum):
    """
    Client type.

    Due to the fact that the client type is used in several places,
    it is more convenient if it is indicated by an object rather than a string.
    Status can be:

         1) basic (he is not a regular customer and he has no discounts)

         2) bronze customer (membership in the club starts with a discount of 0.025 euros for each liter of fuel and in the store
         5% for the goods received)

         3) silver customer (II level club membership, the conditions for receiving it is that the amount of purchases is 1000 euros,
         there is a discount on fuel in the amount of 0.05 euros and a 10% discount on goods in the store)

         4) gold customer (club membership level III, awarded for purchases of EUR 5,000,
         fuel discount is 0.1 euros and the store has a 15% discount on the entire product range)

         For levels II and III, they are thrown in bronze if the customer has not been active for 2 months
    """

    Basic = auto()
    Bronze = auto()
    Silver = auto()
    Gold = auto()


class OrderItem(ABC):
    """One line from bill."""

    def __init__(self, name: str, price: float):
        """
        Constructor (NB! Variables must be private).

        In case the price is negative, raise RuntimeError().
        """
        self.__name = name
        self.__price = price

    def get_name(self) -> str:
        """
        Return the item name.

        :return: str: name
        """
        return self.__name

    def get_price(self) -> float:
        """
        Return the price of the product.

        :return: float: price
        """
        return self.__price

    def get_total_price(self, client_type: ClientType, quantity: float = 1.0) -> float:
        """
        Return the price of the item.

        Returns the price of the goods from the given receipt line,
        taking into account the discount and the purchased quantity.

        :param client_type: the client type
        :param quantity: quantity of a product
        :return: float: total price
        """
        return 0.0

    @abstractmethod
    def get_discount(self, client_type: ClientType) -> float:
        """
        Abstract because fuels and products have different uses for discounts.

        There is no need to write anything here.

        :param client_type
        :return: float: the discount
        """
        ...

    def __hash__(self):
        """Hash for using with dictionaries."""
        return hash((self.__name, self.__price))

    def __eq__(self, other):
        """Return True if OrderItems are equal, else - False."""
        if type(other) is type(self):
            return (self.__name == other.__name) and (self.__price == other.__price)
        else:
            return False

    def __repr__(self):
        """String representation for OrderItem."""
        return "Fill this as you wish"


class ShopItem(OrderItem):
    """
    The product in the store.

    The product class in the store, which has a price, name and discount, calculated for 1 customer.
    """

    def __init__(self, name: str, price: float):
        """Constructor."""
        super().__init__(name, price)

    def get_discount(self, client_type: ClientType) -> float:
        """
        Discount for shop item.

        This has to be implemented for ShopItem.

        :param client_type
        :return: float: the discount
        """
        return 0.0


class Fuel(OrderItem):
    """
    The fuel.

    The fuel class, including price, name and discount, calculated for customers per liter.
    """

    def __init__(self, name: str, price: float):
        """Construtor."""
        super().__init__(name, price)

    def get_discount(self, client_type: ClientType) -> float:
        """
        Discount for fuel.

        This has to be implemented for Fuel.

        :param client_type
        :return: float: the discount
        """
        return 0.0


class Order:
    """Order with order items and date."""

    def __init__(self, items: dict[OrderItem, float], order_date: date, client_type: ClientType):
        """
        Constructor (NB! Variables must be private).

        In case the item quantity is negative, raise RuntimeError().

        : param items: dictionary where key is product / fuel and value is quantity
        : param order_date: date of purchase
        : param client_type: The type of client that made the purchase
        """
        self.__items = items
        self.__order_date = order_date
        self.__client_type = client_type

    def get_date(self) -> date:
        """
        Return the date of purchase.

        :return: date
        """
        pass

    def get_final_price(self) -> float:
        """
        Calculate the total cost of purchases.

        :return: float
        """
        return 0.0

    def __hash__(self):
        """Hash for using with dictionaries."""
        return hash((self.__items, self.__order_date, self.__client_type))

    def __eq__(self, other):
        """Return True if Orders are equal, else - False."""
        if type(other) is not type(self):
            return False
        if not (self.__client_type == other.__client_type) or not (self.__order_date == other.__order_date) \
                or (len(self.__items) != len(other.__items)):
            return False

        return all(map(lambda x: x[0] == x[1], zip(self.__items, other.__items)))

    def __repr__(self):
        """String representation for Order."""
        return f"{', '.join(map(lambda item: item.get_name(), self.__items.keys()))}"


class Client:
    """Client itself."""

    def __init__(self, name: str, balance: float, client_type: ClientType):
        """
        Constructor (NB! Variables must be private).

        :param name: client name
        :param balance: customer money
        :param client_type: client type
        """
        self.__name = name
        self.__balance = balance
        self.__client_type = client_type

        self.__order_history: list['Order'] = []  # Kliendi ostu ajalugu

    def get_name(self):
        """Return client name."""
        return ""

    def get_client_type(self) -> ClientType:
        """
        Return the customer type.

        :return: ClientType
        """
        pass

    def set_client_type(self, value: ClientType):
        """
        Set customer's status.

        :param value: ClientType
        """
        pass

    def get_balance(self) -> float:
        """
        Return the customer's money balance.

        :return: float
        """
        return 0.0

    def get_history(self) -> list['Order']:
        """
        Return customer's purchase history.

        Returns our customer's purchase history as a copy of the purchase history
        Use deepcopy.So that changes made with the dictionary in the class
        do not affect the dictionary object that does not belong to the class.
        :return: list['Order']
        """
        pass

    def clear_history(self):
        """Clear the purchase history."""
        pass

    def get_member_balance(self) -> float:
        """
        The sum of all purchases made by the member's history.

        :return: float: the sum
        """
        return 0.0

    def buy(self, order: 'Order') -> bool:
        """
        Purchasing process.

        The purchase price is calculated.
        If the customer has enough money, a purchase will be made.
        The customer pays for the purchase and the purchase is added to the purchase history.
        If all succeeded will be returned True, otherwise False.
        :param order:
        :return: boolean
        """
        pass

    def __repr__(self):
        """String representation of the client."""
        return f"{self.__name} - {self.get_client_type().name} customer"


class PetrolStation:
    """Petrol Station with fuel and shop items."""

    def __init__(self, fuel_stock: dict[Fuel, float], shop_item_stock: dict[ShopItem, float]):
        """
        Constructor (NB! Variables must be private).

        Used the deepcopy.
        So that changes made with the dictionary in the class do not affect the
        dictionary object that does not belong to the class.

        :param fuel_stock: fuel tank
        :param shop_item_stock: products warehouse
        """
        # define variables here

    def add_fuel(self, fuel: Fuel, quantity: float):
        """
        Add fuel to the tank.

        :param fuel:
        :param quantity:
        """
        pass

    def add_shop_item(self, item: ShopItem, quantity: float):
        """
        Add goods to the warehouse.

        :param item:
        :param quantity:
        """
        pass

    def remove_fuel(self, fuel: Fuel, quantity: float):
        """
        Remove fuel.

        Fuel is dispensed from the tank, first it is checked whether
        it is possible to dispense as much fuel,
        if so, then the quantity of the fuel in the tank is lowered,
        if not, the error RuntimeError() is thrown out.

        :param fuel:
        :param quantity:
        """
        pass

    def remove_items(self, item: ShopItem, quantity: float):
        """
        Remove items.

        The product is released from the warehouse, first it is
        checked whether it is possible to dispense as many products, if so,
        then the quantity of the product is lowered,
        if not, the error RuntimeError () is thrown out.

        :param item:
        :param quantity:
        """
        pass

    def get_fuel_dict(self) -> dict[Fuel, float]:
        """Return dict with Fuel objects as keys and quantities as values."""
        pass

    def get_shop_item_dict(self) -> dict[ShopItem, float]:
        """Return dict with ShopItem objects as keys and quantities as values."""
        pass

    def get_sell_history(self) -> dict[Client, list[Order]]:
        """Return sell history dict where key is Client, value is a list of Orders."""
        pass

    def sell(self, items_to_sell: list[tuple[OrderItem, float]], client: Client = None):
        """
        Sell item.

        If there are not enough items in the station, raise RuntimeError().
        In that case, the quantities of the items should not be changed.

        Use the parameter items_to_sell to create a Purchase Receipt Order
        (must be converted to tuple -> dict format), date put today's date.

        Then do the following with the client:

        Check if his loyalty status is valid.

        Check how much time this customer has had since the last purchase,
        if 2 months or more or there are no purchase history,
        the user will be downgraded to Bronze level
        and their purchase history will be cleared.
        Use customer purchase history instead of Petrol station's history
        as the customer can buy stuff from other stations.

        If the customer is not a regular customer, it remains Basic

        An attempt is made to sell the purchase to the customer
        (through the purchase method), if this is successful,
        the purchase is transferred to the sales archive of
        the service station, the type of which is dict.
        The key is the customer and the valueon his purchase.

        If the purchase is successful, we will try to raise the level of the customer

        Check how much the user has spent and if he has spent enough to move
        to the next status, his status will change.

        :param items_to_sell: is the customer's purchase request,
        given in the form of a `tuple`,
        which contains the position (fuel or product) and the quantity
        (NB! the quantity is always a` float`, even if the number is a product)
        :param client: is a customer, but the customer can be specified as None,
        in which case a new customer must be created with `Basic` status and a
        sufficient amount of money to purchase
        """
        pass
