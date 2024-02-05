#!/usr/bin/python3
"""Defines the  Base geometry class Base Geometry."""


class BaseGeometry:
    """Reprsent Base geometry."""

    def area(self):
        """Not implemented yet."""
        raise Exception("area() isn't implemented")

    def integer_validator(self, name, value):
        """Validate a parameter as Integer.

        Args:
            name (str): Name of the parameter.
            value (int): Parameter to be validated.
        Raises:
            TypeError: If value isn't integer.
            ValueError: If value is <= 0.
        """
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
