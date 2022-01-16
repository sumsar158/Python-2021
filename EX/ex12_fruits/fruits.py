"""Fruits delivery application."""


class Product:
    """Product class."""

    def __init__(self, name, price):
        """
        Product constructor.

        Expected name and price parameters.
        """
        self.price = price
        self.name = name

    def __repr__(self):
        """Represents product by name."""
        return self.name


class Order:
    """Order class."""

    def __init__(self):
        """
        Order constructor.

        Expected default customer parameter starting from Part 3. Also, products dictionary
        is expected to be created and products names set as a helper.
        """
        self.products_to_order = {}

    def get_products_string(self) -> str:
        """
        Method for converting products to a string.

        The template for a single product conversion into a string is 'product_name: product_amount kg'.
        If there are several products in the resulting string, separate them with a comma and space, but in the end
        of such long string there should be no comma, nor string. Example:
        'Avocado: 2 kg, Orange: 1 kg, Papaya: 3 kg, Cherry tomato: 2 kg'
        """
        pass

    def add_product(self, product: tuple):
        """Method for adding a single product to the dictionary."""

        if product[0] not in self.products_to_order.keys():
            self.products_to_order[product[0]] = 0
        if product in self.products_to_order.items():
            self.products_to_order[product[0]] += product[1]

    def add_products(self, products):
        """Method for adding several products to the dictionary."""
        for p in products:
            if p[0] not in self.products_to_order.keys():
                self.products_to_order[p[0]] = 0
            if p in self.products_to_order.items():
                self.products_to_order[p[0]] += p[1]

    def get_products(self):
        return self.products_to_order


class App:
    """
    App class.

    Represents our app, which should remember, which customer ordered what (starting from Part 3).
    Also, this is the place (interface) from where orders should be composed.
    """

    def __init__(self):
        """App constructor, no arguments expected."""
        self.products = []
        self.orders = []
        self.customers = []

    def get_products(self) -> list:
        """Getter for products list."""
        return self.products

    def find_product_by_name(self, name: str) -> Product:
        for product in self.products:
            if product.name == name:
                return product

    def get_orders(self) -> list:
        """Getter for orders list."""
        return self.orders

    def import_products(self) -> list[Product]:
        """
        Import products from a file, return list of Product objects.

        Filename is an argument here.
        """
        self.products = []
        with open("pricelist.txt") as f:
            for line in f:
                line = line.strip()
                line = line.replace(" ", "")
                line = line.split("-")
                p = Product(name=str(line[0]), price=float(line[-1]))
                self.products.append(p)
        print(self.products)
        return self.products

    def order_products(self, product):
        """Order products in general.

        The parameter is list of products. Create a new order, then add passed products to
        this order, then add this order to the orders list.
        Products here is list of tuples.
        """
        order = Order()
        if type(product) == list:
            o = order.add_products(products=product)
            self.orders.append(o)
        else:
            o = order.add_product(product)
            self.orders.append(o)

    def order(self, name, orders):
        """
        Method for ordering products for a customer.

        Products here is list of tuples.
        """
        pass

    def add_customer(self, customer):
        """Method for adding a customer to the list."""
        self.customers.append(customer)

    def add_customers(self, customers: list['Customer']):
        """Method for adding several customers to the list."""
        for customer in customers:
            self.customers.append(customer)

    def show_all_orders(self) -> str:
        """
        Method for returning all orders for all customers.

        If is_summary is true, add totals for each customer
        and also global total price.
        """
        pass

    def calculate_total(self) -> float:
        """Method for calculating total price for all customer's orders."""
        pass

    def calculate_summary(self):
        """Method for printing a summary of all orders with totals and the total for all customers' all orders."""
        pass


class Customer:
    """Customer to implement."""
    def __init__(self, name: str, location: str):
        self.location = location
        self.name = name
        self.orders = []

    def add_new_order(self, order):
        self.orders.append(order)

    def get_name(self):
        return self.name

    def get_address(self):
        return self.location

    def get_orders(self):
        return self.orders

if __name__ == '__main__':
    app = App()
    # Adding default customers to our app.
    app.add_customers([Customer("Anton", "home"), Customer("Rubber Duck", "home-table"), Customer("Svetozar", "Dorm 1"),
                       Customer("Toivo", "Dorm 2"), Customer("Muhhamad", "Muhha's lair"), Customer("test", "TEST")])
    # Ordering some food for everyone.
    app.order("Anton", [("Avocado", 2), ("Orange", 1), ("Papaya", 3), ("Cherry tomato", 2)])
    app.order("Anton", [("Avocado", 4), ("Orange", 2), ("Papaya", 3), ("Cherry tomato", 2)])
    app.order("Rubber Duck", [("Mango Irwin", 6)])
    app.order("Svetozar", [("Lemon", 1)])
    app.order("Svetozar", [("Grapefruit", 10)])
    app.order("Muhhamad", [("Grenades", 13), ("Cannon", 1), ("Red pepper", 666)])
    app.order("Toivo", [("Granadilla", 3), ("Chestnut", 3), ("Pitaya(Dragon Fruit)", 3)])

    print(app.find_product_by_name(name="Eggplant"))
    print(app.find_product_by_name(name="lol"))

    # Checking products list.
    print(app.get_products())
    print("=======")
    # Checking how all orders and summary look like.
    print(app.show_all_orders(False))
    print("=======")
    print(app.show_all_orders(True))
    print("=======")
    app.calculate_summary()
