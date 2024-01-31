#!/usr/bin/python3
"""Defines the Rectangle class."""


class Rectangle:
    """Represent THE rectangle."""

    def __init__(self, width=0, height=0):
        """Initialize THE NEW Rectangle.

        Args:
            width (int): width of the new rectangle.
            height (int): height of the new rectangle.
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """Get or set width of the Rectangle."""
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
        """Get or set height of the Rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height should be an integer")
        if value < 0:
            raise ValueError("height should be >= 0")
        self.__height = value

    def area(self):
        """Return the area of the Rectangle."""
        return (self.__width * self.__height)

    def perimeter(self):
        """Return the perimeter of the Rectangle."""
        if self.__width == 0 or self.__height == 0:
            return (0)
        return ((self.__width * 2) + (self.__height * 2))
