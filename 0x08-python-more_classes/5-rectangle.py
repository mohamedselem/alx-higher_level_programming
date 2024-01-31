#!/usr/bin/python3
"""Defines Rectangle CLass."""


class Rectangle:
    """Represent THE Rectangle."""

    def __init__(self, width=0, height=0):
        """Initialize new Rectangle.

        Args:
            width (int): width of new rectangle.
            height (int): height of new rectangle.
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """Get | set Width of the Rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width SHOULD be integer")
        if value < 0:
            raise ValueError("width SHOULD be >= 0")
        self.__width = value

    @property
    def height(self):
        """Get | set Height of the Rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height SHOULD be integer")
        if value < 0:
            raise ValueError("height SHOULD be >= 0")
        self.__height = value

    def area(self):
        """Return Area of the Rectangle."""
        return (self.__width * self.__height)

    def perimeter(self):
        """Return Perimeter of the Rectangle."""
        if self.__width == 0 or self.__height == 0:
            return (0)
        return ((self.__width * 2) + (self.__height * 2))

    def __str__(self):
        """Return printable representation of the Rectangle.

        Represents rectangle with the # character.
        """
        if self.__width == 0 or self.__height == 0:
            return ("")

        rect = []
        for i in range(self.__height):
            [rect.append('#') for j in range(self.__width)]
            if i != self.__height - 1:
                rect.append("\n")
        return ("".join(rect))

    def __repr__(self):
        """Return String representation of the Rectangle."""
        rect = "Rectangle(" + str(self.__width)
        rect += ", " + str(self.__height) + ")"
        return (rect)

    def __del__(self):
        """Print a message for every deletion of a Rectangle."""
        print("Bye rectangle...")
