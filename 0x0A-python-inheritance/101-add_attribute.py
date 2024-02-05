#!/usr/bin/python3
"""Define the function attributes."""


def add_attribute(obj, att, value):
    """Add  NEW attribute to an object if possible.
    Raises:
        TypeError: If the attribute cannot be added.
    """
    if not hasattr(obj, "__dict__"):
        raise TypeError("can not ADD new attribute")
    setattr(obj, att, value)
