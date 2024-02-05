#!/usr/bin/python3
"""Defines class Base-Geometry."""


class BaseGeometry:
    """Class Body."""

    def area(self):
        """Not implemented yet."""
        raise Exception("area() isn't implemented")

    def integer_validator(self, name, value):
        """Validate a parameter format.
            TypeError: If value isn't  integer.
            ValueError: If value is <= 0.
        """
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
