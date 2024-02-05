#!/usr/bin/python3
"""Defines a class Rectangle that inherits from BaseGeometry."""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Represent A Rectangle using Base-Geometry."""

    def __init__(self, width, height):
        """Intialize the new Rectangle.

        Args:
            width (int): Width of the new Rectangle.
            height (int): Height of the new Rectangle.
        """
        self.integer_validator("Width", width)
        self.__width = width
        self.integer_validator("Height", height)
        self.__height = height
