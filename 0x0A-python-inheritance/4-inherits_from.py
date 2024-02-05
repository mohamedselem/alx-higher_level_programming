#!/usr/bin/python3
"""Defines Inherited class Checking Function."""


def inherits_from(obj, a_class):
    """Checks if the object is an inherited instance of a class.

    Args:
        obj (any): The object to be checked.
        a_class (type): The class to be matched the type of OBJ.
    Returns:
        If OBJ is an inherited instance of a_class - True.
        ELSE - False.
    """
    if issubclass(type(obj), a_class) and type(obj) != a_class:
        return True
    return False
