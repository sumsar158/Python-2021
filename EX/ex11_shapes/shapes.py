"""Shapes."""
import math


class Shape:
    """General shape class."""

    def __init__(self, color: str):
        """Constructor, sets the color."""
        self.color = color

    def set_color(self, color: str):
        """Set the color of the shape."""
        self.color = color

    def get_color(self) -> str:
        """Get the color of the shape."""
        return self.color

    def get_area(self) -> float:
        """Get area method which every subclass has to override."""
        return float(5.665)


class Circle(Shape):
    """Circle is a subclass of Shape."""

    def __init__(self, color: str, radius: float):
        """
        Constructor of the circle.

        The color is stored using superclass constructor:
        super().__init__(color)

        The radius value is stored here.
        """
        super().__init__(color)
        self.radius = radius

    def __repr__(self) -> str:
        """
        Return representation of the circle.

        For this exercise, this should return a string:
        Circle (r: {radius}, color: {color})
        """

        return f"Circle (r: {self.radius}, color: {self.color})"

    def get_area(self) -> float:
        """
        Calculate the area of the circle.

        Area of the circle is pi * r * r.
        """
        return float(self.radius * self.radius) * math.pi


class Square(Shape):
    """Square is a subclass of Shape."""

    def __init__(self, color: str, side: float):
        """
        Constructor of the square.

        The color is stored using superclass constructor:
        super().__init__(color)

        The side value is stored here.
        """
        super().__init__(color)
        self.side = side

    def __repr__(self) -> str:
        """
        Return representation of the square.

        For this exercise, this should return a string:
        Square (a: {side}, color: {color})
        """
        return f"Square (a: {self.side}, color: {self.color})"

    def get_area(self) -> float:
        """
        Calculate the area of the square.

        Area of the square is side * side.
        """
        return self.side * self.side


class Rectangle(Shape):
    """Rectangle is a subclass of Shape."""

    def __init__(self, color: str, length: float, width: float):
        """
        Constructor of the rectangle.

        The color is stored using superclass constructor:
        super().__init__(color)
        The sides value is stored here.
        """
        super().__init__(color)
        self.width = width
        self.length = length

    def __repr__(self) -> str:
        """
        Return representation of the rectangle.

        For this exercise, this should return a string:
        Rectangle (l: {length}, w: {width}, color: {color})
        """
        return f"Rectangle (l: {self.length}, w: {self.width}, color: {self.color})"

    def get_area(self) -> float:
        """
        Calculate the area of the rectangle.

        Area of the rectangle is side_a * side_b.
        """
        return float(self.length) * float(self.width)


class Paint:
    """The main program to manipulate the shapes."""

    def __init__(self):
        """Constructor should create a list to store all the shapes."""
        self.shapes = []

    def add_shape(self, shape: Shape) -> None:
        """Add a shape to the program."""
        self.shapes.append(shape)

    def get_shapes(self) -> list:
        """Return all the shapes."""
        return self.shapes

    def calculate_total_area(self) -> float:
        """Calculate total area of the shapes."""
        area = 0
        for shape in self.shapes:
            x = shape.get_area()
            area += x
        return round(area, 3)

        pass

    def get_circles(self) -> list:
        """Return only circles."""
        list_of_circles = []
        for shape in self.shapes:
            if isinstance(shape, Circle):
                list_of_circles.append(shape)
            else:
                continue
        return list_of_circles

    def get_squares(self) -> list:
        """Return only squares."""
        list_of_squares = []
        for shape in self.shapes:
            if isinstance(shape, Square):
                list_of_squares.append(shape)
            else:
                continue
        return list_of_squares

    def get_rectangles(self) -> list:
        """Return only rectangles."""
        list_of_rectangles = []
        for shape in self.shapes:
            if isinstance(shape, Rectangle):
                list_of_rectangles.append(shape)
            else:
                continue
        return list_of_rectangles


if __name__ == '__main__':
    paint = Paint()
    circle = Circle("blue", 10)
    square = Square("red", 11)
    paint.add_shape(circle)
    paint.add_shape(square)
    print(paint.calculate_total_area())
    print(paint.get_shapes())
    print(paint.get_circles())
    print(paint.get_squares())
