#!/usr/bin/python3
"""Defines Rectangle CLass."""


class Rectangle:
    """Represent Rectangle."""

    def __init__(self, width=0, height=0):
        """Initialize New Rectangle.

        Args:
            width (int): Width of New rectangle.
            height (int): Height of New rectangle.
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
            raise TypeError("width should be an integer")
        if value < 0:
            raise ValueError("width should be >= 0")
        self.__width = value

    @property
    def height(self):
        """Get | set Height of the Rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height SHOULD be an integer")
        if value < 0:
            raise ValueError("height SHOULD be >= 0")
        self.__height = value

    def area(self):
        """Return the area of the Rectangle."""
        return (self.__width * self.__height)

    def perimeter(self):
        """Return the perimeter of the Rectangle."""
        if self.__width == 0 or self.__height == 0:
            return (0)
        return ((self.__width * 2) + (self.__height * 2))

    def __str__(self):
        """Return the printable representation of the Rectangle.

        Represents the rectangle with the # character.
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
        """Return the string representation of the Rectangle."""
        rect = "Rectangle(" + str(self.__width)
        rect += ", " + str(self.__height) + ")"
        return (rect)
