#!/usr/bin/python3
"""Defines Class and inherite class Checking Function."""


def is_kind_of_class(obj, a_class):
    """Check if the object is instance or inherited instance of a class.

    Args:
        obj (any): The object will be checked.
        a_class (type): The class to be matched the type of OBJ to.
    Returns:
        If obj is an instance or inherited instance of aclass - True.
        else - False.
    """
    if isinstance(obj, a_class):
        return True
    return False
