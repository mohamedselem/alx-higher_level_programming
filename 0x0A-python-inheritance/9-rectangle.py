#!/usr/bin/python3
"""Defines Class Rectangle that inherit from Base-Geometry."""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Represent Rectangle using BaseGeometry."""

    def __init__(self, width, height):
        """Intialize New Rectangle.

        Args:
            width (int): Width of new Rectangle.
            height (int): Height of new Rectangle.
        """
        super().integer_validator("width", width)
        self.__width = width
        super().integer_validator("height", height)
        self.__height = height

    def area(self):
        """Return the area of the rectangle."""
        return self.__width * self.__height

    def __str__(self):
        """Return the print() and str() represente of a Rectangle."""
        string = "[" + str(self.__class__.__name__) + "] "
        string += str(self.__width) + "/" + str(self.__height)
        return string
