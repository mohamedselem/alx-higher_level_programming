#!/usr/bin/python3
"""Defines tHE Rectangle class."""


class Rectangle:
    """Represent THE Rectangle."""

    def __init__(self, width=0, height=0):
        """Initialize THE New reectangle.

        Args:
            width (int): width of new rectangle.
            height (int): height of new rectangle.
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """Get/set width of the NEW rectangle."""
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
        """Get/set height of the new rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height should be integer")
        if value < 0:
            raise ValueError("height should be >= 0")
        self.__height = value
