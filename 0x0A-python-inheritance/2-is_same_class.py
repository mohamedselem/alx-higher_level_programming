#!/usr/bin/python3
"""Defines Class Checking Function."""


def is_same_class(obj, a_class):
    """Check if the object is similar to  an instance of a given class.

    Args:
        obj (any): The object will be checked.
        a_class (type): The class to be matched the type of obj to.
    Returns:
        If obj is exactly an instance of a_class - True.
        Otherwise - False.
    """
    if type(obj) == a_class:
        return True
    return False
