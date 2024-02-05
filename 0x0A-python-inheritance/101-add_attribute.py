#!/usr/bin/python3
"""Defines Functions that ADD attributes to OBJ."""


def add_attribute(obj, att, value):
    """Add new attribute to an OBJ if possible.

    Args:
        obj (any): OBJ to be added an attribute to.
        att (str): name of the attribute to add to obj.
        value (any): The value of attribute.
    Raises:
        TypeError: If the attribute can not be added.
    """
    if not hasattr(obj, "__dict__"):
        raise TypeError("can not add new attribute")
    setattr(obj, att, value)
